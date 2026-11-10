import pandas as pd

def analyser_sales(sales):

    # 1. Création du DataFrame
    df = pd.DataFrame({"montant": sales})

    # 2. Nettoyage : conserver uniquement les montants positifs
    df = df[df["montant"] > 0]

    # Vérification
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
sales = [150, 200, 300, 450, 500, -50, 0, 1200, 250]

analyser_sales(sales)