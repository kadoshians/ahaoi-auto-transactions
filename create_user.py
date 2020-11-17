
import random
import json

FIRST_NAMES = ["Heike ", "Lucy ", "Ella ", "Finja ", "Amelie " , "Katharina ", "Romy ", "Juna ", "Lukas ", "David Klaus", "Oskar ", "Philipp ", "Leon ", "Noah ", "Alex"]
SURENAMES = ["Specht", "Albrecht", "Heinz", "Strauss", "Winter", "Bauer", "Fuchs", "Mayer", "Brecht", "Stark", "Frisch", "Schiller", "Klump", "Bader"]


def gen_names():
    names = list()
    for x in range(0, 10):
        name = FIRST_NAMES[random.randint(0,10)] + SURENAMES[random.randint(0,10)]
        names.append(name)
    return names


def gen_ibans():
    ibans = list()
    for x in range(0, 10):
        iban = ""
        for i in range(0, 20):
           iban += str(random.randint(0, 9))
        iban = "DE" + iban
        ibans.append(iban)
    return ibans


def gen_amounts():
    amounts = list()
    for x in range(0, 10):
        amount = ""
        for i in range(0, 4):
            if i == 2:
                amount += ","
            amount += str(random.randint(0, 3))
        amounts.append(amount)
    return amounts


if __name__ == '__main__':
    data = {}
    data["data"] = []

    names = gen_names()
    ibans = gen_ibans()
    amounts = gen_amounts()

    data["data"].append(
        {
            "name" : names,
            "iban" : ibans,
            "amounts" : amounts
        }
    )

    with open("user.json", "w") as json_file:
        json.dump(data, json_file)
