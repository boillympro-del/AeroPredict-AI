import data

data.create_database()  # Le tableau SQL est crée une seul fois.

# Constante
SEUIL_VALIDE_TEMPERATURE = 80
SEUIL_VALIDE_SPEED = 1500
MARGE_SPEED = 150
TEMPERATURE_MAX = 150
TEMPERATURE_MIN = 0
SPEED_MAX = 3600
SPEED_MIN = 0
FULL_CALCUL_SPEED_LOW = SEUIL_VALIDE_SPEED - MARGE_SPEED
FULL_CALCUL_SPEED_HIGH = SEUIL_VALIDE_SPEED + MARGE_SPEED


class Machine:
    # Permet de créer une machine et récupere les données sans etre redemander a chaque fois.
    def __init__(self, identifiant, temperature, vitesse):
        self.identifiant = identifiant
        self.temperature = temperature
        self.speed = vitesse

    def presentation(self):

        print(f"Machine: {self.identifiant}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Speed: {self.speed}tr/min")

    def verification_temperature(self):
        print("Wait, verification on your machine for its temperature.\n\n")
        if self.temperature <= SEUIL_VALIDE_TEMPERATURE:
            print("Your temperature is safe.")
        else:
            print("\nBe careful, your MACHINE is not safe, you must turn it off now.")

    def verification_speed(self):
        print("Wait, verification on your machine for its speed.\n\n")
        if self.speed < FULL_CALCUL_SPEED_LOW:
            print("Your speed is too low, you must increase it.\n")
        elif self.speed > FULL_CALCUL_SPEED_HIGH:
            print("Your speed is too high, you must decrease it.\n")
        else:
            print("Your speed is safe.\n")


machines = []

# Lit les machines depuis la base au démarrage et recrée les objets
for ligne in data.afficher_machines():
    identifiant = ligne[0]
    temperature = ligne[1]
    vitesse = ligne[2]
    machine = Machine(identifiant, temperature, vitesse)
    machines.append(machine)


while True:
    print("""
    ========== AEROPREDICT AI ==========
    1. Add a machine
    2. Show all machines
    3. Search a machine
    4. Alerts
    5. Modify a machine
    6. Delete a machine
    7. Exit

    Choose an option:

    """)
    while True:
        try:
            user = int(input("\nYour choice: "))
            if user < 1 or user > 7:
                print("Please enter a number between 1 and 7.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if user == 1:
        while True:
            try:
                nombres = int(input("\nHow many machines you want to register ? "))
                if nombres < 1:
                    print("Please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        for i in range(nombres):
            print(f"\n---Machine {i + 1}---")

            while True:
                try:
                    identifiant = input("Identifiant: ")
                    if identifiant == "":
                        print("Please enter a valid identifiant.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid identifiant.")

            while True:
                try:
                    temperature = int(input("Temperature: "))
                    if temperature < TEMPERATURE_MIN or temperature > TEMPERATURE_MAX:
                        print(
                            f"Please enter a temperature between {TEMPERATURE_MIN} and {TEMPERATURE_MAX}."
                        )
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid temperature.")

            while True:
                try:
                    speed = int(input("Speed: "))
                    if speed < SPEED_MIN or speed > SPEED_MAX:
                        print(
                            f"Please enter a speed between {SPEED_MIN} and {SPEED_MAX}."
                        )
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid speed.")

            machine = Machine(identifiant, temperature, speed)
            machines.append(machine)
            data.ajouter_machine(machine)

        for machine in machines:
            print("\n===========================")
            machine.presentation()
            print("\nMachine registered successfully.")

    elif user == 2:
        if len(machines) == 0:
            print("\nNo machines registered.")
        else:
            for machine in machines:
                print("===============\n=")
                machine.presentation()

    elif user == 3:
        trouver = False
        while True:
            try:
                print([machine.identifiant for machine in machines])
                user_position = input("\nID of your machine: #")
                for machine in machines:
                    if user_position == machine.identifiant:
                        machine.presentation()
                        trouver = True
                        break
                if trouver == False:
                    print("\nInvalid ID.")
                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif user == 4:
        alerte_fined = False
        for machine in machines:
            if (
                machine.temperature > SEUIL_VALIDE_TEMPERATURE
                or machine.speed < FULL_CALCUL_SPEED_LOW
                or machine.speed > FULL_CALCUL_SPEED_HIGH
            ):
                alerte_fined = True
                print("\n⚠️Urgent Urgent, Alert, Alert, Alert ⚠️")
                machine.presentation()
                machine.verification_temperature()
                machine.verification_speed()
        if alerte_fined == False:
            print("\nZero Alert, everything it's good... :)")

    elif user == 5:
        user_position = input("\nID of your machine to modify: #")
        for machine in machines:
            if user_position == machine.identifiant:
                while True:
                    try:
                        new_temperature = int(input("New Temperature: "))
                        if (
                            new_temperature < TEMPERATURE_MIN
                            or new_temperature > TEMPERATURE_MAX
                        ):
                            print(
                                f"Please enter a temperature between {TEMPERATURE_MIN} and {TEMPERATURE_MAX}."
                            )
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid temperature.")

                while True:
                    try:
                        new_speed = int(input("New Speed: "))
                        if new_speed < SPEED_MIN or new_speed > SPEED_MAX:
                            print(
                                f"Please enter a speed between {SPEED_MIN} and {SPEED_MAX}."
                            )
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid speed.")

                machine.temperature = new_temperature
                machine.speed = new_speed
                data.modifier_machine(machine.identifiant, new_temperature, new_speed)
                print("\nMachine modified successfully.")
                break
        else:
            print("\nInvalid ID.")
    elif user == 6:
        user_position2 = input("\nID of your machine to delete: #")
        for machine in machines:
            if user_position2 == machine.identifiant:
                data.supprimer_machine(user_position2)
                machines.remove(machine)
                print("\nMachine deleted successfully.")
                break
        else:
            print("\nInvalid ID.")

    elif user == 7:
        print("\nThank you for using AeroPredict AI. Goodbye!")
        break
