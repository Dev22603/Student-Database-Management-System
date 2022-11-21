import mysql.connector
from mysql.connector import Error

def add_student():
    Full_name=input("Full name of Student: ")
    Adm_no=int(input('Admission number: '))
    Roll_no=int(input('Roll number: '))
    Class=int(input('Class: '))
    Attd=float(input("Attendance: "))
    DOB=input("Date of Birth in yyyy/mm/dd format: ")
    Gender=input("Gender (F/M): ")
    Eng=int(input("English marks: "))
    Math=int(input("Math marks: "))
    Comp=int(input("Computer Science marks: "))
    Phy=int(input("Physics marks: "))
    Chem=int(input("Chemistry marks: "))
    Address=input("Address: ")
    City=input("City: ")
    Mobile_no=int(input("Mobile number of parents: "))
    Email_id=input("Email id of student if exists or else Parents' Email id: ")
    Total_percent=(Eng+Math+Comp+Phy+Chem)/5
    
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_data',
                                             user='root',
                                             password='root')


        cursor = connection.cursor()
        st="Create table if not exists RESULT_SCI (Full_name Varchar(20), adm_no Smallint, Roll_no tinyint, Class tinyint, Attd decimal(4,1), Eng tinyint, Math tinyint, Comp tinyint, Phy tinyint, Chem tinyint, Total_percent decimal(5,2), Gender Char(1), Address Varchar(40), DOB date, Mobile_no BIGINT , City varchar(25), email_id varchar(30) )"
        cursor.execute(st)

        query ="INSERT INTO result_sci (Full_name,Adm_no,Roll_no,Class,Attd,Gender,Address,DOB,Mobile_no,City,Email_id,Eng,Math,Comp,Phy,Chem,Total_percent) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vvs = (Full_name,Adm_no,Roll_no,Class,Attd,Gender,Address,DOB,Mobile_no,City,Email_id,Eng,Math,Comp,Phy,Chem,Total_percent)
        cursor.execute(query,vvs)
        connection.commit()
        print('\n',cursor.rowcount, "Record inserted successfully into result_sci table")
        input("\n\nPress Any Key to Continue..........")
    except mysql.connector.Error as error:
        print("\nFailed to insert record into result_sci table {}".format(error))
    
    finally:
        if (connection.is_connected()):
            connection.close()
            #print("MySQL connection is closed")
    

