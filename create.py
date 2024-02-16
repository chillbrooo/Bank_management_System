import mysql.connector

#creating connection 

class insert:
        def __init__(self):
                self.conn = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "Abhishek@123",
                        database = "bank"
                        )
        def personal_details(self,cid,fname,lname,addr,pn,an,pan):
                cur = self.conn.cursor() # creating cursor
                cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
                self.conn.commit()      
                print("--------------------Personal information has been saved successfully:------------------------")

        def bank_details(self,acn,cid,ifsc,actype):
                cur = self.conn.cursor() #creating cursur
                cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
                self.conn.commit()
                print("------------------Bank details has been sucessfully saved-----------------------")

        def transaction_details(self,tid,senacc,recacc,amt,mthd):
                cur = self.conn.cursor() #creating cursor
                cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({tid},{senacc},{recacc},{amt},'{mthd}')")
                self.conn.commit()
                print("---------------Transactional details has been saved successfully-------------")

        def account_details(self,accno,tid,amt,clsbl):
                cur = self.conn.cursor()
                cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({accno},{tid},{amt},{clsbl})")
                self.conn.commit()
                print("----------------Account details have been saved successfully---------------")
