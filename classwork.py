import psycopg2
import sys
class Connection:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "8081"
        self.database = "postgres"

    #Login/out function calls
    def loginIn(self,usrName,Pasword):
        try:
            conn = psycopg2.connect(user = usrName,
                                        password = Pasword,
                                        host = self.host,
                                        port = self.port,
                                        database = self.database)
            print("after connecting")
            return conn
        except(Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
            return
    
    def loginOut(self,conn):
        print("Hello!!")
        conn.close()
        print("PostgeSQL connection is closed")
        return


    #User function calls
    def newUser(self,cursor):
        usrName = input("Enter a username: ")
        Pasword = input("Enter a password: ")
        confPassword = input("Confirm the password")
        if Pasword == confPassword:
            try:
                cursor.execute("Create user %s with password %s", (usrName,Pasword))
                userType = input("What type user is this user: ")
                cursor.execute("Grant %s privelages on database %s to %s", (userType,self.conn.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42710: #User does not exist 
                    print("User already exist, try a new username")
                    self.newUser()
                else:
                    print("Error %d occured", error)

        else:
            self.newUser()
        return
    def updateUser(self):
        usrName = input("Enter a username you want to update: ")
        newPasword = input("Enter a password: ")
        confnewPassword = input("Confirm the password")
        if newPasword == confnewPassword:
            try:
                self.cursor.execute("Alter user %s with password %s", (usrName,newPasword))
                userType = input("What type user is this user: ")
                self.cursor.execute("Grant %s privelages on database %s to %s", (userType,self.conn.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42704:
                    print("User does not exit")
                    another_new = input("Would you like to try another username or create a new username \n Options: \n1: Try again \n2: New User")
                    if another_new == 1:
                        self.conn.updateUser(self)
                    elif another_new == 2:
                        self.conn.newUser(self)
                    else:
                        return -1
                else:
                    print("Error %d occured", error)
                return -1    
        else:
            print("Password did not match")
            self.updateUser()
        return

    #Customers function calls
    def newCustomer(self):

        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        self.cursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (fn,ln,))
        return
    def updateCustomer(self):
        return
    def viewCustomers(self):
        return

    #Model function calls
    def newModel(self,modelNumber,itemCost,orderNumber):
        return
    def updateModel(self):
        return

    #Design function calls
    def newDesign(self,employeeID):
        checkempID = self.cursor.execute("Select employeeId from employee where employeeId='%s'", employeeID)
        employeeID = input("Enter your employee ID: ")
        if employeeID == checkempID:
            modelNumber = input("Enter the new model number: ")
            try:
                checkModNum = self.cursor.execute("Select modelNumber from model where modelNumber=%s", modelNumber)
                print("Please try another model number")
                self.newDesign(self)
            except(Exception, psycopg2.Error) as error:
                if error == '02':
                    itemCost = input("Enter the items cost: ")
                    self.cursor.execute("Insert into model (employeeif,costnumber,modelcost) values (%s,%s,%s)", (employeeID,modelNumber,itemCost))
                    return
                else:
                    self.newDesign(employeeID)
        else:
            return

    #Employee function calls
    def newEmployee(self):
        employeeid = input("Enter the Employees ID: ")
        firstname = input("Enter the Employees first mame: ")
        lastname = input("Enter the Employees last name: ")
        ssn = input("Enter the Employees ssn: ")
        paytype = input("Enter the Employees paytype: ")
        jobtype = input("Enter the Employees job type: ")
        self.cursor.execute("Insert into Employee (employeeid,firstname,lastname,ssn,paytype,jobtype) values (%s,%s,%s,%s,%s,%s)", (employeeid,firstname,lastname,ssn,paytype,jobtype))
        return

    #Report function calls
    def createReport(self):
        return
    def viewReport(self):
        return
    
    #Inventory function calls
    def addModel(self):
        return
    def deleteModel(self):
        return
    def viewInventory(self):
        return

    #Orger function calls
    def createOrder(self):
        return
    def updateOrder(self):
        return
    def viewOrders(self):
        return