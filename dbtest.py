import psycopg2
import classwork

def mainMenu():
      
            #we could also query db for the users role and display options based on that?
            print("Welcome to the ERP DBMS!\n\nMain Menu")
            username = input("Please enter your username: ")
            passwrd = input("Please enter your password: ")
            employeeid = input("What is your employee id: ")
            conn1 = psycopg2.connect(user = 'idcheck',
                                    password = 'gettheid3',
                                    host = '127.0.0.1',
                                    port = 5432,
                                    database = 'postgres')
            #call one of the following menus after verifying login info
            #call permisionCheck() to then call correspodning menu
            classConnect = classwork.Connection()
            classConnect.loginid = classConnect.getMaxID(conn1,'login','loginid')+1
            conn = classConnect.loginIn(username, passwrd,employeeid)
            role = classConnect.roleCheck(conn)
            try:
                  if role == "admins" or role=="postgres":
                        admin_menu(classConnect, conn,employeeid)
                  elif role == "engineer":
                        engineer_menu(classConnect, conn,employeeid)
                  elif role == "sales":
                        sales_menu(classConnect, conn,employeeid)
                  elif role == "hr":
                        hr_menu(classConnect, conn,employeeid)
                  else:
                        print("if you're reading this, something went wrong, check 'mainMenu()' in dbtest.py") 
            except KeyboardInterrupt:
                  classConnect.loginOut(conn)


def admin_menu(classConnect, conn,employeeid):
      try:
            goBack = True
            while goBack == True:
                  valid_input = False
                  valid_input1 = False
                  print("Select a menu (number): \n")
                  while valid_input == False: #loop until valid response
                        option = input("1. Users \n2. Tables \n3. Reports \n4. View Employees\n5. Quit\n") #prompt user for option
                        if option == "1":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create user\n2. Update user\n3. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.newUser(conn)
                                    elif option1 == "2": #this is also for granting access to other users
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.updateUser(conn)
                                    elif option1 == "3": #break out of current while loop and go to the first while loop
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "2":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create table\n2. Update table\n3. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.newTable(conn)
                                    elif option1 == "2":
                                          valid_input1 == True
                                          goBack = False
                                          classConnect.updateTable(conn)
                                    elif option1 == "3":#break out of current while loop and go to the first while loop
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "3":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create report\n2. View report\n3. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.createReport(conn)
                                    elif option1 == "2":
                                          valid_input1 == True
                                          goBack = False
                                          classConnect.viewReport(conn)
                                    elif option1 == "3":#break out of current while loop and go to the first while loop
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "4":
                              valid_input = True
                              classConnect.employeeInfo(conn,classConnect.roleCheck(conn))
                        elif option == "5":
                              print("Logging out...")
                              classConnect.loginOut(conn)
                              return
                        else:
                              print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn)

def engineer_menu(classConnect, conn,employeeid):
      try:
            goBack = True
            while goBack == True:
                  valid_input = False
                  valid_input1 = False
                  print("Select a menu (number): \n")
                  while valid_input == False: #loop until valid response
                        option = input("1. Models\n2. Inventory\n3. Employee Infromation\n4. Quit\n") #prompt user for option
                        if option == "1":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create model\n2. View models\n3. Update model\n4. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.newDesign(conn)
                                    elif option1 == "2":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.viewInventory(conn)
                                    elif option1 == "3":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.updateModel(conn)
                                    elif option1 == "4":
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "2":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Add model to inventory\n2. Delete model from inventory\n3. View inventory\n4. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.newModel(conn)
                                    elif option1 == "2":
                                          valid_input1 == True
                                          goBack = False
                                          classConnect.deleteModel(conn)
                                    elif option1 == "3":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.viewInventory(conn)
                                    elif option1 == "4":
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "3":
                              valid_input = True
                              classConnect.employeeInfo(conn, classConnect.roleCheck(conn))
                        elif option == "4":
                              print("Logging out...")
                              classConnect.loginOut(conn)
                              return
                        else:
                              print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn)

def sales_menu(classConnect, conn,employeeid):
      try:
            goBack = True
            while goBack == True:
                  valid_input = False
                  valid_input1 = False
                  print("Select a menu (number): \n")
                  while valid_input == False: #loop until valid response
                        option = input("1. Customers\n2. Orders\n3. Reports\n4. Quit\n") #prompt user for option
                        if option == "1":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create customer\n2. Update customer\n3. View Customers\n4. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          classConnect.newCustomer(conn)
                                    elif option1 == "2":
                                          valid_input1 = True
                                          classConnect.updateCustomer(conn)
                                    elif option1 == "3":
                                          valid_input1 = True
                                          classConnect.viewCustomers(conn)
                                    elif option1 == "4":
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "2":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Create order\n2. Update order\n3. Delete order\n4. View Orders\n5. Return to previous menu\n") #prompt user for option
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
                                    elif option1 == "5":
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "3":
                              valid_input = True
                              classConnect.viewReport(conn)
                        elif option == "4":
                              print("Logging out...")
                              classConnect.loginOut(conn)
                              return
                        else:
                              print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn)

def hr_menu(classConnect, conn,employeeid):
      try:
            goBack = True
            while goBack == True:
                  valid_input = False
                  valid_input1 = False
                  print("Select a menu (number): \n")
                  while valid_input == False: #loop until valid response
                        option = input("1. Employee information\n2. idk\n3. Quit\n") #prompt user for option
                        if option == "1":
                              valid_input = True
                              print("Select an option (number): \n")
                              while valid_input1 == False: #loop until valid response
                                    option1 = input("1. Update employee\n2. View employees\n3. Return to previous menu\n") #prompt user for option
                                    if option1 == "1":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.updateUser(conn)
                                    elif option1 == "2":
                                          valid_input1 = True
                                          goBack = False
                                          classConnect.employeeInfo(conn,classConnect.roleCheck(conn))
                                    elif option1 == "3":
                                          valid_input = False
                                          break
                                    else:
                                          print("Please choose a valid option \n")
                        elif option == "2":
                              valid_input = True
                              print("working on this") #idk
                        elif option == "3":
                              print("Logging out...")
                              classConnect.loginOut(conn)
                              return
                        else:
                              print("Please choose a valid menu: \n")
      except KeyboardInterrupt:
                  classConnect.loginOut(conn)              

mainMenu()