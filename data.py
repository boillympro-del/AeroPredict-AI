import sqlite3


# créer
def create_database():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute(
        # Crée la table uniquement si elle n'existe pas déjà.
        "CREATE TABLE IF NOT EXISTS machines ("
        # Définit l'identifiant de la machine comme texte et Définit les ID en double.
        "identifiant TEXT PRIMARY KEY,"
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
    curseur = connexion.cursor()
    # prends le stylo pour écrire dedans. En base de données, on écrit toujours avec le curseur.
    validation = True
    try:
        curseur.execute(
            "INSERT INTO machines (identifiant, temperature, vitesse) "  # Choisit les colonnes à remplir.
            # Insère les trois valeurs dans l'ordre des colonnes.
            "VALUES (?, ?, ?)",
            (machine.identifiant, machine.temperature, machine.speed),
        )  # valeur qui sera remplacée par les valeurs de la machine.
        validation = True
        connexion.commit()  # enregistres
    except sqlite3.IntegrityError:
        validation = False

    connexion.close()  # refermes le cahier
    return validation


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


def recuperer_machine(identifiant):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    # Cherche une seule machine grâce à son identifiant.
    curseur.execute("SELECT * FROM machines WHERE identifiant = ?", (identifiant,))
    machine = curseur.fetchone()  # None si la machine n'existe pas
    connexion.close()
    return machine


def supprimer_machine(identifiant):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM MACHINES WHERE identifiant = ?", (identifiant,))
    lignes=curseur.rowcount
    connexion.commit()
    connexion.close()    
    if lignes > 0: 
        return True
    else:
        return False
    

def modifier_machine(identifiant, temperature, vitesse):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute(
        "UPDATE machines SET temperature = ?, vitesse = ? WHERE identifiant = ?",
        (temperature, vitesse, identifiant),
    )
    lignes2=curseur.rowcount
    connexion.commit()
    connexion.close()
    if lignes2>0:
        return True
    else:
        return False


def alerte_temperature(temperature):
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM MACHINES WHERE temperature> ?", (temperature,))
    machines_alertes_temperatures = curseur.fetchall()
    connexion.close()
    return machines_alertes_temperatures


def count_machines():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT COUNT (*) FROM MACHINES")
    machines_total = curseur.fetchall()
    connexion.close()
    return machines_total
def avg_machines():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT ROUND(AVG(temperature), 2), ROUND(AVG(vitesse), 2) FROM MACHINES")
    machines_total = curseur.fetchall()
    connexion.close()
    return machines_total

def max_machines():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT MAX(temperature), MAX(vitesse) FROM MACHINES")
    machines_total = curseur.fetchall()
    connexion.close()
    return machines_total

def min_machines():
    connexion = sqlite3.connect("database.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT MIN(temperature), MIN(vitesse) FROM MACHINES")
    machines_total = curseur.fetchall()
    connexion.close()
    return machines_total