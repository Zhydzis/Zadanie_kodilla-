#calculator
import logging

# Konfiguracja loggera
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def kalkulator():
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1: Dodawanie")
    print("2: Odejmowanie")
    print("3: Mnożenie")
    print("4: Dzielenie")
    
    dzialanie = input("Wybór: ")
    
    try:
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
    except ValueError:
        logging.error("Podano nieprawidłową wartość. Wprowadź liczby!")
        return
    
    if dzialanie == '1':
        logging.info(f"Dodaję {liczba1} i {liczba2}")
        print("Wynik:", liczba1 + liczba2)
    elif dzialanie == '2':
        logging.info(f"Odejmuję {liczba2} od {liczba1}")
        print("Wynik:", liczba1 - liczba2)
    elif dzialanie == '3':
        logging.info(f"Mnożę {liczba1} i {liczba2}")
        print("Wynik:", liczba1 * liczba2)
    elif dzialanie == '4':
        if liczba2 == 0:
            logging.error("Błąd: Próba dzielenia przez zero!")
            print("Błąd: Dzielenie przez zero!")
        else:
            logging.info(f"Dzielę {liczba1} przez {liczba2}")
            print("Wynik:", liczba1 / liczba2)
    else:
        logging.warning("Nieprawidłowy wybór!")
        print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    kalkulator()
