from connection import *
def DelProd(id):   
    mycursor = mydb.cursor()
    sql = "Delete from Product where id = %s" % id 
    mycursor.execute(sql)
    mycursor.execute("Commit;")