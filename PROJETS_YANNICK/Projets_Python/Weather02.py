#################################################################
# Programme météo                                               #
# Auteur: [Yohanan N]                                           #
# Date: 03 Novembre 2024                                        #
# Description: Une application Python qui récupère les données  #
#      de prévision météorologique du site web "OpenWeatherMap" #
#      en fonction du code postal ou du nom de la ville et      #
#      les affiche dans un format lisible.                      #
#                                                               #
#################################################################

# Importation des bibliothecques
import requests
import json

# import only system from os
from os import system, name

# Define the Global vaiable
# Url permettant de rcupeerer les donnee a partir du non de la ville
API_URL_NAME_VILLE = f"https://api.openweathermap.org/geo/1.0/direct?"
# Url permettant de rcupeerer les donnee a partir du Zip Code
API_URL_ZIP_CODE = f'https://api.openweathermap.org/geo/1.0/zip?'
# Url final permettant de rcupeerer les donnee
API_URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?"
longitude = 0.0
lattitude = 0.0
Location = ""
API_KEY = "d5751b1a9e2e4b2b8c7983646072da8b"
Text_To_Print = ""


def convert_temp(temperature, unite):
    """
    Convertit une température en Celsius vers Fahrenheit, Kelvin, Réaumur et Rankine.
    :param unite : unite de convertion de la temperature de sortie
        1 - Fahrenheit
        2 - Kelvin
        3 - Rankine
        4 - Celsius
    :param temperature: température en degrés Celsius
    """
    # Calcul des différentes conversions
    convert = 0.0
    temp_name = ''
    match unite:
        case '1':
            convert = ((temperature * 9 / 5) + 32)
            temp_name = '°F'
        case '2':
            temp_name = '°K'
            convert = temperature + 273.15
        case '3':
            temp_name = '°R'
            convert = temperature * 4 / 5
        case '4':
            temp_name = '°C'
            convert = (temperature + 273.15) * 9 / 5
        case _:
            temp_name = '°C'
            convert = temperature
    return "{:.2f}".format(convert)+" "+temp_name


# Fonction permettant d'effacer l'ecran
def clear_scream():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Fonction pour obtenir les coordonnées (latitude et longitude) à partir du code postal ou de la ville
def obtenir_coordonnees(api_key, location, mode_find):
    """
    :param api_key: cle de l'api openweather
    :param location: variable permettant de contenir le nom de la ville ou,le zip code
    :param mode_find: mode de recherche du lieu
        1 - Zip Code
        2 - Nom de la ville
    :return: Lattitude et logitude d'une ville donnee
    """
    if mode_find == 1:
        # Construction de l'url final a partir du zip code
        url = API_URL_ZIP_CODE + f"zip={location}&limit=1&appid={api_key}"
    else:
        # Construction de l'url final a partir du nom de la ville
        url = API_URL_NAME_VILLE + f"q={location}&limit=1&appid={api_key}"
    try:
        # recuperation de donnee methorologique
        response = requests.get(url)
        # Test de Verification de l'existance des donnees
        if response.status_code == 200:
            # Convertion des donnees recuperer au format Json
            data = response.json()
            # Test de verification si le conversion au format Json s'est bien deroule et non vide '
            if len(data) > 0:
                # recuperation de la longitude et de la lattitude
                return data[0]['lat'], data[0]['lon']
            else:
                print("Lieu non trouvé.")
        else:
            print("Erreur lors de la récupération des coordonnées.")
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax:", e)
    return None, None


# Fonction pour obtenir les données météo en utilisant la latitude et la longitude
def obtenir_meteo(api_key, lat, lon, units):
    """

    :param api_key:
    :param lat:
    :param lon:
    :param units:
    :return:
    """
    # Construction de l'url final de recuperation des donnee a l'aide de la longitude et de la lattitude
    url = API_URL_WEATHER + f"lat={lat}&lon={lon}&units={units}&appid={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erreur lors de la récupération des données météo.")
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax:", e)
    return None


