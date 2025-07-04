# Quiz App - Coding Wednesday

Een eenvoudige command-line quiz applicatie in Python, JavaScript en Java voor het leren van Nederlandse-Spaanse vertalingen.

## 📋 Inhoudsopgave

- [📖 Code Uitleg](#-code-uitleg)
  - [Python Versie](#python-versie)
  - [JavaScript Versie](#javascript-versie)
  - [Java Versie](#java-versie)
- [🎯 User Stories](#-user-stories)
  - [Level 1](#level-1)
  - [Level 2](#level-2)
- [🚀 Hoe te beginnen](#-hoe-te-beginnen)
- [💡 Tips](#-tips)


## Uitleg opdracht

Je krijgt wat basiscode voor een quiz applicatie. Dit kun je gebruiken om jouw applicatie mee uit te bouwen. Je mag de code aanpassen als dat nodig is.
Bij de User Stories staan ideeen voor meerdere features. Maar je mag ook je eigen features verzinnen.
Voor elke feature kan je punten krijgen. 

## 📖 Code Uitleg

Deze app is een quiz applicatie die Nederlandse woorden naar het Spaans laat vertalen. De gebruiker krijgt een Nederlands woord te zien en moet de Spaanse vertaling intypen. Aan het einde zie je hoeveel vragen je goed hebt van het totaal.


### Python Versie

#### Structuur
1. **Woordenlijst**: Een lijst met Nederlandse woorden en hun Spaanse vertalingen
2. **Instellingen**: Het aantal vragen dat gesteld wordt (momenteel 5)
3. **Loop**: Een `while` loop die door de vragen gaat
4. **Score**: Bijhouden van correcte antwoorden
5. **Feedback**: Directe feedback na elk antwoord

#### Belangrijke concepten
- **Lists**: `woordenlijst` bevat paren van woorden als nested lists
- **Loops**: `while` loop voor het herhalen van vragen
- **Variables**: `score` en `vraag_nummer` bijhouden
- **Conditionals**: `if/else` voor het controleren van antwoorden
- **Input/Output**: `input()` en `print()` voor gebruikersinteractie

#### Code voorbeelden
```python
# Woordenlijst als nested list
woordenlijst = [
    ["kat", "gato"],
    ["hond", "perro"],
    ["huis", "casa"],
]

# While loop met teller
while vraag_nummer <= AANTAL_VRAGEN:
    # Array toegang met index
    nederlands_woord = woordenlijst[vraag_nummer - 1][0]
    spaans_woord = woordenlijst[vraag_nummer - 1][1]
```

### JavaScript Versie

#### Structuur
1. **Woordenlijst**: Een array met Nederlandse woorden en hun Spaanse vertalingen
2. **Instellingen**: Het aantal vragen dat gesteld wordt (momenteel 5)
3. **Recursive Function**: Een recursieve functie die door de vragen gaat
4. **Score**: Bijhouden van correcte antwoorden
5. **Feedback**: Directe feedback na elk antwoord

#### Belangrijke concepten
- **Arrays**: `woordenlijst` bevat paren van woorden als nested arrays
- **Recursion**: `stelVraag()` functie roept zichzelf aan voor de volgende vraag
- **Variables**: `score` en `aantalVragen` bijhouden (camelCase)
- **Conditionals**: `if/else` voor het controleren van antwoorden
- **Input/Output**: `readline` module en `console.log()` voor gebruikersinteractie
- **Async Programming**: Proper handling van asynchrone readline calls

#### Code voorbeelden
```javascript
// Woordenlijst als nested array
const woordenlijst = [
    ["kat", "gato"],
    ["hond", "perro"],
    ["huis", "casa"],
];

// Recursive function voor vragen
function stelVraag(vraagNummer) {
    if (vraagNummer > aantalVragen) {
        // Base case: quiz klaar
        return;
    }
    // Recursive call voor volgende vraag
    stelVraag(vraagNummer + 1);
}
```

### Java Versie

#### Structuur
1. **Woordenlijst**: Een 2D array met Nederlandse woorden en hun Spaanse vertalingen
2. **Instellingen**: Het aantal vragen dat gesteld wordt (aanpasbaar via input)
3. **Recursive Function**: Een recursieve functie die door de vragen gaat
4. **Score**: Bijhouden van correcte antwoorden
5. **Feedback**: Directe feedback na elk antwoord

#### Belangrijke concepten
- **2D Arrays**: `woordenlijst` bevat paren van woorden als String[][]
- **Recursion**: `stelVraag()` methode roept zichzelf aan voor de volgende vraag
- **Static Variables**: `score` en `aantalVragen` als static class variables
- **Conditionals**: `if/else` voor het controleren van antwoorden
- **Input/Output**: `Scanner` class en `System.out.println()` voor gebruikersinteractie
- **Exception Handling**: Try-catch voor input validation

#### Code voorbeelden
```java
// Woordenlijst als 2D array
private static final String[][] woordenlijst = {
    {"kat", "gato"},
    {"hond", "perro"},
    {"huis", "casa"},
};

// Recursive method voor vragen
public static void stelVraag(int vraagNummer) {
    if (vraagNummer > aantalVragen) {
        // Base case: quiz klaar
        return;
    }
    // Recursive call voor volgende vraag
    stelVraag(vraagNummer + 1);
}
```

## 🎯 User Stories
User stories zijn korte, eenvoudige beschrijvingen van een functionaliteit vanuit het perspectief van een gebruiker. Ze volgen meestal dit format:

**Als** [type gebruiker]  
**Dan** [wat ze willen doen]  
**Zodat** [waarom/wat het oplevert]

### Level 1 

#### 1. Aanpasbaar aantal vragen (5 punten)
**Als** een gebruiker de quiz speelt  
**Dan** wil ik het aantal vragen kunnen aangeven  
**Zodat** ik kortere of langere quizzes kan maken

**Implementatie**: Maak `AANTAL_VRAGEN` aanpasbaar via input


#### 2. Score percentage tonen (3 punten)
**Als** een gebruiker de quiz afrondt  
**Dan** wil ik het percentage correcte antwoorden zien  
**Zodat** ik mijn prestaties beter kan beoordelen

**Implementatie**: Bereken en toon percentage naast de score

#### 3. Hints toevoegen (10 punten)
**Als** een gebruiker een vraag krijgt  
**Dan** wil ik een hint kunnen krijgen  
**Zodat** ik het antwoord makkelijker kan raden

**Implementatie**: Voeg een hint systeem toe

### Level 2

#### 1. Omkeerbare quiz (Spaans → Nederlands) (25 punten)
**Als** een gebruiker de quiz speelt  
**Dan** wil ik in een menu kunnen kiezen tussen Nederlands→Spaans of Spaans→Nederlands  
**Zodat** ik de taal beide kanten op kan oefenen

**Implementatie**: Menu systeem met keuze voor richting


#### 2. Tijdsdruk toevoegen (30 punten)
**Als** een gebruiker de quiz speelt  
**Dan** wil ik een tijdslimiet per vraag  
**Zodat** de quiz uitdagender wordt

**Implementatie**: Timer systeem met countdown



### Werk je eigen user story uit! (1 tot 100 punten)
Bedenk wat je wil bouwen en schrijf het uit in een user story
**Als** ...
**Dan** ...
**Zodat** ...

**Implementatie** ...

## 🚀 Hoe te beginnen

1. **Begrijp de code**: Lees door de bestaande code en begrijp hoe het werkt
2. **Kies een user story**: Start met een Level 1 opdracht
3. **Plan je aanpak**: Schrijf op wat je wilt veranderen
4. **Test je code**: Zorg dat alles nog steeds werkt
5. **Itereer**: Voeg steeds meer functionaliteit toe

### Hoe te runnen

#### Python
```bash
python quiz.py
```

#### JavaScript
```bash
node quiz.js
```

#### Java
```bash
javac Quiz.java
java Quiz
```

## 💡 Tips

- **Begin klein**: Maak kleine aanpassingen en test vaak
- **Backup**: Bewaar een werkende versie voordat je grote wijzigingen maakt
- **Commentaar**: Schrijf commentaar bij je nieuwe code
- **Variabelen**: Gebruik duidelijke namen voor nieuwe variabelen
- **Foutafhandeling**: Denk na over wat er mis kan gaan

Veel succes met het uitbreiden van de quiz! 🎉
# cw-quiz-game
