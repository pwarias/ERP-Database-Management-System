import classwork
import psycopg2

hello = classwork.Connection()
print("after hello hello")
conn = hello.loginIn('postges','Yaysql37')
hello.loginOut(conn)
exit(0)