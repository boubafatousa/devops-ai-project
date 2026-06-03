from collections import Counter

def analyse_logs():
    try:
        with open("app.log", "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        print("❌ Aucun fichier de log trouvé")
        return

    erreurs = []

    for log in logs:
        if log.startswith("ERROR"):
            erreurs.append(log.strip())

    print("🔍 Analyse intelligente des logs\n")

    print(f"📊 Nombre total de logs : {len(logs)}")
    print(f"⚠️ Nombre d'erreurs détectées : {len(erreurs)}\n")

    if erreurs:
        compteur = Counter(erreurs)

        print("📌 Types d'erreurs détectées :")
        for erreur, count in compteur.items():
            print(f"- {erreur} (x{count})")

        print("\n💡 Suggestions automatiques :")

        for erreur in compteur:
            if "division by zero" in erreur:
                print("- Vérifier les calculs pour éviter une division par zéro")
            else:
                print("- Anomalie à analyser")

    else:
        print("✅ Aucun problème détecté")

analyse_logs()

