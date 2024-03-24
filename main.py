import time
import random
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def genera_parola_casuale():
    vocali = 'aeiou'
    consonanti = 'bcdfghlmnpqrstvz'
    parola = ''

    # Scegli una lunghezza casuale per la parola
    lunghezza_parola = random.randint(3, 25)
    for i in range(lunghezza_parola):
        if i % 2 == 0:
            parola += random.choice(consonanti)
        else:
            parola += random.choice(vocali)
    return parola


def genera_lista_parole_casuali(n):
    lista_parole = []
    for _ in range(n):
        parola = genera_parola_casuale()
        lista_parole.append(parola)
    return lista_parole


# GLOBAL VARIABLES
bing_website = 'https://www.bing.com/'
cookie_button_id = 'bnp_btn_accept'
hamburger_menu_id = 'mHamburger'
access_button_xpath = '/html/body/div[2]/div/div[3]/header/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/a[1]'
search_bar_id = 'sb_form_q'

# ! DESKTOP SETTINGS
# Creo il driver per fare i punti su desktop
desktop_driver = webdriver.Edge()

# ! MOBILE SETTINGS
# Creo il driver per fare i punti su mobile
mobile_edge_options = EdgeOptions()
mobile_edge_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
mobile_driver = webdriver.Edge(options=mobile_edge_options)

# ! Esecuzione
# Apro la pagina principale di bing e attendo che si carichi
desktop_driver.get(bing_website)
mobile_driver.get(bing_website)
time.sleep(6)

# Salvo la posizione del tasto per accettare i cookie e lo clicco
desktop_cookie_button = desktop_driver.find_element(By.ID, cookie_button_id)
desktop_cookie_button.click()
mobile_cookie_button = mobile_driver.find_element(By.ID, cookie_button_id)
mobile_cookie_button.click()
time.sleep(3)
desktop_driver.refresh()

# Trovo e apro l'hamburger menu su mobile
mobile_hamburger_menu = mobile_driver.find_element(By.ID, hamburger_menu_id)
mobile_hamburger_menu.click()
time.sleep(1)

# Trovo e clicco il tasto per effettuare il login al mio account su mobile
mobile_access_button = mobile_driver.find_element(By.XPATH, access_button_xpath)
mobile_access_button.click()
time.sleep(1)

# Creo una lista di 50 parole generate casualmente per fare le ricerche
desktop_word_list = genera_lista_parole_casuali(50)
mobile_word_list = genera_lista_parole_casuali(50)
for index, (desktop_word, mobile_word) in enumerate(zip(desktop_word_list, mobile_word_list)):
    print(f"Desktop word {index}: {desktop_word}")
    print(f"Mobile word {index}: {mobile_word}")
    # Aspetto 6 secondi per permettere al sito di registrare i punti e poi passo alla parola successiva
    time.sleep(6)

    # Trovo e salvo la barra di ricerca di desktop e mobile
    desktop_edge_search_bar = desktop_driver.find_element(By.ID, search_bar_id)
    mobile_edge_search_bar = mobile_driver.find_element(By.ID, search_bar_id)

    # Seleziono tutto il testo dalla barra di ricerca
    desktop_edge_search_bar.send_keys(Keys.CONTROL, "a")
    mobile_edge_search_bar.send_keys(Keys.CONTROL, "a")

    # Scrivo la parola da ricercare nella barra di ricerca
    desktop_edge_search_bar.send_keys(desktop_word)
    mobile_edge_search_bar.send_keys(mobile_word)

    # Effettuo la ricerca
    desktop_edge_search_bar.send_keys(Keys.ENTER)
    mobile_edge_search_bar.send_keys(Keys.ENTER)