# Fonction principale pour exécuter l'application
def programme_meteo():
    # Variable permettant de verifier si l'utilisateur souhaite continuer a execute le programme'
    exit_weather_find = False
    # Variable conetnant le mode de recherche du lieu. Recherche par Zip code ou sur le nom de la ville
    find_mode = ""
    # Debut du programme avec test de continuite
    while not exit_weather_find:
        # Variable permettant a l'uitilisateur d'effectuer un choix parmis une liste restreinte
        choice_list = ["1", "2", "q"]
        # variable contenant le choix de l'operation a effectuer'
        choice = ""
        # Selection du mode de recherche
        while choice not in choice_list:
            choice = ""
            clear_scream()
            print("\nSelection un mode de recheche :\n"
                  "1 - Code Postal\n"
                  "2 - Nom de Ville/État\n"
                  "Q - Quitter\n")
            choice = input("Votre choix : ").lower().strip()
        match choice.lower():
            case "1":
                text_to_print = "Zip Code  : "
                find_mode = '1'
            case "2":
                text_to_print = "Nom de la Ville : "
                find_mode = '2'
            case "q":
                print("\n>>> Bye Bye <<<\n")
                exit(0)
            case _:
                text_to_print = ""
        # recuperation de l'information utilisateur
        location = input(text_to_print).lower().strip()
        choice_list = ["1", "2", "3", "q"]
        choice = ""
        # Recuperation de l'unite de la metri
        while choice not in choice_list:
            choice = ""
            clear_scream()
            print("Choisissez les unités\n"
                  "1 - metric\n"
                  "2 - imperial\n"
                  "3 - standard\n"
                  "Q - Quitter\n")
            choice = input("Votre choix : ").lower().strip()
        match choice.lower():
            case "1":
                unite = "metric"
            case "2":
                unite = "imperial"
            case "3":
                unite = "standard"
            case "q":
                print("\n>>> Bye Bye <<<\n")
                exit(0)
            case _:
                unite = ""
        #Recuperation de la lattitude et de la longitude
        latitude, longitude = obtenir_coordonnees(API_KEY, location, find_mode)
        if latitude is not None and longitude is not None:
            #recuperation des donnees meteorologiaue
            meteo = obtenir_meteo(API_KEY, latitude, longitude, unite)
            if meteo:
                choice_list = ["1", "2", "3", "4", "5", "q"]
                choice = ""
                # recuperation de l'unite d"affichage de la temperature
                while choice not in choice_list:
                    choice = ""
                    clear_scream()
                    print("Chooisir unités de la temperature\n"
                          "1 - Fahrenheit\n"
                          "2 - Kelvin\n"
                          "3 - Rankine\n"
                          "4 - Celsius\n"
                          "Q - Quitter\n")
                    choice = input("Votre choix : ").lower().strip()
                if choice.lower().strip() != "q":
                    # Affichage des resultat de la recherche et de la recupereation des donnee de la meteo
                    afficher_meteo(meteo, choice)
                else:
                    print("\n>>> Bye Bye <<<\n")
                    exit(0)
            else:
                print("Veuillez entrer un lieu valide.")
        choice_list = ["0", "1"]
        choice = ""
        #verification si l'utilisateur souhaite effectuer une nouvelle recherche de meteo
        while choice not in choice_list:
            choice = ""
            print("\nNouvelle recherche "
                  "? \n 0 - Oui \n 1 - Non \n")
            choice = input("Votre choix : ").lower().strip()
        if choice == "1":
            exit_weather_find = True
            print("\n>>> Bye Bye <<<\n")
            exit(0)

# Fonction pour afficher les données météo
def afficher_meteo(meteo, unite):
    try:
        if meteo is not None:
            temperature = meteo['main']['temp']
            print(f"Lieu : {meteo['name']}, {meteo['sys']['country']}")
            print(f"Description : {meteo['weather'][0]['description']}")
            print(f"Humidité : {meteo['main']['humidity']}%")
            print(f"Vitesse du Vent : {meteo['wind']['speed']} m/s")
            print(f"Température actuelle : {convert_temp(meteo['main']['temp'], unite)}")
            print(f"Température ressentie : {convert_temp(meteo['main']['feels_like'], unite)}")
            print(f"Température minimum : {convert_temp(meteo['main']['temp_min'], unite)}")
            print(f"Température maximum : {convert_temp(meteo['main']['temp_max'], unite)}")
            print(f"Pression : {meteo['main']['pressure']} hPa")
        else:
            print("erreur lors de la recuperation des information")
    except FileNotFoundError:
        print("Error: The file 'gettysburg.txt' was not found.")
        return


if __name__ == "__main__":
    programme_meteo()
