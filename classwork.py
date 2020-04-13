import psycopg2
class connection:
    def __init__():
        try:
    conn = psycopg2.connect(user = "postgres",
                                  password = "Yaysql37",
                                  host = "127.0.0.1",
                                  port = "8080",
                                  database = "cs425db")
    cursor = conn.cursor()

    def newUser(usrName,Pasword):
        return
    def newCustomer(fn,ln,orderNumber):
        return
    def newModel(modelNumber,itemCost,orderNumber):
        return
    def newDesign(employeeID,modelNumber,itemCost):
        return
    def newEmployee(employeeID,fn,ln,ssNumber,paytype,jobtype):
        return

 
try:
    conn = psycopg2.connect(user = "sysadmin",
                                  password = "",
                                  host = "127.0.0.1",
                                  port = "8080",
                                  database = "postgres_db")
    cursor = conn.cursor()
    print(connection.get_dsn_parameters(),"\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except(Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        conn.close()
        print("PostgeSQL connection is closed")