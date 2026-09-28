import json


def incarca_tranzactii():
    try:
        with open("tranzactii.json", "r") as fisier:
            return json.load(fisier)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salveaza_tranzactii(tranzactii):
    with open("tranzactii.json", "w") as fisier:
        json.dump(tranzactii, fisier, indent=4)


def cere_suma():
    while True:
        try:
            suma = float(input("Introdu suma: "))

            if suma <= 0:
                print("❌ Suma trebuie sa fie mai mare decat 0.")
                continue

        except ValueError:
            print("❌ Valoare invalida! Te rog sa introduci un numar valid.")

        else:
            return suma


def cere_descriere():
    while True:
        descriere = input("Introdu descrierea: ").strip()

        if descriere == "":
            print("❌ Descrierea nu poate fi goala!")
            continue

        return descriere


def cere_categorie():
    categorii = {
        "1": "Mancare",
        "2": "Transport",
        "3": "Jocuri",
        "4": "Haine",
        "5": "Altele"
    }

    while True:
        print("\n--- 📁 CATEGORIE ---")
        print("1. Mancare")
        print("2. Transport")
        print("3. Jocuri")
        print("4. Haine")
        print("5. Altele")

        alegere = input("👉 Alege categoria: ").strip()

        if alegere in categorii:
            return categorii[alegere]

        print("❌ Categorie invalida!")


tranzactii = incarca_tranzactii()


while True:
    print("\n--- 💰 EXPENSE TRACKER ---")
    print("1. Adauga venit")
    print("2. Adauga cheltuiala")
    print("3. Vezi tranzactiile")
    print("4. Vezi soldul")
    print("5. Statistici")
    print("6. Iesire")

    alegere = input("👉 Alege o optiune: ").strip()

    if alegere == "1":
        suma = cere_suma()
        descriere = cere_descriere()

        tranzactie = {
            "tip": "venit",
            "suma": suma,
            "descriere": descriere
        }

        tranzactii.append(tranzactie)
        salveaza_tranzactii(tranzactii)

        print("✅ Venitul a fost adaugat cu succes!")

    elif alegere == "2":
        suma = cere_suma()
        descriere = cere_descriere()
        categorie = cere_categorie()

        tranzactie = {
            "tip": "cheltuiala",
            "suma": suma,
            "descriere": descriere,
            "categorie": categorie
        }

        tranzactii.append(tranzactie)
        salveaza_tranzactii(tranzactii)

        print("✅ Cheltuiala a fost adaugata cu succes!")

    elif alegere == "3":
        if len(tranzactii) == 0:
            print("❌ Nu exista tranzactii inregistrate.")

        else:
            print("\n--- 📋 TRANZACTII ---")

            for tranzactie in tranzactii:
                if tranzactie["tip"] == "cheltuiala":
                    categorie = tranzactie.get(
                        "categorie",
                        "Fara categorie"
                    )

                    print(
                        f"Cheltuiala: {tranzactie['suma']:.2f} lei - "
                        f"{tranzactie['descriere']} [{categorie}]"
                    )

                else:
                    print(
                        f"Venit: {tranzactie['suma']:.2f} lei - "
                        f"{tranzactie['descriere']}"
                    )

    elif alegere == "4":
        sold = 0

        for tranzactie in tranzactii:
            if tranzactie["tip"] == "venit":
                sold += tranzactie["suma"]

            elif tranzactie["tip"] == "cheltuiala":
                sold -= tranzactie["suma"]

        print(f"💰 Soldul actual este: {sold:.2f} lei")

    elif alegere == "5":
        venituri = 0
        cheltuieli = 0
        cheltuieli_categorii = {}

        for tranzactie in tranzactii:
            if tranzactie["tip"] == "venit":
                venituri += tranzactie["suma"]

            elif tranzactie["tip"] == "cheltuiala":
                cheltuieli += tranzactie["suma"]

                categorie = tranzactie.get(
                    "categorie",
                    "Fara categorie"
                )

                if categorie in cheltuieli_categorii:
                    cheltuieli_categorii[categorie] += tranzactie["suma"]
                else:
                    cheltuieli_categorii[categorie] = tranzactie["suma"]

        sold = venituri - cheltuieli

        print("\n--- 📊 STATISTICI ---")
        print(f"🟢 Venituri totale: {venituri:.2f} lei")
        print(f"🔴 Cheltuieli totale: {cheltuieli:.2f} lei")
        print(f"💰 Sold: {sold:.2f} lei")

        if len(cheltuieli_categorii) > 0:
            print("\n--- 📁 CHELTUIELI PE CATEGORII ---")

            for categorie, suma in cheltuieli_categorii.items():
                print(f"{categorie}: {suma:.2f} lei")

    elif alegere == "6":
        print("👋 La revedere!")
        break

    else:
        print("❌ Optiune invalida! Alege un numar intre 1 si 6.")