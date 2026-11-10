


import pandas as pd

# 1. Charger les données depuis le fichier CSV
sales = pd.read_csv("data/sales.csv")


def analyser_sales(df):

    # 2. Nettoyage : conserver les montants positifs
    df = df[df["montant"] > 0].copy()

    if df.empty:
        return "Aucune transaction valide"

    # 3. Calculs statistiques
    nombre = df["montant"].count()
    total = df["montant"].sum()
    moyenne = df["montant"].mean()
    mediane = df["montant"].median()
    ecart_type = df["montant"].std(ddof=0)
    maximum = df["montant"].max()
    minimum = df["montant"].min()

    # 4. Détection des anomalies
    anomalies = df[df["montant"] > 2 * moyenne]

    # 5. Affichage des résultats
    print("Nombre de transactions :", nombre)
    print("Somme totale :", total, "€")
    print("Moyenne :", round(moyenne, 2), "€")
    print("Médiane :", mediane, "€")
    print("Écart-type :", round(ecart_type, 2))
    print("Maximum :", maximum, "€")
    print("Minimum :", minimum, "€")

    print("\nAnomalies détectées :")
    print(anomalies)


# 6. Exécuter la fonction
analyser_sales(sales)

# modification code test