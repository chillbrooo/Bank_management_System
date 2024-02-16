from create import insert
from read import read
from update import update
from delete import delete

obj = insert()

objread = read()

objupdate = update()

objdelete = delete()

print("------------- Bank Management System ---------------")
print("For Inserting the data press 1 : ")
print("For Reading the data press 2 : ")
print("For Updating the data press 3 : ")
print("For Deleting the data press 4 : ")

opr = int(input("Please enter your operation: "))

def myopr():
    print("---- For Personal information press 1 ----")
    print("---- For Bank details press 2 ------------")
    print("---- For transaction details press 3 -----")
    print("---- For Account details press 4 ---------")
    vr = int(input("Please Select your table : "))
    if vr == 1:
        return 'personal_details'
    elif vr ==2:
        return 'bank_details'
    elif vr ==3:
        return 'transaction_details'
    elif vr ==4:
        return 'account_details'
    

if opr ==1:
    h = myopr() 
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)
    elif h=='bank_details':
        acn = int(input("please enter account number:"))
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)

    elif h=='transaction_details':
        tid = int(input("please enter transaction ID:"))
        senacc = int(input("please enter the sender acount number:"))
        recacc = int(input("please enter the reciever's account:"))
        amt = int(input("please enter the amount:"))
        mthd = input("Please enter yhe payment method:")
        obj.transaction_details(tid,senacc,recacc,amt,mthd)

    elif h=='account_details':
        accno = int(input("Please enter account number:"))
        tid = int(input("Please enter transaction Id:"))
        amt = int(input("Please enetr the amount:"))
        clsbl = int(input("Please enter the closing balance:"))
        obj.account_details(accno,tid,amt,clsbl)


if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data: "))
    objread.specific_info(cusid,j)

if opr==3: #user wanted to update the data
    j = myopr()
    cusid = int(input("Please enter the Customer id to update data: "))
    colname = input("Please enter the column name: ")
    newval = input("Please enter new values: ")
    objupdate.myupdate(j,colname,newval,cusid)

if opr==4:
    j = myopr()
    cusid = int(input("please enter the customerID to delete the data: "))
    objdelete.specific_delete(j,cusid)
