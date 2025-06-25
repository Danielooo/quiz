const readline = require('readline');

// Woordenlijst
const woordenlijst = [
    ["kat", "gato"],
    ["hond", "perro"],
    ["huis", "casa"],
    ["auto", "coche"],
    ["boek", "libro"],
];

// Instellingen
const AANTAL_VRAGEN = 5;

// Welkomstbericht
console.log("🎉 Welkom bij de Nederlandse-Spaanse Woordquiz! ");
console.log(`Je krijgt ${AANTAL_VRAGEN} Nederlandse woorden.`);
console.log("");

// Begin met score 0
let score = 0;

// Recursieve functie om vragen te stellen
function stelVraag(vraagNummer) {
    // Check if we've asked all questions
    if (vraagNummer > AANTAL_VRAGEN) {
        // Toon eindresultaat
        console.log(`Quiz klaar! Je hebt ${score} van de ${AANTAL_VRAGEN} goed.`);
        return;
    }

    // Haal het huidige woord op
    const nederlandsWoord = woordenlijst[vraagNummer - 1][0];
    const spaansWoord = woordenlijst[vraagNummer - 1][1];

    // Stel de vraag
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    const vraag = `Vraag ${vraagNummer}: Wat is het Spaanse woord voor '${nederlandsWoord}'? `;
    rl.question(vraag, (antwoord) => {
        rl.close();
        
        // Controleer antwoord
        if (antwoord && antwoord.trim() === spaansWoord) {
            console.log("✅ Goed gedaan!");
            score = score + 1;
        } else {
            console.log(`❌ Helaas, het juiste antwoord was '${spaansWoord}'.`);
        }
        
        console.log(`Score: ${score}`);
        console.log("");
        
        // Ga naar de volgende vraag door de functie opnieuw aan te roepen
        stelVraag(vraagNummer + 1);
    });
}

// Start the quiz met de eerste vraag
stelVraag(1);