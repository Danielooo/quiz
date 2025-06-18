import random

# Dictionary of English to Spanish words
word_bank = {
    "cat": "gato",
    "dog": "perro",
    "house": "casa",
    "car": "coche",
    "book": "libro",
    "apple": "manzana",
    "water": "agua",
    "school": "escuela",
    "sun": "sol",
    "moon": "luna"
}

NUM_QUESTIONS = 5  # Number of quiz questions

def run_quiz():
    print("🎉 Welcome to the Spanish Vocabulary Quiz! 🎉")
    print(f"You will be asked to translate {NUM_QUESTIONS} English words into Spanish.")
    print("Type your answer and press Enter. Good luck!\n")

    # Randomly select words for the quiz
    words = random.sample(list(word_bank.items()), k=NUM_QUESTIONS)
    score = 0

    for i, (english, spanish) in enumerate(words, 1):
        print(f"Question {i}: What is the Spanish word for '{english}'?")
        answer = input("Your answer: ").strip().lower()

        if answer == spanish:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was '{spanish}'.\n")

    print(f"Quiz complete! You got {score} out of {NUM_QUESTIONS} correct.")
    if score == NUM_QUESTIONS:
        print("🏆 Excellent! You're a Spanish master!")
    elif score >= NUM_QUESTIONS // 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📚 Keep studying! Practice makes perfect.")

if __name__ == "__main__":
    run_quiz()