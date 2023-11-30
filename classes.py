import random
import csv
class Agent() :
    count = 0
    Compte = {}
    Client = {}
    ClientCompte = {}

    with open('CSVfile.csv', 'w') as fd :
        csv_writer = csv.writer(fd)
        csv_writer.writerow(['NumCl', 'NumC', 'Mpc', 'Balance']) 

    def __init__(self):
        pass

    def GeneratorAccountNum(self) :
        return str(Agent.count) + str(random.randint(0, 100))
    
    def GeneratorAccountMot(self) :
        return str(random.randint(100000,999999) )

    def AjouterCompte(self, Balance = 0):
        Agent.count += 1
        numcl = Agent.count
        numc = self.GeneratorAccountNum()
        mpc = self.GeneratorAccountMot()
        Agent.Compte[numc] = Balance
        Agent.Client[numcl] = mpc
        Agent.ClientCompte[numc] = numcl
        print("The account was created with the customer number: ", numcl ," and account number: ",numc," and the password: ",mpc)
        with open('CSVfile.csv', 'w') as fd :
            csv_writer = csv.writer(fd)
            csv_writer.writerows([Agent.Compte, Agent.Client, Agent.ClientCompte])

    def SupprimerCompte(self,numc):
        del Agent.Compte[numc]
        del Agent.Client[Agent.ClientCompte[numc]]
        del Agent.ClientCompte[numc]

    def manipSTS(self):
        numComptesListe = list(self.ClientCompte.values())
        numComptesTuple = tuple(self.ClientCompte.values())
        numComptesSet = set(self.ClientCompte.values())

class client(Agent) :
    def __init__(self, numcl, mpc):
        self.numcl = numcl
        self.mpc = mpc

    def Deposer(self) :
        arg = float(input("type number of money : "))
        numc = str(input("type number account : "))
        Agent.Compte[numc] += arg

    def Retirer(self) :
        while True :
            arg = float(input("type number of money : "))
            numc = str(input("type number account : "))
            if Agent.Compte[numc] >= arg :
                Agent.Compte[numc] = Agent.Compte[numc] - arg
                break
            else :
                print("you don't have enough money              ")
    
    def modifierMPClient(self, NMP):
        Agent.Client[self.numcl] = NMP
