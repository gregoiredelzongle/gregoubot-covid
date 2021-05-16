# Gregou Bot Covid

A bot to get a chronodose vaccine in France using **Doctolib**, faster than **ViteMaDose** and tailored for your needs !
Based on [this repo](https://github.com/bntan/doctolib-covid) , but with more features :

- Parallel requests
- Run on a loop
- Apprise notifications

## Setup
1. Clone/Download this repository
1. [Install Python 3.8](https://www.python.org/downloads/)
2. Go to your terminal/bash, go to the project folder and type `pip install -r requirements.txt` (or `pipenv install` if you want to use virtualenv)

## Setup Notifications
The script use [Apprise for notifications](https://github.com/caronc/apprise). You have to create a `.config/apprise.conf` file and setup your notifications preferences from there. I recommand using [Telegram](https://github.com/caronc/apprise/wiki/Notify_telegram) but you can use many more services listed [here][https://github.com/caronc/apprise#popular-notification-services), for example SMS, desktop notifications, mail, Discord, etc ...

## Setup Centers
The script goes through selected centers and check for availability, so make sure you populate `.config/centers.conf` with vaccine centers (to add one, go to doctolib and copy the name of the center from the url.

Example :
```
https://www.doctolib.fr/centre-de-sante/saint-mande/centre-de-vaccinations-covid-saint-mande
```
When added to the `.config/centers.conf` file :
```
...
centre-de-vaccinations-covid-saint-mande
...
```

## Usage
Run the script using `python app.py` inside the project folder


