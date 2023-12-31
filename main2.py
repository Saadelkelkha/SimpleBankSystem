from classes import Agent, client

# Creating an instance of the Agent class
agent = Agent()

# Main menu loop
while True:
    print("Main Menu:")
    print("1. Bank officer")
    print("2. Bank customer")
    print("3. To leave")
    
    choixp = input("Choose an option (1/2/3): ")

    # Bank officer menu
    if choixp == '1':
        while True:
            print("Bank Agent Menu:")
            print("1. Add an account")
            print("2. Delete an account")
            print("3. Back")

            choixag = input("Choose an option (1/2/3): ")

            if choixag == '1':
                agent.AjouterCompte()

            elif choixag == '2':
                numc_supprimer = input("Account number to delete: ")
                agent.SupprimerCompte(numc_supprimer)
                print("Account deleted successfully.")

            elif choixag == '3':
                break

            else:
                print("Invalid choice. Please choose a valid option.")

    # Bank customer menu
    elif choixp == '2':
        while True:
            print("Bank Customer Menu:")
            print("1. Change the password")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Back")

            choixc = input("Choose an option (1/2/3/4): ")

            if choixc == '1':
                while True:
                    numcl = int(input("Type customer number: "))
                    mpc = str(input("Type new password: "))
                    client1 = client(numcl, mpc)
                    if (numcl in Agent.Client) and (Agent.Client[numcl] == mpc):
                        break
                    else:
                        print("Account is not defined")
                
                nmp = str(input("Type new password: "))
                client1.modifierMPClient(nmp)

            elif choixc == '2':
                while True:
                    numcl = int(input("Type customer number: "))
                    mpc = str(input("Type password: "))
                    client1 = client(numcl, mpc)
                    if (numcl in Agent.Client) and (Agent.Client[numcl] == mpc):
                        break
                    else:
                        print("Account is not defined")
                client1.Deposer()
                print("Deposit successfully completed.")

            elif choixc == '3':
                while True:
                    numcl = int(input("Type customer number: "))
                    mpc = str(input("Type password: "))
                    client1 = client(numcl, mpc)
                    if (numcl in Agent.Client) and (Agent.Client[numcl] == mpc):
                        break
                    else:
                        print("Account is not defined")
                client1.Retirer()
                print("Withdrawal completed successfully.")

            elif choixc == '4':
                break

            else:
                print("Invalid choice. Please choose a valid option.")

    # Exiting the program
    elif choixp == '3':
        print("Bye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")

