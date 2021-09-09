import logging
logging.basicConfig(level=logging.INFO)

def calkulator(operation, elements):
    if operation == 1:
        logging.info("You choose dodawanie with arguments: {}".format(elements))
        print("Wynik = ", sum(elements))
    elif operation == 2:
        logging.info("You choose odejmowanie with arguments: {}".format(elements))
        print("Wynik = ",elements[0] - sum(elements[1:])) #Od pierwszej liczby odejmuje pozostałe z listy
    elif operation == 3:
        logging.info("You choose mnożenie with arguments: {}".format(elements))
        print("Wynik = ", elements[0] * elements[1])
    elif operation == 4:
        logging.info("You choose dzielenie with arguments: {}".format(elements))
        print("Wynik = ", elements[0] / elements[1])
    else:
        print("This operation doesn't exist. Choose another number.")

if __name__ == "__main__":
    operation=int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if type(operation) != int:
        print(operation, "isn't integer")

    elements = input("Podaj argumenty działania odzielone spacją: ").split()
    elements = [int(i) for i in elements]
    for i in elements:
        if type(i) != int:
            print(i, "isn't integer")

    calkulator(operation, elements)
