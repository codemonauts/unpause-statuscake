# unpause-statuscake

I was missing the "Pause check for x hours" feature in StatusCake which I was used to from other monitoring solutions,
which is quite handy when you do maintenance and don't want to get alerted on a short downtime. Therefore I build this
script which checks all paused tests in your StatusCake account, and unpauses them if they have been paused for a given
amount of time.

## Usage
  * Install Python 3
  * Go to your StatusCake [User Details](https://app.statuscake.com/User.php) to get your username and an api key
  * `cp config.py.example config.py` and fill in your data
  * Run `python3 main.py` in an cron job or e.g. at AWS Lambda
