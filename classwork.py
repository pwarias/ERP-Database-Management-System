import psycopg2
class Connection:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(user = "postgres",
                                        password = "Yaysql37",
                                        host = "127.0.0.1",
                                        port = "8080",
                                        database = "cs425db")
            self.cursor = self.conn.cursor()
        except(Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)

    def newUser(self,usrName,Pasword):
        return

    def newCustomer(self,fn,ln,orderNumber):
        return

    def newModel(self,modelNumber,itemCost,orderNumber):
        return

    def newDesign(self,employeeID,modelNumber,itemCost):
        return

    def newEmployee(self,employeeID,fn,ln,ssNumber,paytype,jobtype):
        return

    def closeConnection(self):
        if(self.conn):
            self.cursor.close()
            self.conn.close()
            print("PostgeSQL connection is closed")

try:
    conTest = Connection()

finally:
    if(conTest):
        conTest.cursor.close()
        conTest.conn.close()
        print("PostgeSQL connection is closed")