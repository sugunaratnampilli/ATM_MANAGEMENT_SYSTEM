import random
from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def transaction(self):
        pass

#BASE CLASS
class Account():
    def __init__(self):
        self.holder_name=" "                                  #PUBLIC VARIABLE
        self._account_number=" "                            #PROTECTED VARIABLE
        self.__acbalance=" "                                  #PRIVATE VARIABLE
        self.count=" "
        self.Tr_history=[]  
    def set_data(self):
       while True:
        self.holder_name=input("Enter your Name:")
        self.age=int(input("Enter Your age:"))
        #CHECKS THE CONDITION AGE<18 IT IS NOT POSSIBLE TO ACCOUNT CREATION
        if self.age<18:                                       
            print("\nSorry..!You are not able to create a bank account...!")
            print("\tBecause you are minor.!")
            print("Try again..! Create an account with valid age..!\n")
            print("_________________________________________________________\n")
        #WHEN THE CONDITION(AGE<18) FALSE THE ACCOUNT CREATION PROCESS STARTED
        else:                                                
           #RANDOM(MODULE).RANDINT(ATTRIBUTE) GENERATES A RANDOM ACCOUNT NUMBER 
            self._account_number=int(random.randint(100000000,1000000000))             
            print("Account Number of the user:",self._account_number)
            print("ACCOUNT CREATED SUCCESSFULLY..!\n")
            self.__acbalance=int(0)
            self.count=int(0)            #ACCOUNT BALANCE IS INITIALLY HAVING O 
            break
        
    def get_balance(self):             #THIS METHOD RETURNS THE ACCOUNT BALANCE
        return self.__acbalance
    def set_balance(self,s):  
        self.__acbalance=s
    def acc_details(self):                     
    #THE ACC-DETAILS(SELF) METHOD DISPLAYS THE NAME,ACC_NUMBER AND AGE
        print("Account holder name:",self.holder_name)
        print("Age:",self.age)
        print("Account Number:",self._account_number)
    def pin_creation(self):                                                
  #AFTER ACCOUNT CREATION THE PIN CREATION METHOD IS GENERATED FOR SECURITY 
        print("|-------------------------------------------------------------|")
        print("|                        PIN CREATION:                        |")
        print("|-------------------------------------------------------------|\n")
        while True:
         acc_number=int(input("Please Enter your account number:"))
         if acc_number==self._account_number:
           self.__pin=input("Please set a pin for your account:")
           print("\n")
           break
         else:
            print("\nInvalid account number...!\n")
            print("Please enter the correct account number...!\n")
#THE SET_PIN AND GET_PIN METHODS ARE USED FOR ACCESSING THE PRIVATE VARIABLE=PIN
    def set_pin(self,p):                                    
       self.__pin=p
    def get_pin(self):
       return self.__pin
    def pin_verification(self):
       print("|---------------------------------------------------------------|")
       print("|                       PIN VERIFICATION:                       |")
       print("|---------------------------------------------------------------|\n")
       while True:
        acc_number=int(input("Enter the account number:"))
        if acc_number==self._account_number:
          s=input("Enter your pin:")
          if s==self.__pin:
             break
          else:
             print("\nInvalid pin/account number...!\nPlease Try again ....!\n")
        else:
             print("\nInvalid account number...!\nPlease Try again ....!\n")
             
