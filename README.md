# Gregou Bot Covid

A bot to get a chronodose vaccine in France using Doctolib, faster than ViteMaDose and tailored for your needs !
Based on [this repo](https://github.com/bntan/doctolib-covid) , but with more features :

- Parallel requests
- Run on a loop
- Apprise notifications

## Setup
1. Clone/Download this repository
1. [Install Python 3.8](https://www.python.org/downloads/)
2. Go to your terminal/bash, go to the project folder and type `pip install -r requirements.txt` (or `pipenv install` if you want to use virtualenv)
3. Setup [Apprise for notifications](https://github.com/caronc/apprise) : Copy `.config/apprise_example.conf` to `apprise.conf`, and copy there your credentials (examples are provided inside). Apprise is a service used to send you notifications without any hassle. You can use your favorite notification provider (desktop,sms,mail,Telegram,Discord etc...). See [This](https://github.com/caronc/apprise#popular-notification-services) to get your credentials.
4. Use the .config/centers.conf provided to add or remove vaccines centers. Some are already being provided.

## Usage
Run the script using `python app.py` inside the project folder
