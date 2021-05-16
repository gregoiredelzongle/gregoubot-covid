import time
import datetime
import requests
from notifications import Notifications
from multiprocessing import Pool

# Delay in seconds
DELAY_BETWEEN_CHECKS = 60

notification_handler = Notifications()


def read_centers(file):
    with open(file) as centers_file:
        centers = centers_file.readlines()
    centers = [center.strip() for center in centers
               if not center.startswith("#")]
    return centers


def check_for_availability(center):
    data = requests.get(
        f"https://www.doctolib.fr/booking/{center}.json").json()["data"]

    visit_motives = [visit_motive for visit_motive in data["visit_motives"]
                     if visit_motive["name"].startswith("1re injection") and
                     "AstraZeneca" not in visit_motive["name"]]
    if not visit_motives:
        print(
            f'Le centre {center} n\'a pas de rendez vous pour une 1ere injection de Pfizer ou Moderna')
        return

    places = [place for place in data["places"]]
    if not places:
        print(f'Le centre {center} n\'a pas d\'adresses attribuée')
        return

    for place in places:

        start_date = datetime.datetime.today().date().isoformat()
        visit_motive_ids = visit_motives[0]["id"]
        practice_ids = place["practice_ids"][0]
        place_name = place["formal_name"]
        place_address = place["full_address"]
        place_city = place["city"].lower()

        agendas = [agenda for agenda in data["agendas"]
                   if agenda["practice_id"] == practice_ids and
                   not agenda["booking_disabled"] and
                   visit_motive_ids in agenda["visit_motive_ids"]]
        if not agendas:
            continue

        agenda_ids = "-".join([str(agenda["id"]) for agenda in agendas])

        # print(visit_motive_ids)
        # print(practice_ids)
        # print(agenda_ids)
        response = requests.get(
            "https://www.doctolib.fr/availabilities.json",
            params={
                "start_date": start_date,
                "visit_motive_ids": visit_motive_ids,
                "agenda_ids": agenda_ids,
                "practice_ids": practice_ids,
                "insurance_sector": "public",
                "destroy_temporary": "true",
                "limit": 2
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'}

        )
        response.raise_for_status()
        nb_availabilities = response.json()["total"]
        result = str(nb_availabilities) + " appointments available at " + \
            place_name + " - " + place_address
        print(result)
        if (nb_availabilities > 0):
            result += '\nhttps://www.doctolib.fr/centre-de-sante/' + \
                place_city+'/'+center+'?pid=practice-'+str(practice_ids)
            notification_handler.send(result)


def main():
    notification_handler.send('Covid19 Doctolib tracker launched')

    centers = read_centers('.config/centers.conf')
    available = None
    num_tries = 0

    while(True):
        print(f"Vérification de centres disponibles ...")
        print(f"Nombre de centres : {len(centers)}")
        print(
            f"Nombre d'essais depuis le lancement du script : {num_tries}")
        pool = Pool(8)
        pool.map(check_for_availability, centers)
        pool.close()
        pool.join()

        # for center in centers:
        #    available = check_for_availability(center)
        #    if(available is not None):
        #        notification_handler.send(available)
        time.sleep(DELAY_BETWEEN_CHECKS)
        num_tries += 1


if __name__ == "__main__":
    main()
