import mysql.connector
import traceback
def ConnectionToDB():
    
    return mysql.connector.connect(host="localhost", user="root",  passwd="", database="controleur_gestion")
    try:
        
        print("Connexion Etablished with cursor!")
    except Exception:
        print("problem when try to connect")
        print(traceback.format_exc())

def list_known_projects_Id():
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT  project_id FROM sum_salary_in_project "
    mycursor.execute(sql)   
    myresult = mycursor.fetchall()
    #print(myresult)
    list=["'","(",")",","] 
    #res="".join(i for i in myresult if i not in list) 
    res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    #print(res)
    list = res
    #print(list)
    return list

def last_date_dev():
    mydb = ConnectionToDB()
    
    mycursor = mydb.cursor()
    sql = "SELECT date_update FROM grade_res WHERE grade='developer' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    
    return res

def last_date_qa():
    mydb = ConnectionToDB()
    
    mycursor = mydb.cursor()
    sql = "SELECT date_update FROM grade_res WHERE grade='quality' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
   
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
 
    return res

def last_date_devops():
    mydb = ConnectionToDB()
    
    mycursor = mydb.cursor()
    sql = "SELECT date_update FROM grade_res WHERE grade='devops' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
   
    return res

def last_date_sup():
    mydb = ConnectionToDB()
    
    mycursor = mydb.cursor()
    sql = "SELECT date_update FROM grade_res WHERE grade='support' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    return res


def sum_salary_project(num):
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT  sum_salary FROM sum_salary_in_project WHERE project_id = {}".format(num)
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res=",".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    #list = res
    return res

def salary_dev():
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT  salaire FROM grade_res WHERE grade='developer' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res="".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    return res

def salary_qa():
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT salaire FROM grade_res WHERE grade='quality' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res="".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    return res

def salary_devops():
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT  salaire FROM grade_res WHERE grade='devops' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 

    #res="".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    return res

def salary_support():
    mydb = ConnectionToDB()
    mycursor = mydb.cursor()
    sql = "SELECT  salaire FROM grade_res WHERE grade='support' "
    mycursor.execute(sql)   
    myresult = mycursor.fetchone()
    list=["'","(",")",","] 
    res="".join(str(i) for i in myresult if i not in list) 
    #res="".join(''.join(map(str, tup)) for tup in myresult if tup not in list) 
    return res