# -*- coding: utf-8 -*-
#------------------MODULES IMPORTED---------------------------------------
import datetime                #datetime module
import random as rd            #random module
import mysql.connector         #SQL module
from tabulate import tabulate  #table module
from art import *              #ART MODULE
#------------------SQL CONNECTION---------------------------------------
con=mysql.connector.connect(host="localhost",user="root",password="root")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("create database if not exists Library")

cur.execute("use library")


#------------------------Connectivity Table -----------------------------------

cur.execute("create table if not exists books"
            "("
            "bid varchar(20) primary key,"
            "Book_Name varchar(30),"
            "Author varchar(30),"
            "Category char(25),"
            "status varchar(30) )")

cur.execute("create table if not exists issued_books"
            "("
            "bid varchar(20) primary key,"
            "Book_Name varchar(30),"
            "Name varchar(30),"
            "Designation varchar(25) ) ")
            
cur.execute("create table if not exists teachers"
            "("
            "T_Id char(12) primary key,"
            "Name varchar(30),"
            "Gender char(1),"
            "Age int(10),"
            "Pnumber varchar(10) unique) ")

cur.execute("create table if not exists students"
            "("
            "S_Id char(12) primary key,"
            "Name varchar(30),"
            "Gender char(1),"
            "Age int(10),"
            "Pnumber varchar(10) unique) ")





#---------------------Random Thought-------------------------------------------

tht1='''
                   BEAUTIFUL THINGS HAPPEN WHEN YOU DISTANCE YOURSELF FROM 
                  ---------------------------------------------------------
                                       NEGATIVITY
                                      ------------
                    '''
tht2='''
                          DREAMS ARE NOT WHAT YOU SEE WHEN YOU SLEEP,
                          ------------------------------------------
                          DREAMS ARE THOSE WHICH DON'T LET YOU SLEEP 
                          ------------------------------------------
       '''
tht3='''
                     YOU ONLY LIVE ONCE. BUT IF YOU DO IT RIGHT,
                     ------------------------------------------
                                   ONCE IS ENOUGH
                                  ----------------
       '''
tht4=''' 
                      THE EXPERT IN ANYTHING WAS ONCE A BEGINNER
                     --------------------------------------------

'''
tht5='''
                      NOT ALL STORMS COME TO DISRUPT YOUR LIFE
                      ----------------------------------------
                           SOME COME TO CLEAR YOUR PATH
                           ----------------------------
        '''
tht6='''
                   LISTEN TO EVERYONE AND LEARN FROM EVERYONE, BEACAUSE NOBODY KNOWS EVERYTHING  
                  ------------------------------------------------------------------------------       
                                         BUT EVERYONE KNOWS SOMETHING
                                         ----------------------------
                  '''
tht7='''
                     ONE KIND WORD CAN CHANGE SOMEONE'S 
                     ----------------------------------
                               ENTIRE DAY
                               ----------
                               '''
tht8='''
                     GOOD MANNERS AND KINDNESS ARE ALWAYS 
                     ------------------------------------
                                 IN FASHION
                                 ----------
                                 '''
th=(tht1,tht2, tht3,tht4,tht5,tht6,tht7,tht8)

print("""
              
    _     __  __  ____   ___  _____     _     __     __ ___  ____  __   __    _     _         _    __   __    _     __  __ 
   / \   |  \/  ||  _ \ |_ _||_   _|   / \    \ \   / /|_ _||  _ \ \ \ / /   / \   | |       / \   \ \ / /   / \   |  \/  |
  / _ \  | |\/| || |_) | | |   | |    / _ \    \ \ / /  | | | | | | \ V /   / _ \  | |      / _ \   \ V /   / _ \  | |\/| |
 / ___ \ | |  | ||  _ <  | |   | |   / ___ \    \ V /   | | | |_| |  | |   / ___ \ | |___  / ___ \   | |   / ___ \ | |  | |
/_/   \_\|_|  |_||_| \_\|___|  |_|  /_/   \_\    \_/   |___||____/   |_|  /_/   \_\|_____|/_/   \_\  |_|  /_/   \_\|_|  |_|
                                                                                                                           

      
      
      """)
d=datetime.date.today()
t=datetime.datetime.now()
print(" ")
print(" ")
print("        DATE:-",d.strftime("%A, %d %B %Y"))
print(" ")
print("        TIME:-",t.strftime("%H:%M:%S"))
print("")
print('')      

choice=rd.choice(th)
print(choice)

