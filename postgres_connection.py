import psycopg2
#config
hostname = 'localhost'
username = 'postgres'
password = 'password1'
database = 'socket_db'
#db login select
def db_connection(userName, passWord):
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(user=username,password=password,host=hostname,dbname=database)
        # create a cursor
        cur = conn.cursor()
        # Execute a sql
        cur.execute('SELECT * FROM "User_account" where username = %s and password = %s', (userName, passWord))
        # display the PostgreSQL database server version
        if ((cur.rowcount) == 1):
            return True
        else:
            return False

        conn.commit()
        cur.close()
    except Exception as e:
        print('Unable to connect %s' % str(e))
    finally:
        if conn is not None:
            conn.close()
#------------------------------------------------------------------------
#db check exist
#if exist-> return true, else return false
def db_search_username(userName):
    try:
        conn = psycopg2.connect(user=username,password=password,host=hostname,dbname=database)
        cur = conn.cursor()
        cur.execute('SELECT * FROM "User_account" where username = %s', (userName,))
        #check number of row
        #if >=1->exist
        if  ((cur.rowcount) == 1):
            return True
        else:
            return False
        conn.commit()
    except Exception as e:
        print('Unable to connect %s' % str(e))
    finally:
        if conn is not None:
            conn.close()
#------------------------------------------------------------------------
#db new account insert
def db_registration(userName, passWord):
    try:
        conn = psycopg2.connect(user=username,password=password,host=hostname,dbname=database)
        cur = conn.cursor()

        # sql_query =
        cur.execute('INSERT INTO "User_account" (username,password) VALUES (%s, %s)', (userName, passWord))
        #if exist username, return False -> respond error creating account
        conn.commit()
        cur.close()
    except Exception as e:
        print('Unable to connect %s' % str(e))
    finally:
        if conn is not None:
            conn.close()
#------------------------------------------------------------------------
