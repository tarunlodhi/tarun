import mysql.connector as mcon
mydb = mcon.connect(host = "localhost",user = "root",passwd = "tarun@12345",database = "Parkon")
mycursor = mydb.cursor()

def login(u,p):
    mycursor.execute("select uname from logdetails")
    u="('"+u+"',)"
    p="('"+p+"',)"
    unames = ''
    passwd = ''
    for i in mycursor:
        unames += str(i)
    mycursor.execute("select password from logdetails")
    for i in mycursor:
        passwd +=str(i)
    if u == unames and p == passwd:
        return 1
    else:
        return 0
