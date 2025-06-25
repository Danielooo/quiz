import random

# Woordenlijst
woordenlijst = [
    ["kat", "gato"],
    ["hond", "perro"],
    ["huis", "casa"],
    ["auto", "coche"],
    ["boek", "libro"],
]

AANTAL_VRAGEN = 5  # Aantal quizvragen

# Welkomstbericht
print("🎉 Welkom bij de Nederlandse-Spaanse Woordquiz! 🎉")
print(f"Je krijgt {AANTAL_VRAGEN} Nederlandse woorden.")
print("")

# Begin met score 0
score = 0
vraag_nummer = 1

# Stel alle vragen
while vraag_nummer <= AANTAL_VRAGEN:
    # Haal het huidige woord op
    nederlands_woord = woordenlijst[vraag_nummer - 1][0]
    spaans_woord = woordenlijst[vraag_nummer - 1][1]

    # Stel de vraag
    print(f"Vraag {vraag_nummer}: Wat is het Spaanse woord voor '{nederlands_woord}'?")
    antwoord = input("Jouw antwoord: ").strip()

    # Controleer antwoord
    if antwoord == spaans_woord:
        print("✅ Goed gedaan!")
        score = score + 1
    else:
        print(f"❌ Helaas, het juiste antwoord was '{spaans_woord}'.")
    
    print(f"Score: {score}")
    print("")
    
    # Ga naar volgende vraag
    vraag_nummer = vraag_nummer + 1

# Toon eindresultaat
print(f"Quiz klaar! Je hebt {score} van de {AANTAL_VRAGEN} goed.")