const readline = require('readline');

// VARIABELEN (ALTIJD BENADERBAAR)
// Woordenlijst (vul aan tot 100 voor meer variatie)
const woordenlijst = [
    ["kat", "gato"],
    ["auto", "coche"],
    ["hond", "perro"],
    ["huis", "casa"],
    ["boek", "libro"],
    // ... meer woorden
];

let aantalVragen = 5; // default
let score = 0;

// FUNCTIES
function startQuiz() {
    console.log("🎉 Welkom bij de Nederlandse-Spaanse Woordquiz! ");
    console.log(`Je krijgt ${aantalVragen} Nederlandse woorden.`);
    console.log("");
    stelVraag(1);
}

function stelVraag(vraagNummer) {
    if (vraagNummer > aantalVragen) {
        console.log(`Quiz klaar! Je hebt ${score} van de ${aantalVragen} goed.`);
        return;
    }
    const nederlandsWoord = woordenlijst[vraagNummer - 1][0];
    const spaansWoord = woordenlijst[vraagNummer - 1][1];

    const rlStelVraag = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const vraag = `Vraag ${vraagNummer}: Wat is het Spaanse woord voor '${nederlandsWoord}'? `;
    rlStelVraag.question(vraag, (antwoord) => {
        if (antwoord && antwoord.trim() === spaansWoord) {
            console.log("✅ Goed gedaan!");
            score = score + 1;
        } else {
            console.log(`❌ Helaas, het juiste antwoord was '${spaansWoord}'.`);
        }
        console.log(`Score: ${score}`);
        console.log("");
        rlStelVraag.close();
        stelVraag(vraagNummer + 1);
    });
}

// UITVOERENDE CODE
// Vraag eerst het aantal vragen
const rlAantal = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rlAantal.question("Hoeveel vragen wil je? ", (input) => {
    const aantal = parseInt(input, 10);
    if (!isNaN(aantal) && aantal > 0 && aantal <= woordenlijst.length) {
        aantalVragen = aantal;
    } else {
        console.log(`Ongeldig aantal, standaardwaarde (${aantalVragen}) wordt gebruikt.`);
    }
    rlAantal.close();
    startQuiz();
});

