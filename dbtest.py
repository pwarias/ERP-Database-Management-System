import psycopg2
import classwork

connection1 = classwork.Connection()

print("Welcome to the ERP DBMS! \n Main Menu \n")
username = input("Please enter your username: ")
print("\n")
passwrd = input("Please enter your password: ") #very safe and secure xd

conn = connection1.loginIn(username, passwrd)

def mainMenu():
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
            print(role)


def admin_menu():
      valid_input = False
      valid_input1 = False
      print("Select a menu (number): \n")
      while valid_input == False: #loop until valid response
            option = input("1. Users \n 2. Tables \n 3. Reports \n") #prompt user for option
            if option == "1":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create user \n 2. Update user \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              connection1.newUser(conn)
                        elif option1 == "2": #this is also for granting access to other users
                              valid_input1 == True
                              connection1.updateUser(conn)
                        else:
                              print("Please choose a valid option \n")
            elif option == "2":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create table \n 2. Update table \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              connection1.newTable(conn)
                        elif option1 == "2":
                              valid_input1 == True
                              connection1.updateTable(conn)
                        else:
                              print("Please choose a valid option \n")
            elif option == "3":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create report \n 2. View report \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              classwork.Connection.createReport()
                        elif option1 == "2":
                              valid_input1 == True
                              classwork.Connection.viewReport()
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
            if option == "1":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create model \n 2. View models \n 3. Update model \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              classwork.Connection.newDesign()
                        elif option1 == "2":
                              valid_input1 = True
                              classwork.Connection.viewInventory()
                        elif option1 == "3":
                              valid_input1 = True
                              classwork.Connection.updateModel()
                        else:
                              print("Please choose a valid option \n")
            elif option == "2":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Add model to inventory \n 2. Delete model from inventory \n 3. View inventory \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              classwork.Connection.newModel()
                        elif option1 == "2":
                              valid_input1 == True
                              classwork.Connection.deleteModel()
                        elif option1 == "3":
                              valid_input1 = True
                              classwork.Connection.viewInventory()
                        else:
                              print("Please choose a valid option \n")
            elif option == "3":
                  valid_input = True
                  classwork.Connection.employeeInfo()
            else:
                  print("Please choose a valid menu: \n")

def sales_menu():
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
                              classwork.Connection.newCustomer()
                        elif option1 == "2":
                              valid_input1 = True
                              classwork.Connection.updateCustomer()
                        elif option1 == "3":
                              valid_input1 = True
                              classwork.Connection.viewCustomers()
                        else:
                              print("Please choose a valid option \n")
            elif option == "2":
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create order \n 2. Update order \n 3. View Orders \n") #prompt user for option
                        if option1 == "1":
                              valid_input1 = True
                              classwork.Connection.createOrder()
                        elif option1 == "2":
                              valid_input1 == True
                              classwork.Connection.updateOrder()
                        elif option1 == "3":
                              valid_input1 = True
                              classwork.Connection.viewOrders()
                        else:
                              print("Please choose a valid option \n")
            elif option == "3":
                  valid_input = True
                  classwork.Connection.viewReport()
            else:
                  print("Please choose a valid menu: \n")

def hr_menu():
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
                              classwork.Connection.updateUser()
                        elif option1 == "2":
                              valid_input1 = True
                              classwork.Connection.viewUsers()
                        else:
                              print("Please choose a valid option \n")
            elif option == "2":
                  valid_input = True
                  print("working on this") #idk
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
      conn.close()

mainMenu()