def search():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Student_data',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()

        st="Create table if not exists RESULT_SCI (Full_name Varchar(20), adm_no Smallint, Roll_no tinyint, Class tinyint, Attd decimal(4,1), Eng tinyint, Math tinyint, Comp tinyint, Phy tinyint, Chem tinyint, Total_percent decimal(5,2), Gender Char(1), Address Varchar(40), DOB date, Mobile_no BIGINT , City varchar(25), email_id varchar(30) )"
        cursor.execute(st)
        
        A_no=int(input('Admission number: '))
        sql_select_query = "select * from result_sci where Adm_no=%s"
        A=(A_no,)
        cursor.execute(sql_select_query,A)
        record = cursor.fetchone()
        #print(record)
        nm = 'Name'
        rn = 'Roll_no'
        an = 'Adm. No.'
        cl ='Class'
        at = 'Attendance'
        eng = 'English'
        mat = 'Maths'
        cs = 'Comp. Sci.'
        py = 'Physics'
        ch = 'Chemistry'
        per = 'Percentage'
        ge='Gender'
        ad='Address'
        dob='DOB'
        mn='Mobile No.'
        ct='City'
        e_id='email_id'
        if record!=None:
            print('\nRESULT: ')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+nm.ljust(23)+'│'+an.center(10)+'│'+rn.center(9)+'│'+cl.ljust(5)+'│'+at.ljust(10)+'│'+eng.ljust(7)+'│'+mat.ljust(5)+'│'+cs.ljust(10)+'│'+py.ljust(7)+'│'+ch.ljust(9)+'│'+per.ljust(10),' │')
            print('─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+record[0].ljust(23)+'│'+str(record[1]).center(10)+'│'+record[2].center(9)+'│'+str(record[3]).center(5)+'│'+str(record[4]).center(10)+'│'+str(record[5]).center(7)+'│'+str(record[6]).center(5)+'│'+str(record[7]).center(10)+'│'+str(record[8]).center(7)+'│'+str(record[9]).center(9)+'│'+str(record[10]).center(10)+'  │')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('\n\n')
            print('Student Details: ')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+nm.ljust(23)+'│'+an.center(10)+'│'+rn.center(9)+'│'+cl.ljust(5)+'│'+ge.ljust(6)+'│'+at.ljust(10)+'│'+ad.ljust(28)+'│'+dob.ljust(10)+'│'+mn.ljust(10)+'│'+ct.ljust(11)+'│'+per.ljust(10)+'│'+e_id.ljust(29)+' │')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+record[0].ljust(23)+'│'+str(record[1]).center(10)+'│'+record[2].center(9)+'│'+str(record[3]).center(5)+'│'+str(record[11]).center(6)+'│'+str(record[4]).center(10)+'│'+record[12].ljust(28)+'│'+str(record[13]).center(10)+'│'+str(record[14]).center(10)+'│'+str(record[15]).center(11)+'│'+str(record[10]).center(10)+'│'+str(record[16]).ljust(29)+' │')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('\n')
        else:
            
             print("\nRecord with Admission number {} does not exist".format(A_no))
        input("\n\nPress Any Key to Continue..........")
        
    except mysql.connector.Error as error:
        print("Failed to fetch the record: {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            #print("\n\n\nMySQL connection is closed")

            

def Delete():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_data',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()

        st="Create table if not exists RESULT_SCI (Full_name Varchar(20), adm_no Smallint, Roll_no tinyint, Class tinyint, Attd decimal(4,1), Eng tinyint, Math tinyint, Comp tinyint, Phy tinyint, Chem tinyint, Total_percent decimal(5,2), Gender Char(1), Address Varchar(40), DOB date, Mobile_no BIGINT , City varchar(25), email_id varchar(30) )"
        cursor.execute(st)

        
        query = "Delete from result_sci where Adm_no = %s"
        A_no=int(input('Admission number: '))
        A=(A_no,)

        sql_select_query = "select * from result_sci where Adm_no=%s"
        cursor.execute(sql_select_query,A)
        record = cursor.fetchone()

        if record!=None:
        
            cursor.execute(query,A)
            connection.commit()
            print("\nRecord Deleted successfully ")
            input("\n\nPress Any Key to Continue..........")
        else:
            print("\nRecord with Admission number {} does not exist".format(A_no))

    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
           

def update():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Student_data',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        st="Create table if not exists RESULT_SCI (Full_name Varchar(20), adm_no Smallint, Roll_no tinyint, Class tinyint, Attd decimal(4,1), Eng tinyint, Math tinyint, Comp tinyint, Phy tinyint, Chem tinyint, Total_percent decimal(5,2), Gender Char(1), Address Varchar(40), DOB date, Mobile_no BIGINT , City varchar(25), email_id varchar(30) )"
        cursor.execute(st)
        
        Adm_no=int(input('Admission number: '))
        sql_select_query = """select * from result_sci where Adm_no=%s"""
        A=(Adm_no,)
        sql_select_query = "select * from result_sci where Adm_no=%s"
        cursor.execute(sql_select_query,A)
        record = cursor.fetchone()

        if record!=None:
            
            #cursor.execute(sql_select_query,A)
            #record = cursor.fetchone()
            #print(record)
            nm='Name'
            rn='Roll_no'
            an='Adm. No.'
            cl='Class'
            at='Attendance'
            ge='Gender'
            ad='Address'
            dob='DOB'
            mn='Mobile No.'
            ct='City'
            e_id='email_id'
            per='Percentage'
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+nm.ljust(23)+'│'+an.center(10)+'│'+rn.center(9)+'│'+cl.ljust(5)+'│'+ge.ljust(6)+'│'+at.ljust(10)+'│'+ad.ljust(28)+'│'+dob.ljust(10)+'│'+mn.ljust(10)+'│'+ct.ljust(11)+'│'+per.ljust(10)+'│'+e_id.ljust(29)+' │')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+record[0].ljust(23)+'│'+str(record[1]).center(10)+'│'+record[2].center(9)+'│'+str(record[3]).center(5)+'│'+str(record[11]).center(6)+'│'+str(record[4]).center(10)+'│'+record[12].ljust(28)+'│'+str(record[13]).center(10)+'│'+str(record[14]).center(10)+'│'+str(record[15]).center(11)+'│'+str(record[10]).center(10)+'│'+str(record[16]).ljust(29)+' │')
            print('────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            

            
                    

            print('\nTO make change, enter new value else enter "." for string values')
           
            new_Full_name=input("\n\t\tEnter updated Full_name: ")
            if new_Full_name=='.':
                new_Full_name=record[0]
                
            
            
            new_DOB=input("\t\tEnter updated Date of birth: ")
            if new_DOB=='.':
                new_DOB=record[13]

            new_Gender=input("\t\tEnter updated Gender: ")
            if new_Gender=='.':
                new_Gender=record[11]

            new_Class=input("\t\tEnter updated Class: ")
            if new_Class=='.':
                new_Class=record[3]

            new_Address=input("\t\tEnter updated Address: ")
            if new_Address=='.':
                new_Address=record[12]
            
            new_City=input("\t\tEnter updated City: ")
            if new_City=='.':
                new_City=record[15]

            new_Mobile_no=input("\t\tEnter updated Mobile_no: ")
            if new_Mobile_no=='.':
                new_Mobile_no=record[14]

            new_Email_id=input("\t\tEnter updated Email_id: ")
            if new_Email_id=='.':
                new_Email_id=record[16]


            # Update single record now
            sql_update_query = """update result_sci set Full_name='{}',
                                  dob='{}',gender='{}',class='{}',
                                  address='{}',city='{}',mobile_no='{}',
                                  email_id='{}' where adm_no={}""".format(new_Full_name,new_DOB,new_Gender, new_Class, new_Address,new_City, new_Mobile_no, new_Email_id, Adm_no)

            #print(sql_update_query)
            cursor.execute(sql_update_query)
        
            
            connection.commit()
            print(cursor.rowcount," Record Updated successfully ")
        else:
            print("\nRecord with Admission number {} does not exist".format(Adm_no))
        input("\n\nPress Any Key to Continue..........")

    except mysql.connector.Error as error:
        print("Failed to update table record: {}".format(error))
    finally:
        if (connection.is_connected()):
            connection.close()
            

def Display():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_data',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()

        st="Create table if not exists RESULT_SCI (Full_name Varchar(20), adm_no Smallint, Roll_no tinyint, Class tinyint, Attd decimal(4,1), Eng tinyint, Math tinyint, Comp tinyint, Phy tinyint, Chem tinyint, Total_percent decimal(5,2), Gender Char(1), Address Varchar(40), DOB date, Mobile_no BIGINT , City varchar(25), email_id varchar(30) )"
        cursor.execute(st)
        
        cls = int(input("Enter class whose result you want to see(11 or 12): "))
        Query = "SELECT * FROM result_sci where class={} order by total_percent desc ".format(cls)
        
        cursor.execute(Query)                        
        data = cursor.fetchall()
        
        if cursor.rowcount>0:        
            nm = 'Name'
            an = 'Adm. No.'
            cl ='Class'
            at = 'Attendance'
            eng = 'English'
            mat = 'Maths'
            cs = 'Comp. Sci.'
            py = 'Physics'
            ch = 'Chemistry'
            per = 'Percentage'
            print('─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print('│ '+nm.ljust(30)+'│'+an.center(10)+'│'+cl.ljust(5)+'│'+at.ljust(10)+'│'+eng.ljust(7)+'│'+mat.ljust(5)+'│'+cs.ljust(10)+'│'+py.ljust(7)+'│'+ch.ljust(9)+'│'+per.ljust(10),' │')
            print('─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            
            
            for record in data:
                print('│ '+record[0].ljust(30)+'│'+str(record[1]).center(10)+'│'+str(record[3]).center(5)+'│'+str(record[4]).center(10)+'│'+str(record[5]).center(7)+'│'+str(record[6]).center(5)+'│'+str(record[7]).center(10)+'│'+str(record[8]).center(7)+'│'+str(record[9]).center(9)+'│'+str(record[10]).center(10)+'  │')
            print('─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            input("\n\nPress Any Key to Continue..........")
        else:
            print("No Record Found with given Criteria..")
            input("\n\nPress Any Key to Continue..........")
        
    except mysql.connector.Error as error:
        print("\nFailed to Display records from result_sci table {}".format(error))
    
    finally:
        if (connection.is_connected()):
            connection.close()
            




#______MAIN_________
            

while True:
    print('\nMain Menu: ')
    print('1. Add Student: ')
    print('2. Search Student: ')
    print('3. Delete Student: ')
    print('4. Update Student:')
    print('5. Display Result:')
    print('6. Exit:\n\n ')
    ch=int(input("Enter Your Choice: "))
    while True:
        if ch==1:
            add_student()
            break
            
        elif ch==2:
            search()
            break
        
        elif ch==3:
            Delete()
            break
        
        elif ch==4:
            update()
            break
        
        elif ch==5:
            Display()
            break
        
        elif ch==6:            
            exit()
            
        else:
            print("You entered wrong choice")
            input("Press Any Key to Continue.......")
            break
        
