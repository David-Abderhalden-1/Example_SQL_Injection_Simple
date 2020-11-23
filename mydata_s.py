import mysql.connector

# Connection to database
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL_wardwird0$",
    database="user"
)

# Login not injectable
def login_checker_safe(username, password):
    my_cursor_prepared = mydatabase.cursor()
    checker_query = "SELECT * FROM user_authentication_2 WHERE username = %s AND password = %s;"
    credentials = (username, password)
    my_cursor_prepared.execute(checker_query, credentials)
    my_result = my_cursor_prepared.fetchall()
    print("Length of Query result: " + str(len(my_result)))
    if len(my_result) > 0:
        return True
    my_cursor_prepared.close()