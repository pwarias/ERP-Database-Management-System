import psycopg2
import classwork

def mainMenu():
      #we could also query db for the users role and display options based on that?
      no_connection = True
      print("Welcome to the ERP DBMS! \n Main Menu \n")
      username = input("Please enter your username: ")
      print("\n")
      passwrd = input("Please enter your password: ") #very safe and secure xd

      
      '''
      while no_connection == True:
            username = input("Please enter your username: ")
            print("\n")
            passwrd = input("Please enter your password: ") #very safe and secure xd
            
            try:      
                  conn = psycopg2.connect(database="postgres", user = username, password = passwrd, host = "localhost", port = "5432")
                  no_connection = False
            except:
                  print("Could not connect to databse, please try again.")
                  no_connection = True
      '''
      
      #call one of the following menus after verifying login info
      #call permisionCheck() to then call correspodning menu
      classConnect=classwork.Connection()
      conn=classConnect.loginIn(username, passwrd)

      role = roleCheck(conn)

      if role == "admins":
            admin_menu(classConnect, conn)
      elif role == "engineer":
            engineer_menu(classConnect, conn)
      elif role == "sales":
            sales_menu(classConnect, conn)
      elif role == "hr":
            hr_menu(classConnect, conn)
      else:
           print("if you're reading this, something went wrong, check 'mainMenu()' in dbtest.py") 


def admin_menu(classConnect, conn):
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Users \n2. Tables \n3. Reports \n:") #prompt user for option
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
            else:
                  print("Please choose a valid menu: \n")

def engineer_menu(classConnect, conn):
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
                  classConnect.employeeInfo(conn)
            else:
                  print("Please choose a valid menu: \n")

def sales_menu(classConnect, conn):
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Customers \n 2. Orders \n 3. Reports \n") #prompt user for option
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
                        option1 = input("1. Create order \n 2. Update order \n 3. View Orders \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              classConnect.createOrder(conn)
                        elif option1 == "2":
                              valid_input1 == True
                              classConnect.updateOrder(conn)
                        elif option1 == "3":
                              valid_input1 = True
                              classConnect.viewOrders(conn)
                        else:
                              print("Please choose a valid option \n")
            elif option == "3":
                  valid_input = True
                  classConnect.viewReport(conn)
            else:
                  print("Please choose a valid menu: \n")

def hr_menu(classConnect, conn):
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
                              classConnect.viewUsers(conn)
                        else:
                              print("Please choose a valid option \n")
            elif option == "2":
                  valid_input = True
                  #idk
            else:
                  print("Please choose a valid menu: \n")              


def roleCheck(conn):
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
mainMenu()