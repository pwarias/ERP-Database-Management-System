<<<<<<< HEAD
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
    def newUser(self,conn):
        usrName = input("Enter a username: ")
        Pasword = input("Enter a password: ")
        confPassword = input("Confirm the password")
        if Pasword == confPassword:
            try:
                cursor.execute("Create user %s with password %s", (usrName,Pasword))
                userType = input("What type user is this user: ")
                cursor.execute("Grant %s privelages on database %s to %s", (userType,self.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42710: #User does not exist 
                    print("User already exist, try a new username")
                    newUser(conn)
                else:
                    print("Error %d occured", error)

        else:
            self.newUser()
        return
    def updateUser(self,conn):
        myCursor = conn.cursor()
        usrName = input("Enter a username you want to update: ")
        newPasword = input("Enter a password: ")
        confnewPassword = input("Confirm the password")
        if newPasword == confnewPassword:
            try:
                self.cursor.execute("Alter user %s with password %s", (usrName,newPasword))
                userType = input("What type of user is this user: ")
                self.cursor.execute("Grant %s privileges on database %s to %s", (userType,self.conn.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42704:
                    print("User does not exit")
                    another_new = input("Would you like to try another username or create a new username \n Options: \n1: Try again \n2: New User")
                    if another_new == 1:
                        updateUser(self,conn)
                    elif another_new == 2:
                        newUser(self,conn)
                    else:
                        return -1
                else:
                    print("Error %d occured", error)
                return -1    
        else:
            print("Password did not match")
            updateUser(self,conn)
        return

    #Customers function calls
    def newCustomer(self,conn):
        myCursor = conn.cursor()
        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        myCursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (fn,ln,))
        return
    def updateCustomer(self):
        return
    def viewCustomers(self):
        return

    #Model function calls
    def newModel(self,modelNumber,itemCost,orderNumber,conn):
        return
    def updateModel(self): 
        return

    #Design function calls
    def newDesign(self,employeeID,conn):
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
    def newEmployee(self,conn):
        employeeid = input("Enter the Employees ID: ")
        firstname = input("Enter the Employees first mame: ")
        lastname = input("Enter the Employees last name: ")
        ssn = input("Enter the Employees ssn: ")
        paytype = input("Enter the Employees paytype: ")
        jobtype = input("Enter the Employees job type: ")
        self.cursor.execute("Insert into Employee (employeeid,firstname,lastname,ssn,paytype,jobtype) values (%s,%s,%s,%s,%s,%s)", (employeeid,firstname,lastname,ssn,paytype,jobtype))
        return

    def employeeInfo(self): #Engineers have limited view of emplyee info like name, title, etc.
        return

    #Report function calls
    def createReport(self,conn):
        return
    def viewReport(self,conn):
        return
    
    #Inventory function calls
    #there is newModel() no need for addModel()
    def deleteModel(self):
        return
    def viewInventory(self,conn):
        return

    #Orger function calls
    def createOrder(self,conn):
        return
    def updateOrder(self,conn):
        return
    def viewOrders(self):
        return


    def newTable(self):
        return
    def updateTable(self):
        return
    
    
try:
    conTest = Connection()

finally:
    if(conTest):
        conTest.cursor.close()
        conTest.conn.close()
        print("PostgeSQL connection is closed")
=======
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
    def newUser(self,conn):
        myCursor = conn.cursor()
        usrName = input("Enter a username: ")
        Pasword = input("Enter a password: ")
        confPassword = input("Confirm the password")
        if Pasword == confPassword:
            try:
                myCursor.execute("Create user %s with password %s", (usrName,Pasword))
                userType = input("What type user is this user: ")
                myCursor.execute("Grant %s privelages on database %s to %s", (userType,self.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42710: #User does not exist 
                    print("User already exist, try a new username")
                    newUser(conn)
                else:
                    print("Error %d occured", error)

        else:
            self.newUser()
        return
    def updateUser(self,conn):
        myCursor = conn.cursor()
        usrName = input("Enter a username you want to update: ")
        newPasword = input("Enter a password: ")
        confnewPassword = input("Confirm the password")
        if newPasword == confnewPassword:
            try:
                self.cursor.execute("Alter user %s with password %s", (usrName,newPasword))
                userType = input("What type of user is this user: ")
                self.cursor.execute("Grant %s privileges on database %s to %s", (userType,self.conn.database,usrName))
                print("New User has been added")
            except(Exception,psycopg2.Error) as error:
                if error == 42704:
                    print("User does not exit")
                    another_new = input("Would you like to try another username or create a new username \n Options: \n1: Try again \n2: New User")
                    if another_new == 1:
                        updateUser(self,conn)
                    elif another_new == 2:
                        newUser(self,conn)
                    else:
                        return -1
                else:
                    print("Error %d occured", error)
                return -1    
        else:
            print("Password did not match")
            updateUser(self,conn)
        return

    #Customers function calls
    def newCustomer(self,conn):
        myCursor = conn.cursor()
        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        myCursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (fn,ln,))
        return
    def updateCustomer(self,conn):
        myCursor = conn.cursor()
        return
    def viewCustomers(self,conn):
        myCursor = conn.cursor()
        return

    #Model function calls
    def newModel(self,modelNumber,itemCost,orderNumber,conn):
        myCursor = conn.cursor()
        return
    def updateModel(self,conn): 
        myCursor = conn.cursor()
        return

    #Design function calls
    def newDesign(self,employeeID,conn):
        myCursor = conn.cursor()
        checkempID = self.cursor.execute("Select employeeId from employee where employeeId='%s'", employeeID)
        employeeID = input("Enter your employee ID: ")
        if employeeID == checkempID:
            modelNumber = input("Enter the new model number: ")
            try:
                checkModNum = self.cursor.execute("Select modelNumber from model where modelNumber=%s", modelNumber)
                print("Please try another model number")
                newDesign(self,employeeID,conn)
            except(Exception, psycopg2.Error) as error:
                if error == '02':
                    itemCost = input("Enter the items cost: ")
                    myCursor.execute("Insert into model (employeeif,costnumber,modelcost) values (%s,%s,%s)", (employeeID,modelNumber,itemCost))
                    return
                else:
                    newDesign(self,employeeID,conn)
        else:
            return

    #Employee function calls
    def newEmployee(self,conn):
        myCursor = conn.cursor()
        employeeid = input("Enter the Employees ID: ")
        firstname = input("Enter the Employees first mame: ")
        lastname = input("Enter the Employees last name: ")
        ssn = input("Enter the Employees ssn: ")
        paytype = input("Enter the Employees paytype: ")
        jobtype = input("Enter the Employees job type: ")
        self.cursor.execute("Insert into Employee (employeeid,firstname,lastname,ssn,paytype,jobtype) values (%s,%s,%s,%s,%s,%s)", (employeeid,firstname,lastname,ssn,paytype,jobtype))
        return

    def employeeInfo(self,conn): #Engineers have limited view of emplyee info like name, title, etc.
        myCursor = conn.cursor()
        return

    #Report function calls
    def createReport(self,conn):
        myCursor = conn.cursor()
        return
    def viewReport(self,conn):
        myCursor = conn.cursor()
        return
    
    #Inventory function calls
    #there is newModel() no need for addModel()
    def deleteModel(self,conn):
        myCursor = conn.cursor()
        return
    def viewInventory(self,conn):
        myCursor = conn.cursor()
        return

    #Orger function calls
    def createOrder(self,conn):
        myCursor = conn.cursor()
        return
    def updateOrder(self,conn):
        myCursor = conn.cursor()
        return
    def viewOrders(self,conn):
        myCursor = conn.cursor()
        return


    def newTable(self,conn):
        myCursor = conn.cursor()
        return
    def updateTable(self,conn):
        myCursor = conn.cursor()
        return
>>>>>>> 4db4d2184868642b2052ae55d47ece1aecad16e4
