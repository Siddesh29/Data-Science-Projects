class Health():
 def __init__(self):        #constructor for connecting to database
        import pymysql
        try:
            self.__conn=pymysql.connect(host='Localhost',user='root',password='',db='health')
        except Exception as e:
            print(e)
        else:
            print('Connection successful')
 def empdata(self,eid,n,age,exr,jnk,drk,smk):      #method to input data of employee
     self.__eid=eid
     self.__n=n
     self.__age=age
     self.__exr=exr
     self.__jnk=jnk
     self.__drk=drk
     self.__smk=smk
     query='insert into lifestyle values(%s,%s,%s,%s,%s,%s,%s)'
     val=(eid,n,age,exr,jnk,drk,smk)
     cur=self.__conn.cursor()
     try:
         cur.execute(query,val)
     except Exception as e:
         print(e)
     else:
         print('Record Entered Successfully')
         self.__conn.commit()
         self.__conn.close()
 def showdata(self,eid):         #method to display data of required employee
     query='select * from lifestyle where empid=%s'
     cur=self.__conn.cursor()
     try:
         cur.execute(query,eid)
     except Exception as e:
         print(e)
     else:
         result=cur.fetchall()
         if result:
             import pandas
             a=[]
             b=['Employee I.D :','Name :','Age :','Exersice :','Junk Food :','Alcohol :','Smoking :']
             for i in result:
                 for j in i:
                     a.append(j)
                 dict={'A':b,'B':a}
                 product=pandas.DataFrame(dict)
                 print(product)
                 self.__conn.commit()
                 self.__conn.close()
 def alterdata(self,eid):     #method to update employee data
     print('Which data would yoy like to update\n1.Exercise\n2.Junk Food\n3.Alcohol\n4.Smoking')
     alt=int(input('Enter appropriate service option number :'))
     if alt==1:
         print('How many times you exercise weekly\n1.6 Times a week\n2.3-5 times a week\n3.Never')
         exr=int(input('Please enter appropriate option number : '))
         if exr==1:
             exr='Daily'
         elif exr==2:
             exr='3-5 times a week'
         else:
             exr='Never'
         query='update lifestyle set exercise=%s where empid=%s'
         val=(exr,eid)
         cur=self.__conn.cursor()
         try:
             cur.execute(query,val)
         except Exception as e:
             print(e)
         else:
             print('Record Updated Sucessfully')
             self.__conn.commit()
             self.__conn.close()
     elif alt==2:
         print('How many times you eat fast food weely\n1.Everyday\n2.3-5 times a week\n3.Occasionally')
         jnk=int(input('Please enter appropriate option number : '))
         if jnk==1:
             jnk='Daily'
         elif jnk==2:
             jnk='3-5 times a week'
         else:
             jnk='Never'
         query='update lifestyle set junk_food=%s where empid=%s'
         val=(jnk,eid)
         cur=self.__conn.cursor()
         try:
             cur.execute(query,val)
         except Exception as e:
             print(e)
         else:
             print('Record Updated Sucessfully')
             self.__conn.commit()
             self.__conn.close()
     elif alt==3:
         print('How many times you drink Alcohol weekly\n1.Everyday\n2.Occasionally\n3.Never')
         drk=int(input('Please enter appropriate option number : '))
         if drk==1:
             drk='Daily'
         elif drk==2:
             drk='3-5 times a week'
         else:
             drk='Never'
         query='update lifestyle set drinking=%s where empid=%s'
         val=(drk,eid)
         cur=self.__conn.cursor()
         try:
             cur.execute(query,val)
         except Exception as e:
             print(e)
         else:
             print('Record Updated Sucessfully')
             self.__conn.commit()
             self.__conn.close()        
     elif alt==4:
         print('How many times you smoke weekly\n1.Everyday\n2.Occasionally\n3.Never')
         smk=int(input('Please enter appropriate option number : '))
         if smk==1:
             smk='Daily'
         elif smk==2:
             smk='3-5 times a week'
         else:
             smk='Never'
         query='update lifestyle set smoking=%s where empid=%s'
         val=(smk,eid)
         cur=self.__conn.cursor()
         try:
             cur.execute(query,val)
         except Exception as e:
             print(e)
         else:
             print('Record Updated Sucessfully')
             self.__conn.commit()
             self.__conn.close()
 def deletedata(self,eid):        #method to delete particular employee data
     query='delete from lifestyle where empid=%s'
     cur=self.__conn.cursor()
     try:
         cur.execute(query,eid)
     except Exception as e:
         print(e)
     else:
        print('Record Deleted Sucessfully')
        self.__conn.commit()
        self.__conn.close()
 def showall(self):         #method to show all data
     query='select * from lifestyle'
     cur=self.__conn.cursor()
     try:
         cur.execute(query)
     except Exception as e:
         print(e)
     else:
         result=cur.fetchall()
         #print(result)
         for i in result:
             for j in i:
                 print(j)
         self.__conn.commit()
         self.__conn.close()
 
         
