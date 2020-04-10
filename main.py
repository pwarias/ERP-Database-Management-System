#Abdallah Abdeljamil, Przemyslaw Warias, Andrew Woltman

import pypyodbc as pyodbc

cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for PostgreSQL};Server=localhost; \
    Port=8080;Database=postgres;User ID=postgres;Password=Yaysql37;String Types=Unicode')

cursor = cnxn.cursor()
cursor.execute("INSERT INTO Model (modelNumber, modelName) VALUES (12345, 'dildo')") 
