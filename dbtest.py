import psycopg2;
from classwork import *;

def mainMenu():
      #we could also query db for the users role and display options based on that?
      no_connection = True
      print("Welcome to the ERP DBMS! \n Main Menu \n")
      username = input("Please enter your username: ")
      print("\n")
      passwrd = input("Please enter your password: ") #very safe and secure xd

      conn = classwork.loginIn(username, passwrd)

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
      
      role = roleCheck(conn)

      if role == "admins":
            admin_menu()
      elif role == "engineer":
            engineer_menu()
      elif role == "sales":
            sales_menu()
      elif role == "hr":
            hr_menu()
      else:
           print("if you're reading this, something went wrong, check 'mainMenu()' in dbtest.py") 


def admin_menu():
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Users \n 2. Tables \n 3. Reports \n") #prompt user for option
            if option == 1:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create user \n 2. Update user \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.newUser()
                        elif option1 == 2: #this is also for granting access to other users
                              valid_input1 == True
                              classwork.updateUser()
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create table \n 2. Update table \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.newTable()
                        elif option1 == 2:
                              valid_input1 == True
                              classwork.updateTable()
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create report \n 2. View report \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.createReport()
                        elif option1 == 2:
                              valid_input1 == True
                              classwork.viewReport()
                        else:
                              print("Please choose a valid option \n")
            else:
                  print("Please choose a valid menu: \n")

def engineer_menu():
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Models \n 2. Inventory \n 3. Employee Infromation \n") #prompt user for option
            if option == 1:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create model \n 2. View models \n 3. Update model \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.newDesign()
                        elif option1 == 2:
                              valid_input1 = True
                              classwork.viewInventory()
                        elif option1 == 3:
                              valid_input1 = True
                              classwork.updateModel()
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Add model to inventory \n 2. Delete model from inventory \n 3. View inventory \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.newModel()
                        elif option1 == 2:
                              valid_input1 == True
                              classwork.deleteModel()
                        elif option1 == 3:
                              valid_input1 = True
                              classwork.viewInventory()
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  classwork.employeeInfo()
            else:
                  print("Please choose a valid menu: \n")

def sales_menu():
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Customers \n 2. Orders \n 3. Reports \n") #prompt user for option
            if option == 1:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create customer \n 2. Update customer \n 3. View Customers \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.newCustomer()
                        elif option1 == 2:
                              valid_input1 = True
                              classwork.updateCustomer()
                        elif option1 == 3:
                              valid_input1 = True
                              classwork.viewCustomers()
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create order \n 2. Update order \n 3. View Orders \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.createOrder()
                        elif option1 == 2:
                              valid_input1 == True
                              classwork.updateOrder()
                        elif option1 == 3:
                              valid_input1 = True
                              classwork.viewOrders()
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  classwork.viewReport()
            else:
                  print("Please choose a valid menu: \n")

def hr_menu():
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Employee information \n 2. idk \n") #prompt user for option
            if option == 1:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Update employee \n 2. View employees \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              classwork.updateUser()
                        elif option1 == 2:
                              valid_input1 = True
                              classwork.viewUsers()
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  #idk
            else:
                  print("Please choose a valid menu: \n")              


def roleCheck(psycopg2 conn):
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
      conn.close()