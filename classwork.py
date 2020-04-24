import psycopg2
import psycopg2.sql
import sys
from psycopg2.extensions import AsIs
from psycopg2 import sql
import datetime

class Connection:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "8080"
        self.database = "postgres"

    #Login/out function calls
    def loginIn(self,usrName,Pasword,employeeid):
        try:
            conn = psycopg2.connect(user = usrName,
                                    password = Pasword,
                                    host = self.host,
                                    port = self.port,
                                    database = self.database)
            myCursor = conn.cursor()
            currentTime = datetime.datatime.now()
            date = int(currentTime.strftime("%Y%m%d"))
            time = int(currentTime.strftime("%H%M%S"))
            loginid = getMaxID(conn,'login','loginid')+1
            myCursor.execute("Insert into login (loginid,privilege,logouttime,logintime,employeeid,logindate,logoutdate) \
                             values () ", (loginid,roleCheck(conn),0,time,employeeid,0))
            conn.commit()
            return conn,loginid
        except(Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
            return
    
    def loginOut(self,conn,loginid):
        myCursor = conn.cursor()
        LogoutTime = datetime.datatime.now()
        outDate = int(LogoutTime.strftime("%Y%m%d"))
        outTime = int(LogoutTime.strftime("%H%M%S"))
        myCursor.execute("update login set (logouttime,logoutdate)=(%d,%d) where loginid = %d",(outTime,outDate,loginid))
        conn.commit()
        conn.close()
        print("PostgeSQL connection is closed")
        return

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



    #User function calls
    def newUser(self,conn):
        myCursor = conn.cursor()
        invalid=True
        while(invalid):
            usrName = input("Enter a username: ")
            Password = input("Enter a password: ")
            confPassword = input("Confirm the password: ")
            if Password == confPassword:
                try:
                    #manually scrub username for errors- special case
                    myCursor.execute("Create user %s with password %s", (AsIs(usrName),Password, )) #(AsIs(usrName), Pasword, ))
                    conn.commit()
                    userType = input("What type user is this user: ")
                    myCursor.execute("Grant %s to %s", (AsIs(userType),AsIs(usrName)))
                    conn.commit()
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
                    conn.commit()
                    userType = input("What type of user is this user: ")
                    myCursor.execute("Grant %s privileges on database %s to %s", (userType,self.database,usrName))
                    conn.commit()
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

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



    #Customers function calls
    def newCustomer(self,conn):
        myCursor = conn.cursor()
        fName = input("Enter First Name: ")
        lName = input("\nEnter Last Name: ")
        myCursor.execute("select * from customer where firstName = %s and lastName = %s", (fName, lName))
        conn.commit()
        duplicateName = myCursor.fetchall() #if this list is empty then the customer has not been added yet
        if duplicateName:
            ques = input("Customer with that name already exists. Is this a different customer with the same name? (Y/N)")
            if ques == "Y":
                cId = getMaxID(conn,'customer','customerid')+1
                myCursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (cId, fName,lName))
                conn.commit()
        else:
            cId = getMaxID(conn,'customer','customerid')+1 
            myCursor.execute("Insert into Customer (customerid,firstname,lastname) values (%s,%s)", (cId, fName,lName))
            conn.commit()
    def updateCustomer(self,conn):
        myCursor = conn.cursor()
        invalid = True
        while invalid == True:
            confirmCId = input("Please enter the ID of the customer you want to update: ")
            myCursor.execute("select * from Customer where customerId = %s", (confirmCId))
            idExists = myCursor.fetchall() #list of that customerId, should not be empty
            if idExists:
                invalid = False
            else:
                tryAgain = input("Customer ID does not exist. Would you like to try another ID? (Y/N)")
                if tryAgain != "Y":
                    return
        fName = input("\nEnter new First Name: ")
        lName = input("\nEnter new Last Name: ")
        myCursor.execute("update Customer set firstName = %s, lastName = %s where customerId = %s", (fName, lName, confirmCId))
        conn.commit()
    def viewCustomers(self,conn):
        print("Customer ID\tFirst Name\tLast Name")
        myCursor = conn.cursor()
        myCursor.execute("select * from Customer")
        allCust = myCursor.fetchall()
        for i in range(len(all)):
            print(allCust[i][0], "\t\t", allCust[i][1], "\t\t", allCust[i][2])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



    #Model function calls
    def newModel(self,conn):
        myCursor = conn.cursor()
        invalid = True
        while invalid == True:
            dsnNmbr = input("Please enter the design ID of the design that you would like to make a model \
                            and add to the inventory: ")
            myCursor.execute("select designid from design where designid = %d", (dsnNmbr))
            doesExist = myCursor.fetchall()
            if doesExist:
                invalid = False
            else:
                tryAgain = input("Invalid design ID. Would you like to try another design ID? (Y/N)")
                if tryAgain != "Y":
                    return
        name = input("Please enter a name for this model: ")
        cost = input("Please enter how much it cost for this model to be manufactured: ")
        price = input("Please enter a price for this model: ")
        time = input("Please enter how long it took to manufacturer this model in days: ")
        category = input("Please enter a category for this model: ")
        quantity = input("Please enter a quantity for this model: ")
        invId = getMaxID(conn,'inventory','inventoryid')+1
        myCursor.execute("insert into Model (modelname, costmodel, designid, leadtime) values (%s, %s, %s, %s)", (name, cost, doesExist[0], time))
        conn.commit()
        myCursor.execute("insert into inventory (inventoryId, saleprice, category, modelname, quantity) values (%s, %s, %s %s, %s)", (invId, price, category, name, quantity))
        conn.commit()

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

    def deleteModel(self,conn):
        invalid = True
        while(invalid):
            try:
                myCursor = conn.cursor()
                delModel = input("What model would you like to delete: ")
                modelNum = input("What is the model number you would like to delete: ")
                myCursor.execute("delete from model where modelnumber=%s and modelname=%s", (delModel,modelNum))
                conn.commit()
                print("Model has been created")
                invalid = False
            except(Exception, psycopg2.Error) as error:
                        if error == 42704:
                            print("Error occured",error)
                            invalid = True

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    

    #Design function calls- verify why the double employee id check
    def newDesign(self,conn):
        myCursor = conn.cursor()
        employeeID = input("Enter your employee ID: ")
        myCursor.execute("Select employeeId from employee where employeeId='%s'", employeeID)
        checkempID = myCursor.fetchall()
        invalid=True
        invalidemp = True
        while(invalid):
            if employeeID == checkempID[0]:
                #is there something supposed to be here?
                while(invalid):
                    modelNumber = input("Enter the new model number: ")
                    try:
                        myCursor.execute("Select modelNumber from model where modelNumber=%s", modelNumber)#should throw an error
                        conn.commit()
                        print("Please try another model number") 

                    except(Exception, psycopg2.Error) as error:
                        if error == '02':
                            itemCost = input("Enter the items cost: ")
                            myCursor.execute("Insert into model (employeeid,modelnumber,costitem) values (%s,%s,%s)", (employeeID,modelNumber,itemCost))
                            conn.commit()
                            invalid=False
                            return
            else:
                print("Invalid Employee id")
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    #Employee function calls
    def newEmployee(self,conn):
        myCursor = conn.cursor()
        employeeid = input("Enter the Employee's ID: ")
        firstname = input("Enter the Employee's first mame: ")
        lastname = input("Enter the Employee's last name: ")
        ssn = input("Enter the Employee's ssn: ")
        paytype = input("Enter the Employee's paytype: ")
        jobtype = input("Enter the Employee's job type: ")
        myCursor.execute("Insert into Employee (employeeid,firstname,lastname,ssn,paytype,jobtype) values \
                        (%s,%s,%s,%s,%s,%s)", (employeeid,firstname,lastname,ssn,paytype,jobtype))

    def updateEmployee(self,conn):
        myCursor = conn.cursor()
        invalid = True
        invalid1 = True
        while invalid == True:
            eId = input("What is the employee ID of the employee you want to update:")
            myCursor.execute("select employeeid from employee where employeeid = %s", (eId))
            eIdTuple = myCursor.fetchone()
            if eIdTuple:
                invalid = False
            else:
                tryAgain = input("Invalid employee ID. Would you like to try another ID? (Y/N)")
                if tryAgain != "Y":
                    return
        change = input("Select an option (number):\n1. Change name\n2. Change pay type\
                        \n3. Change job type\n4. Change salary: ")
        while invalid1 == True:
            if change == "1":
                invalid1 = False
                fName = input("\nEnter new First Name: ")
                lName = input("\nEnter new Last Name: ")
                myCursor.execute("update Employee set firstName = %s, lastName = %s where employeeid = %s",
                                (fName, lName, eId))
                conn.commit()
            elif change == "2":
                invalid1 = False
                ptype = input("Enter new pay type (hourly or salary): ")
                myCursor.execute("update Employee set paytype = %s where employeeid = %s", (ptype, eId))
            elif change == "3":
                invalid1 = False
                jtype = input("Enter new job type (Sales, Engineer, HR, Admin): ")
                myCursor.execute("update Employee set jobtype = %s where employeeid = %s", (jtype, eId))
            elif change == "4":
                invalid1 = False
                newSalary = input("Enter new salary (hourly rate if hourly pay type): ")
                myCursor.execute("update Employee set salary = %s where employeeid = %s", (newSalary, eId))
            else:
                print("Please choose a valid option")

    def employeeInfo(self,conn,jobtype): #Engineers have limited view of emplyee info like name, title, etc.
        myCursor = conn.cursor()
        if jobtype == "engineer":
            myCursor.execute("select * from engineeremployeeview")
            employees = myCursor.fetchall()
            print(" First Name \t\t Last Name \t\t Job Type")
            for i in range(len(employees)):
                print(employees[i][0], "\t\t", employees[i][1], "\t\t", employees[i][2])
        elif jobtype == "postgres":
            myCursor.execute("select * from employee")
            employees = myCursor.fetchall()
            print(" Employee ID \t\t First Name \t\t Last Name \t\t Social Security Number \t\t Pay Type \t\t Job Type")
            for i in range(len(employees)):
                print(employees[i][0], "\t\t", employees[i][1], "\t\t", employees[i][2],employees[i][3], "\t\t", employees[i][4], "\t\t", employees[i][5])
        else:
            myCursor.execute("select * from hremployeeview")
            employees = myCursor.fetchall()
            print(" Employee ID \t\t First Name \t\t Last Name \t\t Pay Type \t\t Job Type")
            for i in range(len(employees)):
                print(employees[i][0], "\t\t", employees[i][1], "\t\t", employees[i][2], employees[i][3])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



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

    def viewTotalRevenue(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from total_revenue"
        myCursor.execute(sql)
        totalRev=myCursor.fetchall()
        print(totalRev)

    def viewCustomerPrediction(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from customer_prediction"
        myCursor.execute(sql)
        custPred=myCursor.fetchall()
        print(custPred)

    def viewOrderInventory(self,conn): #Neeeds testing
        myCursor = conn.cursor()
        sql="select * from parts"
        myCursor.execute(sql)
        parts=myCursor.fetchall()
        print(parts)

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

    #Abdallah
    #Table function calls
    def updateTable(self, conn):
        myCursor = conn.cursor()
        invalid = True
        myCursor.execute("select table_name from information_schema.tables where table_schema = 'public'")
        tblNames = myCursor.fetchall() #list of all tables and views
        while invalid == True:
            tblName = input("Please enter the name of the table: ")
            if tblName in tblNames:
                invalid = False
            else:
                tryAgain = input("Table doesn't exist. Would you like to try another name? (Y/N)")
                if tryAgain != "Y":
                    return
        myCursor.execute("select column_name from information_schema.columns where table_schema = 'public'\
                         and table_name = %s", (tblName))
        cols = myCursor.fetchall() #list of tuples i.e. [(employeeId), (firstName)...(salary)]
        option = input("Please select an option (number):\n1. Rename column\n2. Add coulumn\n3. Delete column")
        while invalid == True:
            if option == "1":
                invalid = False
                invalid1 = True
                while invalid1 == True:
                    col = input("Please enter the name of the column you want to rename: ")
                    if col in cols:
                        invalid1 = False
                    else:
                        tryAgain = input("Column doesn't exist. Would you like to try another name? (Y/N)")
                        if tryAgain != "Y":
                            return
                newCol = input("Please enter the new column name: ")
                myCursor.execute("alter table %s rename column %s to %s", (col, newCol))
            elif option == "2":
                invalid = False
            elif option == "3":
                invalid = False
            else:
                tryAgain = input("Invalid input. Would you like to try again? (Y/N)")
                if tryAgain != "Y":
                    return

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



    #Inventory function calls
    def viewInventory(self,conn):
        myCursor = conn.cursor()
        myCursor.execute("select * from Inventory")
        allInv = myCursor.fetchall()
        print("Inventory ID \t\t Sale Price \t\t Category \t\t Model Name \t\t Quantity \n")
        for i in range(len(allInv)):
            print(allInv[i][0], "\t\t", allInv[i][1], "\t\t", allInv[i][2], "\t\t", allInv[i][3], "\t\t", allInv[i][4])
        return

    def updateInventory(self,conn):
        myCursor = conn.cursor()
        valid_input = False
        while valid_input == False:
            print("Update Inventory Menu:")
            menuSelect = input("1. Update Quantity \n 2. Remove Item")
            if menuSelect == "1":
                valid_input = True
                inventoryid = input("What inventory ID would you like to update: ")
                invenid = myCursor.execute("slect inventoryid from inventory where inventoryid = %d",inventoryid)
                inventvals = myCursor.fetchone()[0]
                if inventoryid == inventvals:
                    newQuantity = input("What is the updated quantity: ")
                    myCursor.execute("update inventory set quantity = newQuantity where inventoryid = %d", inventoryid)
                    conn.commit()
                    return
            elif menuSelect == "2":
                valid_input = True
                inventoryid = input("What inventory ID would you like to remove: ")
                invenid = myCursor.execute("slect inventoryid from inventory where inventoryid = %d",inventoryid)
                inventvals = myCursor.fetchone()[0]
                if inventoryid == inventvals:
                    myCursor.execute("delete from inventory where inventoryid = inventoryid")
                    conn.commit()
                    return
            else:
                tryAgain = input("Invalid input. Would you like to try again? (Y/N)")
                if tryAgain != "Y":
                    return



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



    #Order function calls
    def createOrder(self,conn):
        myCursor = conn.cursor()
        ordernumber = getMaxID(conn,'order','ordernumber')+1
        custumerid = input("Enter the custumers ID number: ")
        custIdCheck = myCursor.execute("select custumerid from customer where customerid = %d",custumerid)
        custvals = myCursor.fetchall()
        if custvals:
            employeeid = input("Enter your employee ID number: ") 
            inventoryid = input("Enter the inventory ID you would like to purchase: ")
            myCursor.execute("select quantity from inventory where inventoryid = %d",inventoryid)
            checkInventory = myCursor.fetchone()[0]
            if checkInventory > 0:
                myCursor.execute("select saleprice from inventory where inventoryid = %d",inventoryid)
                saleprice = myCursor.fetchone()[0]
                myCursor.execute("Insert into order (ordernumber,customerid,employeeid,saleprice,inventoryId) values ()")
                conn.commit()
                myCursor.execute("Update inventory set inventory = %d where inventoryid = %d",
                                (checkInventory-1,inventoryid))
                conn.commit()
        return
    def updateOrder(self,conn):
        myCursor = conn.cursor()
        valid_input = False
        valid_input1 = False
        print("Select a menu (number): \n")
        while valid_input == False: #loop until valid response
            option = input("1. Change Model \n2. Delete Order") #prompt user for option
            if option == "1":
                pass
        return
    def viewOrders(self,conn):
        myCursor = conn.cursor()
        myCursor.execute("select * from orders")
        orders = myCursor.fetchall()
        print(" Order Numeber \t\t Customer ID \t\t Employee ID \t\t Sale Price \t\t Inventory")
        for i in range(len(orders)):
            print(orders[i][0], "\t\t", orders[i][1], "\t\t", orders[i][2], "\t\t", orders[i][3], "\t\t", orders[i][4])
        return

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


    #Useful functions
    def getMaxID(self,conn,table,column):
        myCursor = conn.cursor()
        myCursor.execute("select max(%s) from %s", (column,table))
        maxID = myCursor.fetchone()
        if maxID:
            return maxID[0]
        return 1
    
    def roleCheck(self, conn):
        cur = conn.cursor()
        cur.execute('''SELECT current_user;''')
        rows=cur.fetchall()
        currentUser=rows[0]  #grab username
        
        query="SELECT rolname FROM pg_roles WHERE pg_has_role( (%s), oid, 'member');" #see which role the user has
        cur.execute(query, currentUser)
        rows=cur.fetchall()
        roleType=[]
        for i in range(len(rows)-1):
                roleType.append(''.join(rows[i]))
        #print(roleType) all roles including inherited types, excludes name

        #assume that emplyees can't have more than one role (not including inherited)
        return roleType[len(roleType)-1] #the last role will contain the actual role of the user


        conn.commit()
    