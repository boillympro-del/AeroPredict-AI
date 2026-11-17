import sqlite3


# créer
def create_database():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute(
        # Crée la table uniquement si elle n'existe pas déjà.
        "CREATE TABLE IF NOT EXISTS machines ("
        # Définit l'identifiant de la machine comme texte.
        "identifiant TEXT,"
        # Définit la température de la machine comme nombre entier.
        "temperature INTEGER,"
        # Définit la vitesse de la machine comme nombre entier.
        "vitesse INTEGER"
        # Termine la définition de la table.
        ")"
    )
    connexion.commit()
    connexion.close()


# enregistrer dans la base de données
def ajouter_machine(machine):
    connexion = sqlite3.connect(
        "database.db"
    )  # tu ouvres le cahier. S’il n’existe pas, il est créé
    curseur = connexion.cursor()  # prends le stylo pour écrire dedans. En base de données, on écrit toujours avec le curseur.
    curseur.execute(
        # Choisit les colonnes à remplir.
        "INSERT INTO machines (identifiant, temperature, vitesse) "
        # Insère les trois valeurs dans l'ordre des colonnes.
        "VALUES (?, ?, ?)",  # valeur qui sera remplacée par les valeurs de la machine.
        (machine.identifiant, machine.temperature, machine.speed),
    )
    connexion.commit()  # enregistres
    connexion.close()  # refermes le cahier


def afficher_machines():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    # Sélectionne toutes les colonnes de la table « machines ».
    curseur.execute("SELECT * FROM machines")
    machines_data = (
        curseur.fetchall()
    )  # Récupère toutes les machines trouvées et les stocke dans une liste.
    connexion.close()
    return machines_data

def supprimer_machine(identifiant):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM MACHINES WHERE identifiant = ?", (identifiant,))
    connexion.commit()
    connexion.close()

def modifier_machine(identifiant, temperature, vitesse):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE machines SET temperature = ?, vitesse = ? WHERE identifiant = ?", (temperature, vitesse, identifiant))
    connexion.commit()
    connexion.close()