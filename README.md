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
The script use [Apprise for notifications](https://github.com/caronc/apprise). You have to create a `.config/apprise.conf` file and setup your notifications preferences from there. I recommand using [Telegram](https://github.com/caronc/apprise/wiki/Notify_telegram) but you can use many more services listed [here](https://github.com/caronc/apprise#popular-notification-services), for example SMS, desktop notifications, mail, Discord, etc ...

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

## Optional settings
By default, script checks for updates every 60 seconds. You can change it on `app.py` here :

```python
# Delay in seconds
DELAY_BETWEEN_CHECKS = 60
```

## Usage
Run the script using `python app.py` inside the project folder using the terminal/bash

Output example :
```
Nombre de centres : 26
Nombre d'essais depuis le lancement du script : 34
Le centre centre-de-vaccination-grand-chambery n'a pas de rendez vous pour une 1ere injection de Pfizer ou Moderna
0 appointments available at Mairie du 8ème arrondissement de Paris - 3 Rue de Lisbonne, 75008 Paris
0 appointments available at  - 78 Rue Bonaparte, 75006 Paris
0 appointments available at Mairie du 9e - Centre de Vaccination Covid - 6 Rue Drouot, 75009 Paris
0 appointments available at Centre de Vaccination - Salle Olympe de Gouges - 15 Rue Merlin, 75011 Paris
0 appointments available at Centre de Vaccination - Centre Médical International - 38 Quai de Jemmapes, 75010 Paris
0 appointments available at Gymnase Camou - 37 Avenue de la Bourdonnais, 75007 Paris
Le centre centre-de-vaccination-covid-19-des-sapeurs-pompiers-de-paris n'a pas de rendez vous pour une 1ere injection de Pfizer ou Moderna
0 appointments available at Centre de santé Bauchat Nation - 22 Rue du Sergent Bauchat, 75012 Paris
0 appointments available at Centre de Vaccination - Centre Bertheau - 15-17 Rue Charles Bertheau, 75013 Paris

```


