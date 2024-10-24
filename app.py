# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# TODO: Pääohjelman ikuinen silmukka, josta poistutaan tarvittaessa (keksi mekanismi itse)
# TODO: Paranna pääohjelmaa siten, että se ei kaadu, kun käyttäjä syöttää virheellisen henkilötunnuksen
userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
userGivenLastname = input('Syötä asiakkan sukunimi')
# TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
userGivenFirstname = input('Syötä asiakkan etunimi')
# TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
# TODO: Varaudu tilanteeseen, jossa hetu:n tarkiste on annettu pienillä kirjaimilla
# TODO: Muuta syötettyjen nimien alkukirjain isoksi

ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
if ssnToCheck.isValidSsn() == True:
    ssnToCheck.getDateOfBirth()
    ssnToCheck.getGender()
    age = ssnToCheck.calculateAge()
    print('Syntymäaika:', ssnToCheck.dateOfBirth)
    print('Ikä:', age)
    print('Sukupuoli:', ssnToCheck.gender)

