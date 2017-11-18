'''
Created on Jun 3, 2016

@author: Ebin
'''

#!/usr/bin/python

import MySQLdb

# create connection to database inventory
db = MySQLdb.connect("localhost","root","password","inventory" )
db.set_character_set('utf8')

db_name = "inventory"
db_table_name = "server_inventory"


query_create_table = " CREATE TABLE " + db_table_name + "( HOSTNAME VARCHAR(32),\
DC_LOCATION  VARCHAR(10), PHYSICAL_Localtion VARCHAR(40) ) "


print "Test"
cursor = db.cursor()
cursor.execute ("show databases")
response = cursor.fetchall()

for i in response:
    print i
    
cursor.execute("use inventory")
#cursor.execute("drop table " + db_table_name )
cursor.execute (query_create_table)

cursor.execute("show tables")
servertable = cursor.fetchall()

#print "test2"

for i in servertable:
    print i[0]
    
  
  






