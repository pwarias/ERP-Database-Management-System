import psycopg2
import classwork
def test():
      permissionCheck()

def mainMenu():
      #we could also query db for the users role and display options based on that?
      print("Main Menu")
      username = input("Please enter your username: ")
      print("\n")
      password = input("Please enter your password: ") #very safe and secure xd
      
      #call one of the following menus after verifying login info
      #call permisionCheck() to then call correspodning menu
      creatingCon=classwork.Connection()
      conn=creatingCon.loginIn(username, password)



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
                              #prompt user for user specifics
                              #call function to create user
                        elif option1 == 2: #this is also for granting access to other users
                              valid_input1 == True
                              #prompt user for specifics
                              #call function to update user
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create table \n 2. Update table \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              #prompt user for table specifics
                              #call function to create table
                        elif option1 == 2:
                              valid_input1 == True
                              #prompt user for specifics
                              #call function to update table
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create report \n 2. View report \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              #prompt user for report specifics
                              #call function to create report
                        elif option1 == 2:
                              valid_input1 == True
                              #prompt user for specifics
                              #call function to view report
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
                              #prompt user for model specifics
                              #call function to create model
                        elif option1 == 2:
                              valid_input1 = True
                              #call function to view Model table
                        elif option1 == 3:
                              valid_input1 = True
                              #Prompt user what they want to change
                              #call function to update Model
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Add model to inventory \n 2. Delete model from inventory \n 3. View inventory \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              #prompt user for model to add
                              #call function to add model to inventory
                        elif option1 == 2:
                              valid_input1 == True
                              #prompt user for model to delete
                              #call function to delete model from inventory
                        elif option1 == 3:
                              valid_input1 = True
                              #call function to view inventory table
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  #call function to view employee information
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
                              #prompt user for customer specifics
                              #call function to create customer
                        elif option1 == 2:
                              valid_input1 = True
                              #prompt user for customer specifics
                              #call function to update customer
                        elif option1 == 3:
                              valid_input1 = True
                              #call function to view customer table
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  print("Select an option (number): \n")
                  while valid_input1 == False: #loop until valid response
                        option1 = input("1. Create order \n 2. Update order \n 3. View Orders \n") #prompt user for option
                        if option1 == 1:
                              valid_input1 = True
                              #prompt user for order specifics
                              #call function to create order
                        elif option1 == 2:
                              valid_input1 == True
                              #prompt user for order specifics
                              #call function to update order
                        elif option1 == 3:
                              valid_input1 = True
                              #call function to view order table
                        else:
                              print("Please choose a valid option \n")
            elif option == 3:
                  valid_input = True
                  #call function to view reports
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
                              #prompt user for employee specifics
                              #call function to update employee
                        elif option1 == 2:
                              valid_input1 = True
                              #call function to view employee table
                        else:
                              print("Please choose a valid option \n")
            elif option == 2:
                  valid_input = True
                  #idk
            else:
                  print("Please choose a valid menu: \n")
                  
def main():
      username=input("welcome to our web app to connect to the database please enter a username: ")
      password=input("please enter your password: ")

      try:
            conn = psycopg2.connect(database="test", user = username, password = password, host = "localhost", port = "5432")
      except:
            print("could not connect")
            exit()


      print("Opened database successfully")
      mainMenu()
      cur = conn.cursor()
      '''
      cur.execute(CREATE TABLE COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);) add triple quotes
      print("Table created successfully")
      '''

      conn.commit()
      conn.close()




def permissionCheck():
      conn = psycopg2.connect(database="postgres", user = "postgres", password = "Yaysql37", host = "localhost", port = "5432")
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
      print(roleType) #all roles including inherited types, excludes name

      #assume that emplyees can't have more than one role (not including inherited)
      print(roleType[len(roleType)-1]) #the last role will contain the actual role of the user


      conn.commit()
      conn.close()

test()