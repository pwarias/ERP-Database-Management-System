import psycopg2
import classwork

def mainMenu():
      
            #we could also query db for the users role and display options based on that?
            print("Welcome to the ERP DBMS!\n\nMain Menu")
            username = input("Please enter your username: ")
            passwrd = input("Please enter your password: ")
            employeeid = input("What is your employee id: ")


            #call one of the following menus after verifying login info
            #call permisionCheck() to then call correspodning menu
            classConnect=classwork.Connection()
            connReturn=classConnect.loginIn(username, passwrd,employeeid)
            conn = connReturn[0]
            loginid = connReturn[1]
            role = classConnect.roleCheck(conn)
            try:
                  if role == "admins" or role=="postgres":
                        admin_menu(classConnect, conn,employeeid,loginid)
                  elif role == "engineer":
                        engineer_menu(classConnect, conn,employeeid,loginid)
                  elif role == "sales":
                        sales_menu(classConnect, conn,employeeid,loginid)
                  elif role == "hr":
                        hr_menu(classConnect, conn,employeeid,loginid)
                  else:
                        print("if you're reading this, something went wrong, check 'mainMenu()' in dbtest.py") 
            except KeyboardInterrupt:
                  classConnect.loginOut(conn,employeeid,classConnect.roleCheck(conn),loginid)


def admin_menu(classConnect, conn,employeeid,loginid):
      try:
            valid_input = False
            valid_input1 = False
            print("Select a menu (number): \n")
            while valid_input == False: #loop until valid response
                  option = input("1. Users \n2. Tables \n3. Reports \n4. View Employees:") #prompt user for option
                  if option == "1":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create user \n 2. Update user \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.newUser(conn)
                              elif option1 == "2": #this is also for granting access to other users
                                    valid_input1 == True
                                    classConnect.updateUser(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "2":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create table \n 2. Update table \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.newTable(conn)
                              elif option1 == "2":
                                    valid_input1 == True
                                    classConnect.updateTable(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "3":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create report \n 2. View report \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.createReport(conn)
                              elif option1 == "2":
                                    valid_input1 == True
                                    classConnect.viewReport(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "4":
                        valid_input = True
                        classConnect.employeeInfo(conn,classConnect.roleCheck(conn))
                  else:
                        print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn,employeeid,classConnect.roleCheck(conn),loginid)

def engineer_menu(classConnect, conn,employeeid,loginid):
      try:
            valid_input = False
            valid_input1 = False
            print("Select a menu (number): \n")
            while valid_input == False: #loop until valid response
                  option = input("1. Models \n 2. Inventory \n 3. Employee Infromation \n") #prompt user for option
                  if option == "1":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create model \n 2. View models \n 3. Update model \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.newDesign(conn)
                              elif option1 == "2":
                                    valid_input1 = True
                                    classConnect.viewInventory(conn)
                              elif option1 == "3":
                                    valid_input1 = True
                                    classConnect.updateModel(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "2":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Add model to inventory \n 2. Delete model from inventory \n 3. View inventory \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.newModel(conn)
                              elif option1 == "2":
                                    valid_input1 == True
                                    classConnect.deleteModel(conn)
                              elif option1 == "3":
                                    valid_input1 = True
                                    classConnect.viewInventory(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "3":
                        valid_input = True
                        classConnect.employeeInfo(conn, classConnect.roleCheck(conn))
                  else:
                        print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn,employeeid,classConnect.roleCheck(conn),loginid)

def sales_menu(classConnect, conn,employeeid,loginid):
      try:
            valid_input = False
            valid_input1 = False
            print("Select a menu (number): \n")
            while valid_input == False: #loop until valid response
                  option = input("1. Customers \n2. Orders \n3. Reports \n") #prompt user for option
                  if option == "1":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create customer \n 2. Update customer \n 3. View Customers \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.newCustomer(conn)
                              elif option1 == "2":
                                    valid_input1 = True
                                    classConnect.updateCustomer(conn)
                              elif option1 == "3":
                                    valid_input1 = True
                                    classConnect.viewCustomers(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "2":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Create order\n2. Update order\n3. Delete order\n4. View Orders \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.createOrder(conn)
                              elif option1 == "2":
                                    valid_input1 == True
                                    classConnect.updateOrder(conn)
                              elif option1 == "3":
                                    valid_input1 = True
                                    classConnect.deleteOrder(conn)
                              elif option == "4":
                                    valid_input1 = True
                                    classConnect.viewOrders(conn)
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "3":
                        valid_input = True
                        classConnect.viewReport(conn)
                  else:
                        print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn,employeeid,classConnect.roleCheck(conn),loginid)

def hr_menu(classConnect, conn,employeeid,loginid):
      try:
            valid_input = False
            valid_input1 = False
            print("Select a menu (number): \n")
            while valid_input == False: #loop until valid response
                  option = input("1. Employee information \n 2. idk \n") #prompt user for option
                  if option == "1":
                        valid_input = True
                        print("Select an option (number): \n")
                        while valid_input1 == False: #loop until valid response
                              option1 = input("1. Update employee \n 2. View employees \n") #prompt user for option
                              if option1 == "1":
                                    valid_input1 = True
                                    classConnect.updateUser(conn)
                              elif option1 == "2":
                                    valid_input1 = True
                                    classConnect.employeeInfo(conn,classConnect.roleCheck(conn))
                              else:
                                    print("Please choose a valid option \n")
                  elif option == "2":
                        valid_input = True
                        print("working on this") #idk
                  else:
                        print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn,employeeid,classConnect.roleCheck(conn),loginid)              

mainMenu()