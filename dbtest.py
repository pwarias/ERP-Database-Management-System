import psycopg2
def test():
      permissionCheck()

def mainMenu():
      #we could also query db for the users role and display options based on that?
      print("Main Menu")
      print("select a user type:")
      print("1. Sales")
      print("2. HR")
      print("3. Engineering")
      print("4. Admin")
      print("5. exit")
      selection=input("select a user type: ")   
      if(selection==1):
            print("Here is a list of Sales options")
      elif(selection==2):
            print("Here is a list of HR options")
      elif(selection==3):
            print("Here is a list of Engineering options")
      elif(selection==4):
            print("Here is a list of Admin options")
      else:
            print("Exiting...")

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