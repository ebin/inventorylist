'''
Created on May 31, 2016

@author: Ebin
'''
''' import MySQLdb and xlrd'''

import MySQLdb
import xlrd

db = MySQLdb.connect("localhost","root","password","inventory" )
cursor = db.cursor()
cursor.execute("use inventory")
db.set_character_set('utf8')

book = xlrd.open_workbook("HW_Inventory_List.xlsx")
sheet = book.sheet_by_name("Inventory")

for r in range(2, sheet.nrows):
    HOSTNAME = sheet.cell(r,0).value
    DC_LOCATION = sheet.cell(r,1).value
    PHYSICAL_Localtion = sheet.cell(r,2).value
    FQDN = sheet.cell(r,3).value
    PRIMARYIPADDRESS = sheet.cell(r,4).value
    VLAN = sheet.cell(r,5).value
        
    DATA_VALUES = (HOSTNAME, DC_LOCATION, PHYSICAL_Localtion, FQDN, PRIMARYIPADDRESS, VLAN )
    
    try:
        cursor.execute("use inventory")
        print "Hostname is " + HOSTNAME + "  "  + PHYSICAL_Localtion 
        INSERT_QUERY  = " INSERT INTO server_inventory  ( HOSTNAME, DC_LOCATION, PHYSICAL_Localtion, FQDN, PRIMARYIPADDRESS, VLAN) VALUES (%s, %s, %s, %s, %s, %s )"
        cursor.execute(INSERT_QUERY, DATA_VALUES)
        db.commit()
    
    except MySQLdb.ProgrammingError:
        print "the following query failed"       
 
print " End "  

cursor.execute(" select * from  server_inventory " )
table_details = cursor.fetchall()

for i in table_details:
    print i[0]  + "   "  + i[1]

db.close()

