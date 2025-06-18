import random

# Woordenboek: Nederlands naar Spaans
woordenlijst = {
    "kat": "gato",
    "hond": "perro",
    "huis": "casa",
    "auto": "coche",
    "boek": "libro",
    "appel": "manzana",
    "water": "agua",
    "school": "escuela",
    "zon": "sol",
    "maan": "luna"
}

AANTAL_VRAGEN = 5  # Aantal quizvragen

def start_quiz():
    print("🎉 Welkom bij de Nederlandse-Spaanse Woordquiz! 🎉")
    print(f"Je krijgt {AANTAL_VRAGEN} Nederlandse woorden. Geef de juiste Spaanse vertaling.")
    print("Typ je antwoord en druk op Enter. Succes!\n")

    # Kies willekeurige woorden uit de woordenlijst
    vragen = random.sample(list(woordenlijst.items()), k=AANTAL_VRAGEN)
    score = 0

    for i, (nederlands, spaans) in enumerate(vragen, 1):
        print(f"Vraag {i}: Wat is het Spaanse woord voor '{nederlands}'?")
        antwoord = input("Jouw antwoord: ").strip().lower()

        if antwoord == spaans:
            print("✅ Goed gedaan!\n")
            score += 1
        else:
            print(f"❌ Helaas, het juiste antwoord was '{spaans}'.\n")

    print(f"De quiz is klaar! Je hebt {score} van de {AANTAL_VRAGEN} goed.")
    if score == AANTAL_VRAGEN:
        print("🏆 Fantastisch! Je beheerst deze woorden uitstekend!")
    elif score >= AANTAL_VRAGEN // 2:
        print("👍 Goed gedaan! Blijf oefenen.")
    else:
        print("📚 Blijf studeren! Oefening baart kunst.")

# Start het spel
if __name__ == "__main__":
    start_quiz()