#DERIVED CLASS(INHERITANCE{ACCOUNT}+ABSTRACTION{BANK_ACCOUNT})  
class Atm(Account,BankAccount):                                     
   #THE ATM CLASS STORES SOME INSTANCE METHODS,CLASS METHOD AND STATIC METHOD 
    bank="SBI BANK"
    def transaction(self):                                     #INSTANCE METHOD
        print("\t\tATM TRANSACTION STARTED...........!!\n") 
    def check_balance(self):                                  #INSTANCE METHOD
        print("The Balance is ₹",self.get_balance())
        print("\n")
    def deposit(self):                                         #INSTANCE METHOD
        while True:
         amount = int(input("How much amount you want to deposit/credited..? ₹"))
         if amount>0:   #CHECKING THE CONDITION AMOUNT>0 THEN DEPOSIT THE AMOUT
          current_balance = self.get_balance()
          new_balance = current_balance + amount
          self.set_balance(int(new_balance))
          print("After depositing, The account Balance is ₹",new_balance)
          print("\n\t\tTHE AMOUNT IS DEPOSITED SUCCESSFULLY..........!")
          print("\n")
          status='₹',amount,'credited.'
          self.Tr_history.append(status)
          self.count+=1
          break
         else:                                                        
        #IF THE AMOUNT IS LESS THAN 0 OR EQUAL TO 0 THE DEPOSIT METHOD AGAIN RUN
          print("\t\tEnter the valid amount..!\n")
    def withdraw(self):                                      #INSTANCE METHOD
        amount = int(input("How much amount you want to withdraw/debited..? ₹"))
        if amount<=5000:
         current_balance= self.get_balance()
         if amount<=0 or amount>current_balance:                       
           #2 CONDITIONS FOR CORRECT AMOUNT WITHDRAWING
            print("\n\t\tINSUFFICIENT FUNDS.........!")
            print("\n")
         else:
            new_balnce=current_balance-amount
            self.set_balance(int(new_balnce))
            print("After withdrawing, The account Balance is ₹",new_balnce)
            print("\n\t\tTHE AMOUNT IS WITHDRAWED SUCCESSFULLY.........!")
            print("\n")
            j='₹',amount,' Debited.'
            self.Tr_history.append(j)
            self.count+=1
        else:
           print("SBI bank withdraw limit is 5000...!\n ")
           print("Please Enter the valid amount for withdrawing..!")
    def transaction_count(self):      
       print("TRANSACTION COUNT:",self.count)         #Returns transaction count
       print("|---------------------------------------------------------------|")
       print("|                      TRANSACTION HISTORY                      |")
       print("|---------------------------------------------------------------|\n")
       for r in self.Tr_history:
          print("|\t\t",r,"\t\t|")                  #Returns transaction history 
       print("|______________________________________________________________|")

    @classmethod
    @staticmethod
    def bankname(cls):                             #CLASS METHOD & STATIC METHOD
        print("|---------------------------------------------------------------|")
        print("|                  WELCOME TO",cls.bank,"ATM                      |")
        print("|---------------------------------------------------------------|\n")
 
d=Atm()                                   
d.bankname()                                    
d.set_data()                                   
d.pin_creation()                                
#CONDITIONS FOR TRANSACTION PROCESS
while True:
 print("\n__________________________________________________________________\n")
 print("\tATM MENU:")
 print("1.Check Balance")
 print("2. Deposit Money")
 print("3.Withdraw Money")
 print("4.Accont Details")
 print("5.Transaction History")
 print("6.Exit")
 choice=int(input("Enter your choice 1/ 2/ 3/ 4/ 5/6: "))
 if choice==1:              #If you select choice 1 below 3 methods are executed
    d.pin_verification()              #Pin verification method for security 
    d.transaction()       #Transaction methods displays ATM transaction started
    d.check_balance()  #Check balance method returns the balance of your account
    print("__________________________________________________________________\n")
 elif choice==2:
    d.pin_verification()          #Pin verification method for security 
    d.transaction()       #Transaction methods displays ATM transaction started
    d.deposit()      #Deposit method is used for adds the money in your account
    print("__________________________________________________________________\n")
 elif choice==3:
    d.pin_verification()      #Pin verification method for security 
    d.transaction()        #Transaction methods displays ATM transaction started
    d.withdraw()   #Withdraw method is used for debits the money in your account
    print("__________________________________________________________________\n")
 elif choice==4:
    d.acc_details()            #acc_details method returns your details
    print("__________________________________________________________________\n")
 elif choice==5:
    d.transaction_count()               
  #transaction_count method returns the transaction count and transaction history
    print("__________________________________________________________________\n")
 elif choice==6:
 #if you enter choice 6 then the system asks exit confirmation message 
    print("Are you sure to exit this system...!\n")
    k=int(input("If you want to exit, please Enter 1:"))
    if k==1:             #if you enter 1 then the system will be exited 
       print("\n\t\tTHANK YOU FOR VISITING...!\n\t\t\tEXITING.....!")
       print("----------------------------------------------------------------")
       break
    else:#if you entered any other value except 1 the system continue the proces
       pass
 else:         
  #if you entered invalid choice the system returns the menu and continue 
     print("________________________________________________________________\n")
     print("\n\t\tENTER THE VALID CHOICE.....!")