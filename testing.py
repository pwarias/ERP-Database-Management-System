import psycopg2

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