#main program
print('Which service would you like to use\nPlease enter oppropriate option number\n1.Enter employee data\n2.Collect employee data\n3.Alter employee data\n4.Delete employee data\n5.Show all data\n6.Exit')
srv=int(input('Please enter required service number :'))
if srv==1: 
    try:
        eid=int(input('Enter Employee I.D :'))
    except Exception as e:
        print('Please enter valid Employee I.D')
    else:    
        n=input('Enter name :')
        try:
            age=int(input('Enter age in years :'))
        except Exception as e:
            print('Please enter integer value')
        else:    
            print('How many times you exercise weekly\n1.6 Times a week\n2.3-5 times a week\n3.Never')
            try:
                exr=int(input('Please enter appropriate option number :'))
                if exr<1 or exr>3:
                    raise Exception('Please Enter Valid Option Number')
            except Exception as e:
                print(e)
            else:
                if exr==1:
                    exr='Daily'
                elif exr==2:
                    exr='3-5 times a week'
                else:
                    exr='Never'
                print('How many times you eat fast food weely\n1.Everyday\n2.3-5 times a week\n3.Occasionally')
                try:
                    jnk=int(input('Please enter appropriate option number :'))
                    if jnk<1 or jnk>3:
                        raise Exception('Please Enter Valid Option Number')
                except Exception as e:
                    print(e)
                else:
                    if jnk==1:
                        jnk='Daily'
                    elif jnk==2:
                        jnk='3-5 times a week'
                    else:
                        jnk='Occasionally'
                    print('How many times you drink Alcohol weekly\n1.Everyday\n2.Occasionally\n3.Never')
                    try:
                        drk=int(input('Please enter appropriate option number :'))
                        if drk<1 or drk>3:
                            raise Exception('Please Enter Valid Option Number')
                    except Exception as e:
                        print(e)
                    else:
                        if drk==1:
                            drk='Daily'
                        elif drk==2:
                            drk='Occasionally'
                        else:
                            drk='Never'
                        print('How many times you smoke weekly\n1.Everyday\n2.Occasionally\n3.Never')
                        try:
                            smk=int(input('Please enter appropriate option number :'))
                            if smk<1 or smk>3:
                                raise Exception('Please Enter Valid Option Number')
                        except Exception as e:
                            print(e)
                        else:
                            if smk==1:
                                smk='Daily'
                            elif smk==2:
                                smk='Occasionally'
                            else:
                                smk='Never'    
                            H=Health()
                            H.empdata(eid,n,age,exr,jnk,drk,smk)
                        
elif srv==2:
    try:
        eid=int(input('Enter Employee I.D :'))
    except Exception as e:
        print('Please enter valid Employee I.D')
    else:
        H=Health()
        H.showdata(eid)
elif srv==3:
    try:
        eid=int(input('Enter Employee I.D :'))
    except Exception as e:
        print('Please enter valid Employee I.D')
    else:
        H=Health()
        H.alterdata(eid)
elif srv==4:
    try:
        eid=int(input('Enter Employee I.D :'))
    except Exception as e:
        print('Please enter valid Employee I.D')
    else:
        H=Health()
        H.deletedata(eid)
elif srv==5:
        H=Health()
        H.showall()
elif srv==6:
    pass
else:
    print('Please Enter Valid Option')
