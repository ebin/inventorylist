'''
Created on Jun 3, 2016

@author: Ebin
'''

#!/usr/bin/python

import MySQLdb
db_name = "inventory"
db_table_name = "server_inventory"

# create connection to database inventory
db = MySQLdb.connect("localhost","root","password","inventory" )
dbc = db.cursor() 

dbc.execute ("show databases")
result = dbc.fetchall()

#for i in result:
#    print i[0] 

print " ************** "
dbc.execute("use inventory")
dbc.execute( "show columns from server_inventory")
result2 = dbc.fetchall()
for i in result2:
    print i[0]

#dbc.execute( "select HOSTNAME,SERVER_FUNCTION,PRIMARYIPADDRESS from server_inventory where DC_LOCATION LIKE 'Singapore' ")
dbc.execute( "select HOSTNAME,PRIMARYIPADDRESS from server_inventory where DC_LOCATION LIKE 'Singapore' ")
result1 = dbc.fetchall()

#for i in result1:
#    print i[0] + " " + i[2] + "  " + i[1]




 
