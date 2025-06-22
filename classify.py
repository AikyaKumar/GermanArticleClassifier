# Hardcoded examples for German articles
article_dict = {
    "der": ["Hund", "Tisch", "Baum", "Stuhl", "Apfel", "Sessel", "Stuhle", "Tisch","Schribtisch", "Schrank",
            "Kleiderschrank", "Teppich", "Nachttisch", "Spiegel", "Hocker", "Vorhang", "Laptop", "Drucker",
            "Ventilator", "Haartrockner", "Standmixer", "Entsafter", "Fernseher", "Kühlschrank", "Ofen", 
            " Wasserspender", "Haarschneider", "Herd", "Stanbsauger", "Backofen", "Trockner", "Geschirrspüler", 
            "Toaster", "Wasserkocher"
            ],

    "die": ["Katze", "Blume", "Tasse", "Tasche", "Uhr", "Lampe", "Tischlampe", "Stehlampe", "Couch", "Kommode",
            "Vase", "Sitzbank", "Kamera", "Abzugshaube", "Waschmaschine", "Nähmaschine", 
            "Stereoanlage","Kaffeemaschine", "Mikrowelle", "Spülmaschine", "Toaster", "Geschirrspüler",],

    "das": ["Kind", "Auto", "Buch", "Haus", "Mädchen", "Möbel", "Sofa", "Bett", "Regal", "Bücherregal", 
            "Haushaltsgerät", "Fenster", "Bild", "Kissen", "Radio", "Handy", "Faxgerät", "Bügeleisen"]
}

def classify_article(noun):
    for article, nouns in article_dict.items():
        if noun in nouns:
            return article
    return "Unknown"  # If the noun is not in the dictionary

# Example usage
# test_nouns = ["Hund", "Katze", "Auto", "Tisch", "Uhr", "Buch", "Lampe"]

# for noun in test_nouns:
#     article = classify_article(noun)
#     print(f"{article} {noun}")