while True:
    print(""" 
      
    
        
         ______________                 ___________________                 ___________
        |             |                |                  |                |          |
        | 1. REGISTER |                | 2. ISSUE BOOKS   |                | 3. EXIT  |
        |_____________|                |__________________|                |__________|
        
         
        
        """)


    x=int(input("||  SELECT || :-"))

    if x==1:
        
        def AddStu():
            S_Id=input("Enter Student ID:-  ")
            S_Name=input("Enter Student Name:-  ")
            while True:
                Gender=input("Enter Gender(M/F):-  ")
                if Gender=="M" or Gender=="F":
                    break
                else:
                    print("~!~!~!~~ M\F only ~~!~!~!~")
            while True:
                age=int(input("Age:"))
                if type(age)!=int:
                    print("~!~!~!~~digits required~~!~!~!~")
                else:
                    break
            while True:
                ph=input("Phone no.:")
                if len(ph)==10 :
                    break
                else:
                    print("~!~!~!~~10 digits required~~!~!~!~")
            cur.execute("insert into students(S_Id,Name,Age,Gender,Pnumber) values(%s,%s,%s,%s,%s)",(S_Id,S_Name,age,Gender,ph,))
            con.commit()
     
            print(" ")
            print("""   
           ____________________________        
          |                           |
          |STUDENT HAS BEEN REGISTERED| 
          |___________________________|     
             """)
          
            print("""
         ______________________________ 
        |                             |
        | Details are as follows:-    |
        |_____________________________| 
        
            """)
            cur.execute("select * from students where S_Id=(%s);",(S_Id,))
            d=cur.fetchall()
            for i in d:
                print("""     Student Id:-""",i[0])
                print('''     Student Name:-''',i[1])
                print('''     Age:-''',i[2])
                print('''     Gender:-''',i[3])
                print('''     Phone:-''',i[4])
                return("")
        
        def AddTea():
            T_Id=input("Enter Teacher ID:-  ")
            T_Name=input("Enter Teacher Name:-  ")
            while True:
                Gender=input("Enter Gender(M/F):-  ")
                if Gender=="M" or Gender=="F":
                    break
                else:
                    print("~!~!~!~~ M\F only ~~!~!~!~")
            while True:
                age=int(input("Age:"))
                if type(age)!=int:
                    print("~!~!~!~~digits required~~!~!~!~")
                else:
                    break
            while True:
                ph=input("Phone no.:")
                if len(ph)==10 :
                    break
                else:
                    print("~!~!~!~~10 digits required~~!~!~!~")
            cur.execute("insert into teachers(T_Id,Name,Age,Gender,Pnumber) values(%s,%s,%s,%s,%s)",(T_Id,T_Name,age,Gender,ph,))
            con.commit()
     
            print(" ")
            print("""   
           _________________________        
          |                        |
          |  TEACHER REGISTERED    | 
          |________________________|     
             """)
          
            print("""
         ______________________________ 
        |                             |
        | Details are as follows:-    |
        |_____________________________| 
        
        """)
            cur.execute("select * from Teachers where T_Id=(%s);",(T_Id,))
            d=cur.fetchall()
            for i in d:
                print("""     Teacher Id:-""",i[0])
                print('''     Teacher Name:-''',i[1])
                print('''     Gender:-''',i[2])
                print('''     Age:-''',i[3])
                print('''     Phone:-''',i[4])
                return("")
        
        def AddBook():
            book_no=input("Enter Book ID:-  ")
            Book_Name=input("Enter Book Name:-   ")
            Author=input("Enter Author Name:-   ")
            Category=input("Enter Book Category:-   ")
            status=input("Enter Status ( avail\issued):-  ")
    
    
            cur.execute("insert into books(bid, Book_Name, Author, Category, status) values(%s,%s,%s,%s,%s)",(book_no, Book_Name,Author, Category, status))
            con.commit()
            print(" ")
            print("""   
           _________________________        
          |                        |
          |BOOK SUCCESSFULLY ADDED | 
          |________________________|     
             """)
          
            print("""
         ______________________________ 
        |                             |
        |        BOOK DETAILS         |
        |_____________________________| 
        
            """)
            cur.execute("select * from books where bid=(%s);",(book_no,))
            d=cur.fetchall()
            for i in d:
                print("""     Book Number:-""",i[0])
                print('''     Book Name:-''',i[1])
                print('''     Author:-''',i[2])
                print('''     Category:-''',i[3])
                print('''     Status:- ''',i[4])
                return("")
        
        
        
        while True:
            print(""" 
      
    
        
         _________________                 ___________________                 ________________            ___________________                 ___________
        |                |                |                  |                |               |           |                  |                |          |
        | 1. ADD STUDENT |                | 2. ADD TEACHER   |                | 3. ADD BOOKS  |           | 4. SHOW DETAILS  |                | 5. BACK  |
        |________________|                |__________________|                |_______________|           |__________________|                |__________|
        
         
        
            """)
            y=int(input("||  SELECT || :-"))
            
            if y==1:
                AddStu()
            elif y==2:
                AddTea()
            elif y==3:
                AddBook()
            elif y==4:
                while True:
                    print("                                                                      Details:-                         ")
                    print(""" 
      
    
        
         _________________                 ___________________                 ________________            ___________________
        |                |                |                  |                |               |           |                  |  
        | 1. STUDENT     |                | 2. TEACHER       |                | 3.  BOOKS     |           | 4. BACK          | 
        |________________|                |__________________|                |_______________|           |__________________|
        
         
        
                    """)
                    z=int(input("||  SELECT || :-"))
                    print("  ")
                    print("  ")
                    if z==1:
                        cur.execute("select * from students")
                        data=cur.fetchall()
                        h=["S_Id","S_Name","Gender","Age","Phone Number"]
                        print(tabulate(data, headers=h, tablefmt='psql'))
                        break
                    elif z==2:
                        cur.execute("select * from teachers")
                        data=cur.fetchall()
                        h=["T_Id","T_Name","Gender","Age","Phone Number"]
                        print(tabulate(data, headers=h, tablefmt='psql'))
                        break
                    elif z==3:
                        cur.execute("select * from books")
                        data=cur.fetchall()
                        h=["Book_No","Book_Name","Author","Category","Status"]
                        print(tabulate(data, headers=h, tablefmt='psql'))
                        break
                    elif z==4:
                        break
                    else:
                        print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
            elif y==5:
                break
            else:
                print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
                
    elif x==2:
        while True:
            print(""" 
      
    
        
         _____________________                 _____________________                 ___________________            ___________________
        |                    |                |                    |                |                  |           |                  |
        | 1. Teacher's Issue |                | 2. Student's Issue |                | 3. Issued Books  |           |   4. BACK        |
        |____________________|                |____________________|                |__________________|           |__________________|
        
         
        
            """)
            a=int(input("||  SELECT || :-"))
            
            if a==1:
               def TeaIss():
                    print("-------------------Teachers Issue--------------------")
                    print("  ")
                    print("  ")
                    bk_no=input("Enter Book ID:-   ")
                    bk_name=input("Enter Book Name:-   ")
                    name=input("Enter Teacher's Name:-  ")
                    Designation="Teacher"
                    cur.execute("")
                
                    cur.execute("insert into issued_books(bid,Book_Name,Name,Designation) values(%s,%s,%s,%s)",(bk_no,bk_name,name,Designation))
                    con.commit()
                    print(" ")
                    print("""   
                           _________________________        
                          |                        |
                          |BOOK ISSUED SUCCESSFULLY| 
                          |________________________|     
                     """)
               TeaIss()
               break
            elif a==2:
               def StuIss():
                    print("-------------------Students Issue--------------------")
                    print("  ")
                    print("  ")
                    bk_no=input("Enter Book ID:-   ")
                    bk_name=input("Enter Book Name:-   ")
                    name=input("Enter Student's Name:-  ")
                    Designation="Student"
                
                
                    cur.execute("insert into issued_books(bid,Book_Name,Name,Designation) values(%s,%s,%s,%s)",(bk_no,bk_name,name,Designation))
                    con.commit()
                    print(" ")
                    print("""   
                           _________________________        
                          |                        |
                          |BOOK ISSUED SUCCESSFULLY| 
                          |________________________|     
                     """)
               StuIss()
               break
            elif a==3:
               cur.execute("select * from issued_books")
               data=cur.fetchall()
               h=["Book No","Book Name","Issued By","Designation"]
               print(tabulate(data, headers=h, tablefmt='psql'))
               break
            elif a==4:
                break
            else:
                print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
    elif x==3:
        Art = text2art("THANK  YOU")

        print(Art)
        print("")
        print("                             Developed By:-                             ")
        print("                                           ADARSH NAYAK                               ")
        print("                                           ADVAIT KALE                                ")
        print("                                           GOVIND NAIR                                ")
        print("                                           HARSH MHATRE                               ")
        break
    

