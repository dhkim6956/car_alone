import mysql.connector

db = mysql.connector.connect(host='52.79.105.4', user='rccar', password='1', database='senseDB', auth_plugin='mysql_native_password')
cur = db.cursor()

#query
cur.execute("select * from command")

#print
for (id, time, cmd_string, arg_string, is_finish) in cur:
    print(id, time, cmd_string, arg_string, is_finish)

cur.close()
db.close()