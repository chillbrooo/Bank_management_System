import mysql.connector

#creating connection 

class delete:
        def __init__(self):
                self.conn = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "Abhishek@123",
                        database = "bank"
                        )
        
        def specific_delete(self,table_name,cusid):
                cur = self.conn.cursor()
                cur.execute(f"delete from {table_name} where customerID={cusid}")
                self.conn.commit()
                print("-----------Data has been deleted Successfully----------")