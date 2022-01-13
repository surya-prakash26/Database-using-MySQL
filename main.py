<<<<<<< HEAD
import mysql.connector as c
con = c.connect(host="localhost", user="root", passwd="", database="company")
if con.is_connected():
    print("sucessfully connected")
cursor = con.cursor()

def employee():
    def insert():
        SSN = int(input("Enter Employee ID: "))
        Fname = input("First Name: ")
        Lname = input("Last Name: ")
        Address = input("Address: ")
        phone = input("phone: ")
        salary = int(input("Enter Salary: "))
        Dnumber = int(input("Enter Department No: "))
        query = "insert into employee values ({},'{}','{}','{}','{}',{},{})".format(SSN,Fname,Lname,Address,phone,salary,Dnumber)
        cursor.execute(query)
        con.commit()
        print("Data Inserted Sucessfully")

    def update():
        def update_salary():
            SSN = int(input("Enter Employee ID: "))
            salary = int(input("Enter Salary: "))
            query = "update employee set salary = {} where SSN={}".format(salary,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("salary of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")
        def update_phone():
            SSN = int(input("Enter Employee ID: "))
            phone = input("Enter New phone no.: ")
            query = "update employee set phone = '{}' where SSN={}".format(phone,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Phone no. of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        def update_Deptno():
            SSN = int(input("Enter Employee ID: "))
            Dnumber = int(input("Enter New Dept no.: "))
            query = "update employee set Dnumber = {} where SSN={}".format(Dnumber,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Dept no. of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        def update_Address():
            SSN = int(input("Enter Employee ID: "))
            Address = input("Enter New Address: ")
            query = "update employee set Address = '{}' where SSN={}".format(Address,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Address of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        print("Updating Employee Details.")
        while True:
            n = int(input("1:Update Salary 2:Update Phone no. 3:Dept no. 4:Address 5:Exit\nEnter Choice: "))
            if n == 1:
                update_salary()
            elif n ==2:
                update_phone()
            elif n ==3:
                update_Deptno()
            elif n == 4:
                update_Address()
            elif n ==5:
                break
            else:
                print("Enter a valid number")
    def delete():
        SSN = int(input("Enter Employee ID: "))
        query = "Delete from employee where SSN={}".format(SSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted employee ID = {} Sucessfully".format(SSN))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif n ==4:
            break
        else:
            print("Enter valid number")
def department():
    def insert():
        dno = input("Department Number: ")
        dname = input("Department Name: ")
        budget = input("Budget: ")
        query = "insert into department values ({},'{}',{})".format(dno,dname,budget)
        cursor.execute(query)
        con.commit()
        print("Data Inserted Sucessfully")
    def delete():
        dno = int(input("Enter department Number: "))
        query = "Delete from department where dno={}".format(dno)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted department number {} Sucessfully".format(dno))
        else:
            print("No Data Found")
    def update():
        def update_dept_name():
            dno = int(input("Enter department No. : "))
            dname = input("Enter New dept Name: ")
            query = "update department set dname = '{}' where dno={}".format(dname,dno)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("department Name of {} Updated Sucessfully".format(dno))
            else:
                print("No Data Found")
        def update_budget():
            dno = int(input("Enter department No. : "))
            budget = int(input("Enter New budget: "))
            query = "update department set budget = {} where dno={}".format(budget,dno)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("budget of {} Updated Sucessfully".format(dno))
            else:
                print("No Data Found")

        print("Updating department Details.")

        while True:
            n = int(input("1:Update department Name 2:Update budget 3:Exit\nEnter Choice: "))
            if n == 1:
                update_dept_name()
            elif n ==2:
                update_budget()
            elif n ==3:
                break
            else:
                print("Enter a valid number")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")

def work_in():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Dnumber = input("Department Number: ")
        From_ = input("Date of Joining: ")
        To_ = input("Date of Leaving: ")
        working_hrs = input("No. Of Hrs/Day: ")
        query = "insert into work_in values ({},{},'{}','{}','{}')".format(ESSN,Dnumber,From_,To_,working_hrs)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID: "))
        query = "Delete from work_in where ESSN={}".format(ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted employee ID = {} Sucessfully".format(ESSN))
        else:
            print("No Data Found")
    def update():
        def update_dept_no():
            ESSN = int(input("Enter Employee ID: "))
            Dnumber = int(input("Enter New department No. : "))
            query = "update work_in set Dnumber = {} where ESSN={}".format(Dnumber,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("department Number of {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        def update_dateOfjoining():
            ESSN = int(input("Enter Employee ID: "))
            From_ = input("Enter Date of Joining : ")
            query = "update work_in set From_ = '{}' where ESSN={}".format(From_,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Date of Joining  {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        def update_dateOfleaving():
            ESSN = int(input("Enter Employee ID: "))
            To_ = input("Enter Date of Leaving  : ")
            query = "update work_in set To_ = '{}' where ESSN={}".format(To_,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Date of Leaving  {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        print("Updating Work Details.")

        while True:
            n = int(input("1:Update department Name 2:Update dateOfjoining 3: update dateOfleaving 4:Exit\nEnter Choice: "))
            if n == 1:
                update_dept_no()
            elif n ==2:
                update_dateOfjoining()
            elif n ==3:
                update_dateOfleaving()
            elif n ==4:
                break
            else:
                print("Enter a valid number")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")
def manages():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Dnumber = input("Department Number: ")
        query = "insert into manages values ({},{})".format(Dnumber,ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID to Delete: "))
        query = "delete from manages where ESSN={}".format(ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Deleted Sucessfully")
        else:
            print("No Data Found")
    def update():
        Dnumber = int(input("Enter department No. : "))
        ESSN = int(input("Enter New Manager ID: "))
        query = "update manages set ESSN = {} where Dnumber={}".format(ESSN,Dnumber)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Manager of Department {} Updated Sucessfully".format(Dnumber))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")
def children():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Fname = input("Enter First Name: ")
        Lname = input("Enter Last Name: ")
        age = int(input("Enter age: "))
        relationship  = input("Enter son/daughter/other: ")

        query = "insert into children values ({},'{}','{}',{},'{}')".format(ESSN,Fname,Lname,age,relationship)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID to Delete: "))
        Lname = input("Enter Child Name: ")
        query = "delete from children where ESSN={} and Lname='{}'".format(ESSN,Lname)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Deleted Sucessfully")
        else:
            print("No Data Found")
    def update():
        ESSN = int(input("Enter Employee ID: "))
        Lname = input("Enter child Name: ")
        age = int(input("Enter current age: "))
        query = "update children set age = {} where ESSN={} and Lname='{}'".format(age,ESSN,Lname)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Manager of Department {} Updated Sucessfully".format(ESSN))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")


if __name__ == '__main__': 

    print("Enter choice: ")
    while True:
        n = int(input("1:Employee 2:Department 3:Work In 4:Manages 5:Children 6:Exit "))
        if n == 1:
            employee()
        elif n ==2:
            department()
        elif n ==3:
            work_in()
        elif n == 4:
            manages()
        elif n == 5:
            children()
        elif n == 6:
            break
=======
import mysql.connector as c
con = c.connect(host="localhost", user="root", passwd="", database="company")
if con.is_connected():
    print("sucessfully connected")
cursor = con.cursor()

def employee():
    def insert():
        SSN = int(input("Enter Employee ID: "))
        Fname = input("First Name: ")
        Lname = input("Last Name: ")
        Address = input("Address: ")
        phone = input("phone: ")
        salary = int(input("Enter Salary: "))
        Dnumber = int(input("Enter Department No: "))
        query = "insert into employee values ({},'{}','{}','{}','{}',{},{})".format(SSN,Fname,Lname,Address,phone,salary,Dnumber)
        cursor.execute(query)
        con.commit()
        print("Data Inserted Sucessfully")

    def update():
        def update_salary():
            SSN = int(input("Enter Employee ID: "))
            salary = int(input("Enter Salary: "))
            query = "update employee set salary = {} where SSN={}".format(salary,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("salary of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")
        def update_phone():
            SSN = int(input("Enter Employee ID: "))
            phone = input("Enter New phone no.: ")
            query = "update employee set phone = '{}' where SSN={}".format(phone,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Phone no. of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        def update_Deptno():
            SSN = int(input("Enter Employee ID: "))
            Dnumber = int(input("Enter New Dept no.: "))
            query = "update employee set Dnumber = {} where SSN={}".format(Dnumber,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Dept no. of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        def update_Address():
            SSN = int(input("Enter Employee ID: "))
            Address = input("Enter New Address: ")
            query = "update employee set Address = '{}' where SSN={}".format(Address,SSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Address of {} Updated Sucessfully".format(SSN))
            else:
                print("No Data Found")            
        print("Updating Employee Details.")
        while True:
            n = int(input("1:Update Salary 2:Update Phone no. 3:Dept no. 4:Address 5:Exit\nEnter Choice: "))
            if n == 1:
                update_salary()
            elif n ==2:
                update_phone()
            elif n ==3:
                update_Deptno()
            elif n == 4:
                update_Address()
            elif n ==5:
                break
            else:
                print("Enter a valid number")
    def delete():
        SSN = int(input("Enter Employee ID: "))
        query = "Delete from employee where SSN={}".format(SSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted employee ID = {} Sucessfully".format(SSN))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif n ==4:
            break
        else:
            print("Enter valid number")
def department():
    def insert():
        dno = input("Department Number: ")
        dname = input("Department Name: ")
        budget = input("Budget: ")
        query = "insert into department values ({},'{}',{})".format(dno,dname,budget)
        cursor.execute(query)
        con.commit()
        print("Data Inserted Sucessfully")
    def delete():
        dno = int(input("Enter department Number: "))
        query = "Delete from department where dno={}".format(dno)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted department number {} Sucessfully".format(dno))
        else:
            print("No Data Found")
    def update():
        def update_dept_name():
            dno = int(input("Enter department No. : "))
            dname = input("Enter New dept Name: ")
            query = "update department set dname = '{}' where dno={}".format(dname,dno)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("department Name of {} Updated Sucessfully".format(dno))
            else:
                print("No Data Found")
        def update_budget():
            dno = int(input("Enter department No. : "))
            budget = int(input("Enter New budget: "))
            query = "update department set budget = {} where dno={}".format(budget,dno)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("budget of {} Updated Sucessfully".format(dno))
            else:
                print("No Data Found")

        print("Updating department Details.")

        while True:
            n = int(input("1:Update department Name 2:Update budget 3:Exit\nEnter Choice: "))
            if n == 1:
                update_dept_name()
            elif n ==2:
                update_budget()
            elif n ==3:
                break
            else:
                print("Enter a valid number")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")

def work_in():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Dnumber = input("Department Number: ")
        From_ = input("Date of Joining: ")
        To_ = input("Date of Leaving: ")
        working_hrs = input("No. Of Hrs/Day: ")
        query = "insert into work_in values ({},{},'{}','{}','{}')".format(ESSN,Dnumber,From_,To_,working_hrs)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID: "))
        query = "Delete from work_in where ESSN={}".format(ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Deleted employee ID = {} Sucessfully".format(ESSN))
        else:
            print("No Data Found")
    def update():
        def update_dept_no():
            ESSN = int(input("Enter Employee ID: "))
            Dnumber = int(input("Enter New department No. : "))
            query = "update work_in set Dnumber = {} where ESSN={}".format(Dnumber,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("department Number of {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        def update_dateOfjoining():
            ESSN = int(input("Enter Employee ID: "))
            From_ = input("Enter Date of Joining : ")
            query = "update work_in set From_ = '{}' where ESSN={}".format(From_,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Date of Joining  {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        def update_dateOfleaving():
            ESSN = int(input("Enter Employee ID: "))
            To_ = input("Enter Date of Leaving  : ")
            query = "update work_in set To_ = '{}' where ESSN={}".format(To_,ESSN)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Date of Leaving  {} Updated Sucessfully".format(ESSN))
            else:
                print("No Data Found")
        print("Updating Work Details.")

        while True:
            n = int(input("1:Update department Name 2:Update dateOfjoining 3: update dateOfleaving 4:Exit\nEnter Choice: "))
            if n == 1:
                update_dept_no()
            elif n ==2:
                update_dateOfjoining()
            elif n ==3:
                update_dateOfleaving()
            elif n ==4:
                break
            else:
                print("Enter a valid number")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")
def manages():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Dnumber = input("Department Number: ")
        query = "insert into manages values ({},{})".format(Dnumber,ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID to Delete: "))
        query = "delete from manages where ESSN={}".format(ESSN)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Deleted Sucessfully")
        else:
            print("No Data Found")
    def update():
        Dnumber = int(input("Enter department No. : "))
        ESSN = int(input("Enter New Manager ID: "))
        query = "update manages set ESSN = {} where Dnumber={}".format(ESSN,Dnumber)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Manager of Department {} Updated Sucessfully".format(Dnumber))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")
def children():
    def insert():
        ESSN = int(input("Enter Employee ID: "))
        Fname = input("Enter First Name: ")
        Lname = input("Enter Last Name: ")
        age = int(input("Enter age: "))
        relationship  = input("Enter son/daughter/other: ")

        query = "insert into children values ({},'{}','{}',{},'{}')".format(ESSN,Fname,Lname,age,relationship)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Inserted Sucessfully")
        else:
            print("No Data Found")
    def delete():
        ESSN = int(input("Enter Employee ID to Delete: "))
        Lname = input("Enter Child Name: ")
        query = "delete from children where ESSN={} and Lname='{}'".format(ESSN,Lname)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Data Deleted Sucessfully")
        else:
            print("No Data Found")
    def update():
        ESSN = int(input("Enter Employee ID: "))
        Lname = input("Enter child Name: ")
        age = int(input("Enter current age: "))
        query = "update children set age = {} where ESSN={} and Lname='{}'".format(age,ESSN,Lname)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount>0:
            print("Manager of Department {} Updated Sucessfully".format(ESSN))
        else:
            print("No Data Found")
    while True:
        a = int(input("1:insert 2:Update 3:Delete 4:Exit "))
        if a == 1:
            insert()
        elif a == 2:
            update()
        elif a == 3:
            delete()
        elif a ==4:
            break
        else:
            print("Enter valid number")


if __name__ == '__main__': 

    print("Enter choice: ")
    while True:
        n = int(input("1:Employee 2:Department 3:Work In 4:Manages 5:Children 6:Exit "))
        if n == 1:
            employee()
        elif n ==2:
            department()
        elif n ==3:
            work_in()
        elif n == 4:
            manages()
        elif n == 5:
            children()
        elif n == 6:
            break
>>>>>>> c2f27f2e1cfa51c1716c79b127f27615f995f747
        