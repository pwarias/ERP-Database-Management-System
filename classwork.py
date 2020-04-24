import psycopg2
import psycopg2.sql
import sys
from psycopg2.extensions import AsIs
from psycopg2 import sql

class Connection:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "postgres"
        self.cIdCounter = 0

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
        conn.close()
        print("PostgeSQL connection is closed")
        return


    #User function calls- changed recursive calls
    def newUser(self,conn):
        myCursor = conn.cursor()
        invalid=True
        while(invalid):
            usrName = input("Enter a username: ")
            Pasword = input("Enter a password: ")
            confPassword = input("Confirm the password: ")
            if Pasword == confPassword:
                try:
                    #manually scrub username for errors- special case
                    myCursor.execute("Create user %s with password %s", (AsIs(usrName),Pasword, )) #(AsIs(usrName), Pasword, ))
                    userType = input("What type user is this user: ")
                    myCursor.execute("Grant %s to %s", (AsIs(userType),AsIs(usrName)))
                    print("New User has been added")
                    invalid=False
                except(Exception,psycopg2.Error) as error:
                    if error == 42710: #User does not exist 
                        print("User already exist, try a new username")
                    else:
                        print("Error : ", str(error))

            else:
                print("Passwords do not match, please try again")
        return

    def updateUser(self,conn): #updated so no recursive calls
        myCursor = conn.cursor()
        usrName = input("Enter a username you want to update: ")
        newPasword = input("Enter a password: ")
        confnewPassword = input("Confirm the password")
        invalid=True
        if newPasword == confnewPassword:
            while(invalid):
                try:
                    myCursor.execute("Alter user %s with password %s", (usrName,newPasword))
                    userType = input("What type of user is this user: ")
                    myCursor.execute("Grant %s privileges on database %s to %s", (userType,self.database,usrName))
                    print("New User has been added")
                    invalid=False
                except(Exception,psycopg2.Error) as error:
                    if error == 42704:
                        print("User does not exit")
                    else:
                        print("Error %d occured", error)
                    return -1    
        else:
            print("Password did not match")
        return

    #Model function calls
    def newModel(self,modelNumber,itemCost,orderNumber,conn):
        myCursor = conn.cursor()
        return

    #Design function calls- verify why the double employee id check
    def newDesign(self,employeeID,conn):
        myCursor = conn.cursor()
        checkempID = myCursor.execute("Select employeeId from employee where employeeId='%s'", employeeID)
        employeeID = input("Enter your employee ID: ")
        invalid=True
        if employeeID == checkempID:
            while(invalid):
                modelNumber = input("Enter the new model number: ")
                try:
                    myCursor.execute("Select modelNumber from model where modelNumber=%s", modelNumber)#should throw an error

                    print("Please try another model number") 

                except(Exception, psycopg2.Error) as error:
                    if error == '02':
                        itemCost = input("Enter the items cost: ")
                        myCursor.execute("Insert into model (employeeid,costnumber,modelcost) values (%s,%s,%s)", (employeeID,modelNumber,itemCost))
                        invalid=False
                        return
        else:
            print("Invalid Employee id")#check what this might be for

    #Employee function calls
    def newEmployee(self,conn):
        myCursor = conn.cursor()
        employeeid = input("Enter the Employees ID: ")
        firstname = input("Enter the Employees first mame: ")
        lastname = input("Enter the Employees last name: ")
        ssn = input("Enter the Employees ssn: ")
        paytype = input("Enter the Employees paytype: ")
        jobtype = input("Enter the Employees job type: ")
        myCursor.execute("Insert into Employee (employeeid,firstname,lastname,ssn,paytype,jobtype) values (%s,%s,%s,%s,%s,%s)", (employeeid,firstname,lastname,ssn,paytype,jobtype))
        return


    #Customers function calls
    def customerIdCounter(self):
        rtrn = self.cIdCounter + 1
        self.cIdCounter += 1
        return rtrn
        
    def newCustomer(self,conn):
        myCursor = conn.cursor()
        fName = input("Enter First Name: ")
        lName = input("\nEnter Last Name: ")
        #cId = customerIdCounter() 
        #SmyCursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (cId, fName,lName))
        return

    def updateCustomer(self,conn): #still needs validation of customerId
        myCursor = conn.cursor()
        confirmCId = input("Please enter the ID of the customer you want to update: ")
        fName = input("\nEnter new First Name: ")
        lName = input("\nEnter new Last Name: ")
        myCursor.execute("update Customer set firstName = %s, lastName = %s where customerId = %s", (fName, lName, confirmCId))
    def viewCustomers(self,conn):
        myCursor = conn.cursor()
        myCursor.execute("select * from Customer")
        #need to print out table.
        #can it be done by "print(myCursor.execute('select * from Customer'))"?
        return

    #Przmek
    #Report function calls
    def createTotalRevenue(self, conn): #Neeeds testing
        #total revenue from sale, associate employee and customer
        myCursor=conn.cursor()
        sql="create or replace view total_revenue as select employeeid, customerid, sum(saleprice) from orders group by employeeid, customerid;"
        myCursor.execute(sql)

    def createCustomerPrediction(self, conn): #Neeeds testing
        #Customer model bought and quantity to make prediction and understand trending
        myCursor=conn.cursor()
        sql= "create view customer_prediction as select orders.customerid, inventory.modelname, count(orders) from orders, inventory group by customerid, modelname;"
        myCursor.execute(sql)

    def createOrderInentory(self, conn): #Neeeds testing
        #For each order, the associated parts and available inventory
        myCursor=conn.cursor()
        sql="create or replace view parts as select orders.ordernumber, inventory.modelname, inventory.quantity from orders, inventory;"
        myCursor.execute(sql)

    def viewExpenseReport(self, conn): #Neeeds testing
        #Expense report, employee showing salary, bonus expense and part cost
        myCursor=conn.cursor()
        modelCostQuery="select sum(costmodel) from model"
        salaryCostQuery="select sum(employee.salary) from employee where employee.paytype= 'Salary'"
        hourlyCostQuery="select sum(employee.salary * 40 * 52) from employee where employee.paytype= 'Hourly'"

        myCursor.execute(modelCostQuery)
        modelCost=myCursor.fetchall()
        print("cost for models is: ")
        print(modelCost)

        myCursor.execute(salaryCostQuery)
        salaryCost=myCursor.fetchall()
        print("cost for the salary employee is: ")
        print(salaryCost)

        myCursor.execute(hourlyCostQuery)
        hourlyCost=myCursor.fetchall()
        print("cost for the hourly employee's working 40 hour workweeks 52 weeks a year: ")
        print(hourlyCost)
        return


    def viewTotalRevenue(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from total_revenue"
        myCursor.execute(sql)
        totalRev=myCursor.fetchall()
        print(totalRev)
        return



    def viewCustomerPrediction(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from customer_prediction"
        myCursor.execute(sql)
        custPred=myCursor.fetchall()
        print(custPred)
        return

    def viewOrderInventory(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from parts"
        myCursor.execute(sql)
        parts=myCursor.fetchall()
        print(parts)
        return
    

    def newTable(self,conn): #checked with Ola likely not needed
        myCursor = conn.cursor()
        return
    def updateModel(self, conn):
        myCursor = conn.cursor()
        invalid=True
        while(invalid):
            try:
                id=input("Please enter the model number of the model: ")
                myCursor.execute("Select modelNumber from model where modelNumber='%s'", (id, ))
                newCost=input("Please enter the new cost of the model: ") #error checking
                newLead=input("Please enter the new lead time: ")
                newDesign=input("Please enter the new designId: ")
                sql="UPDATE model SET costmodel=%s, designId=%s, leadtime=%s, WHERE modelname=%s"
                myCursor.execute(sql, (newCost, newDesign, newLead, id, ))
                myCursor.commit() #should include after all executions
                invalid=False

            except:
                print("Error: model number not found")

        return
    def updateInventory(self, conn):
        myCursor = conn.cursor()
        invalid=True
        while(invalid):
            try:
                id=input("Please enter the inventory id: ")
                myCursor.execute("Select inventoryId from inventory where inventoryId='%s'", (id, ))
                newPrice=input("Please enter the new sales price: ")
                newQuantity=input("Please enter the new quantity: ")
                sql="UPDATE inventory SET saleprice=%s, quantity=%s WHERE inventoryId=%s"
                myCursor.execute(sql, (newPrice, newQuantity, id, ))
                myCursor.commit() #should include after all executions
                invalid=False

            except:
                print("Error: Inventory Id not found")

        return
    def updateEmployee(self, conn):
        myCursor = conn.cursor()
        invalid=True
        while(invalid):
            try:
                id=input("Please enter the employee id: ")
                myCursor.execute("Select employeeId from employee where employeeId='%s'", (id, ))
                #updates can be made more granular
                newFirst=input("Please enter the employee's new first name: ")
                newLast=input("Please enter the employee's new last name: ")
                newPayType=input("Please enter the employee's new pay type: ")
                #newSalary=input("Please enter the employee's new pay type: ")
                sql="UPDATE employee SET firtname=%s, lastname=%s, paytype=%s WHERE employeeId=%s"
                myCursor.execute(sql, (newFirst, newLast, newPayType, id, ))
                myCursor.commit() #should include after all executions
                invalid=False

            except:
                print("Error: Inventory Id not found")

        return

    #Andrew
    #Inventory function calls
    #there is newModel() no need for addModel()
    def deleteModel(self,conn):
        myCursor = conn.cursor()
        return
    def viewInventory(self,conn):
        myCursor = conn.cursor()
        return
    #Order function calls
    def createOrder(self,conn):
        myCursor = conn.cursor()
        return
    def updateOrder(self,conn):
        myCursor = conn.cursor()
        return
    def viewOrders(self,conn):
        myCursor = conn.cursor()
        return
    #Part of Employee Function calls
    def employeeInfo(self,conn): #Engineers have limited view of emplyee info like name, title, etc.
        myCursor = conn.cursor()
        return
    