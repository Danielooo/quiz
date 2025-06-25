import java.util.Scanner;

public class Quiz {
    // VARIABELEN (ALTIJD BENADERBAAR)
    // Woordenlijst (vul aan tot 100 voor meer variatie)
    private static final String[][] woordenlijst = {
        {"kat", "gato"},
        {"auto", "coche"},
        {"hond", "perro"},
        {"huis", "casa"},
        {"boek", "libro"},
        // ... meer woorden
    };
    
    private static int aantalVragen = 5; // default
    private static int score = 0;
    private static Scanner scanner = new Scanner(System.in);
    
    // FUNCTIES
    public static void startQuiz() {
        System.out.println("🎉 Welkom bij de Nederlandse-Spaanse Woordquiz! ");
        System.out.println("Je krijgt " + aantalVragen + " Nederlandse woorden.");
        System.out.println();
        stelVraag(1);
    }
    
    public static void stelVraag(int vraagNummer) {
        if (vraagNummer > aantalVragen) {
            System.out.println("Quiz klaar! Je hebt " + score + " van de " + aantalVragen + " goed.");
            scanner.close();
            return;
        }
        
        String nederlandsWoord = woordenlijst[vraagNummer - 1][0];
        String spaansWoord = woordenlijst[vraagNummer - 1][1];
        
        System.out.print("Vraag " + vraagNummer + ": Wat is het Spaanse woord voor '" + nederlandsWoord + "'? ");
        String antwoord = scanner.nextLine().trim();
        
        if (antwoord.equals(spaansWoord)) {
            System.out.println("✅ Goed gedaan!");
            score = score + 1;
        } else {
            System.out.println("❌ Helaas, het juiste antwoord was '" + spaansWoord + "'.");
        }
        
        System.out.println("Score: " + score);
        System.out.println();
        
        stelVraag(vraagNummer + 1);
    }
    
    public static void main(String[] args) {
        // UITVOERENDE CODE
        // Vraag eerst het aantal vragen
        System.out.print("Hoeveel vragen wil je? ");
        String input = scanner.nextLine();
        
        try {
            int aantal = Integer.parseInt(input);
            if (aantal > 0 && aantal <= woordenlijst.length) {
                aantalVragen = aantal;
            } else {
                System.out.println("Ongeldig aantal, standaardwaarde (" + aantalVragen + ") wordt gebruikt.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Ongeldig aantal, standaardwaarde (" + aantalVragen + ") wordt gebruikt.");
        }
        
        startQuiz();
    }
} 