import random
import csv

class Agent():
    # Class variables to keep track of counts and relationships between clients, accounts, and balances.
    count = 0
    Compte = {}
    Client = {}
    ClientCompte = {}

    # Creating a CSV file and writing headers if it doesn't exist.
    with open('CSVfile.csv', 'w') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(['NumCl', 'NumC', 'Mpc', 'Balance']) 

    def __init__(self):
        pass

    # Generates a unique account number combining the agent's count and a random number.
    def GeneratorAccountNum(self):
        return str(Agent.count) + str(random.randint(0, 100))
    
    # Generates a random account password.
    def GeneratorAccountMot(self):
        return str(random.randint(100000, 999999) )

    # Adds a new account with a unique account number, a corresponding client number, and a password.
    def AjouterCompte(self, Balance=0):
        Agent.count += 1
        numcl = Agent.count
        numc = self.GeneratorAccountNum()
        mpc = self.GeneratorAccountMot()
        Agent.Compte[numc] = Balance
        Agent.Client[numcl] = mpc
        Agent.ClientCompte[numc] = numcl
        print("The account was created with the customer number:", numcl, "and account number:", numc, "and the password:", mpc)
        # Appends the account details to the CSV file.
        with open('CSVfile.csv', 'a') as fd:
            csv_writer = csv.writer(fd)
            csv_writer.writerow([numcl, numc, mpc, Balance])

    # Removes an account based on the account number.
    def SupprimerCompte(self, numc):
        del Agent.Compte[numc]
        del Agent.Client[Agent.ClientCompte[numc]]
        del Agent.ClientCompte[numc]

    # Manipulates sets derived from client and account relationships.
    def manipSTS(self):
        numComptesListe = list(self.ClientCompte.values())
        numComptesTuple = tuple(self.ClientCompte.values())
        numComptesSet = set(self.ClientCompte.values())

class client(Agent):
    # Initializes a client with a client number and password.
    def __init__(self, numcl, mpc):
        self.numcl = numcl
        self.mpc = mpc

    # Deposits money into a specified account.
    def Deposer(self):
        arg = float(input("type number of money: "))
        numc = str(input("type number account: "))
        Agent.Compte[numc] += arg

    # Withdraws money from a specified account if there are sufficient funds.
    def Retirer(self):
        while True:
            arg = float(input("type number of money: "))
            numc = str(input("type number account: "))
            if Agent.Compte[numc] >= arg:
                Agent.Compte[numc] = Agent.Compte[numc] - arg
                break
            else:
                print("you don't have enough money")

    # Modifies the password of the client.
    def modifierMPClient(self, NMP):
        Agent.Client[self.numcl] = NMP

