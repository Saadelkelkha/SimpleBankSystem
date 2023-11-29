# SimpleBankSystem
The "SimpleBankSystem" is a Python program that simulates a basic banking system with two main roles: Bank Agent and Bank Customer. The program utilizes classes and methods to perform various banking operations, such as creating and deleting accounts, changing passwords, depositing and withdrawing money.


# Classes:

_Agent:

Attributes:

count: Class variable to keep track of the number of accounts.
Compte: Dictionary to store account balances with account numbers as keys.
Client: Dictionary to store customer passwords with customer numbers as keys.
ClientCompte: Dictionary to associate account numbers with customer numbers.
Methods:

GeneratorAccountNum: Generates a unique account number based on the current count.
GeneratorAccountMot: Generates a random account password.
AjouterCompte: Adds a new account with a specified balance and updates relevant dictionaries.
SupprimerCompte: Deletes an account and updates relevant dictionaries.
manipSTS: Performs some manipulation on the client account data (currently not fully implemented).


_client (inherits from Agent):

Attributes:

numcl: Customer number.
mpc: Customer password.
Methods:

Deposer: Allows the customer to deposit money into their account.
Retirer: Allows the customer to withdraw money from their account.
modifierMPClient: Modifies the customer's password.


#Main:


The main part of the program consists of a menu-driven interface that allows the user to choose between the Bank Agent and Bank Customer roles. Depending on the role, the user can perform actions like adding/deleting accounts, changing passwords, depositing, and withdrawing money.

Overall, the "SimpleBankSystem" program provides a basic framework for a simple banking system with functionality for account management and transactions.





