"""A simple example of how to access the Google Analytics API and store the specific data into Postgresql server."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import psycopg2

def get_service(api_name, api_version, scopes, key_file_location):

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service

def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
                accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                    accountId=account,
                    webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None


def get_results(service, profile_id):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the yesterday.
    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    return service.data().ga().get(
            ids='ga:' + profile_id,
            start_date=yesterday,
            end_date='today',
            metrics='ga:sessions').execute()

def update_db(results):
    today = datetime.strftime(datetime.now() - timedelta(), '%Y%m')
    if results:
        try:
            connection = psycopg2.connect(user="YourDatabaseUser",
                                          password="YourDatabaseUserPassword",
                                          host="YourDatabaseHost",
                                          port="5432",
                                          database="YourDatabaseName")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO traffic (visitor, yearmonth) VALUES (%s, %s) """
            record_to_insert = (results.get('rows')[0][0], today)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into traffic table")

        except (Exception, psycopg2.Error) as error:
            if (connection):
                print("Failed to insert record into traffic table", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed.")

def print_results(results):
    # Print data nicely for the user.
    if results:
        print ('View (Profile):', results.get('profileInfo').get('profileName'))
        print ('Total Sessions:', results.get('rows')[0][0])

    else:
        print ('No results found')


def main():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'YourKeyfileLocationFromGoogleAPIConsole'

    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    profile_id = get_first_profile_id(service)
    print_results(get_results(service, profile_id))
    update_db(get_results(service, profile_id))


if __name__ == '__main__':
    main()
