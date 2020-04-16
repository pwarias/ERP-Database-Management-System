import psycopg2
import sys
class Connection:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(user = "postgres",
                                        password = "Yaysql37",
                                        host = "127.0.0.1",
                                        port = "8080",
                                        database = "cs425db")
            self.cursor = self.conn.cursor()
        except(Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
    def closeConnection(self):
        if(self.conn):
            self.cursor.close()
            self.conn.close()
            print("PostgeSQL connection is closed")
            return

    #Login/out function calls
    def loginIn(self, usrName,Pasword):
        try:
            self.conn = psycopg2.connect(user = usrName,
                                        password = Pasword,
                                        host = "127.0.0.1",
                                        port = "8080",
                                        database = "cs425db")
            self.cursor = self.conn.cursor()
        except(Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
            return

    #User function calls
    def newUser(self):
        usrName = input("Enter a username: ")
        Pasword = input("Enter a password: ")
        confPassword = input("Confirm the password")
        if Pasword == confPassword:
            self.cursor.execute("Create user %s with password %s", (usrName,Pasword))
            userType = input("What type user is this user: ")
            self.cursor.execute("Grant %s privelages on database %s to %s", (userType,self.conn.database,usrName))
            print("New User has been added")
        else:
            self.newUser()
        return
    def updateUser(self):
        return

    #Customers function calls
    def newCustomer(self):

        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        self.cursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (fn,ln,))
        return
    def updateCustomer():
        return
    def viewCustomers():
        return

    #Model function calls
    def newModel(self,modelNumber,itemCost,orderNumber):
        return
    def updateModel()
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
    def addModel():
        return
    def deleteModel():
        return
    def viewInventory():
        return

    #Orger function calls
    def createOrder():
        return
    def updateOrder():
        return
    def viewOrders():
        return

    
try:
    conTest = Connection()

finally:
    if(conTest):
        conTest.cursor.close()
        conTest.conn.close()
        print("PostgeSQL connection is closed")