<center># kopmaz-py_read_google_analytics_data_write_to_postgresql</center>
</br>
<a href="https://kopmaz.ch" target="blank"><img src="https://kopmaz.ch/wp-content/uploads/2019/06/kopmazch481x97.png"> </a>
</br>

Note: This is just an example, you can improve and adapt your Postgresql scheme to data write process. Also able to adapt my Telegram bot script to send you daily reports with charts.

------------ Requirements ------------

- Python 3
- Google Analytics Account
- Postgresql Server

------------ Features ------------

- Read Google Analytics data via Python
- Write data to Postgresql Server

</br>
------------ Instructions ------------
</br>
1. Create a service account on Google:
</br>
Documentation: https://developers.google.com/android/management/service-account
</br>
2. Grant User Access in Google Analytics:
</br>
Documentation: https://www.monsterinsights.com/docs/how-to-grant-user-access-in-google-analytics/
</br>
3. You need Python3 to run this code, first we are going to check is it installed or not:
</br>
<code>python3 --version</code>
</br>
If you see a response like "Python 3.x.x", then you have Python3 on your machine. Please skip the next step.
</br>
4. Python3 installation for Debian based Linux distrubitions:
</br>
<code>sudo apt-get install python3.7</code>
</br>
<code>sudo apt-get update</code>
</br>
<code>sudo apt-get -y upgrade</code>
</br>
5. Go inside of the repository folder:
</br>
<code>cd py_health_check-master</code>
</br>
6. Change the Credentials:
</br>
You have to change the credentials with yours. Example: 
7. Running the py_health_check:
</br>
<code>python3 py_read_google_analytics_data_write_to_postgresql.py</code>
</br>
Thanks!
</br>
My e-mail for github: github@kopmaz.ch

*You can create free Heroku account for Postgresql tests. Link: https://www.heroku.com/postgres
