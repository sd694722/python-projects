import mysql.connector

def create_conn():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
    return conn

create_conn()

conn = create_conn()
cursor = conn.cursor()

# ********************************************************************************************************
# insert student details --------------------------------------------------------
def insert_student():
    sql_insert= "INSERT INTO `students`(`name`, `age`, `phone_number`) VALUES('{name}',{age},'{phone_number}')"
    name = input("Enter name: ")
    age = input("Enter age: ")
    phone_number = input("Enter phone number: ")
    sql_insert = sql_insert.format(name=name, age=age, phone_number=phone_number)
    print(sql_insert)
    cursor.execute(sql_insert)
    conn.commit()
    print("Record inserted successfully")
    print("\n")

# ********************************************************************************************************
# read student details ----------------------------------------------------------
def read_student():
    sql_select = "SELECT * FROM students"
    cursor.execute(sql_select)
    result = cursor.fetchall()
    for row in result:
        print("______________________________")
        print(row)
        print("______________________________")

    print("\n")

# ********************************************************************************************************
# update student details -------------------------------------------------------
def update_student():
    student_id = input("Enter student id: ")
    if not student_id.isdigit():
        print("Invalid student id\n")
        return
    student_id = int(student_id)
    sql_select = "SELECT * FROM students WHERE student_id = {student_id}"
    cursor.execute(sql_select.format(student_id=student_id))
    result = cursor.fetchall()
    if not result:
        print("Student not found\n")
        return
    print("Student found\n")

    print(result)
    print("______________________________")
    print("WHAT DO YOU WANT TO UPDATE ?")
    print("1. Name")
    print("2. Age")
    print("3. Phone Number")
    print("4. All")
    print("5. Exit")
    key = int(input("Enter your choice: "))
    
    if key == 1:
        name = input("Enter new name: ")
        sql_update = "UPDATE students SET name = '{name}' WHERE student_id = {student_id}"
        sql_update = sql_update.format(name=name, student_id=student_id)
        cursor.execute(sql_update)
        conn.commit()
        print("Record updated successfully")
    elif key == 2:
        age = input("Enter new age: ")
        sql_update = "UPDATE students SET age = {age} WHERE student_id = {student_id}"
        sql_update = sql_update.format(age=age, student_id=student_id)
        cursor.execute(sql_update)
        conn.commit()
        print("Record updated successfully")
    elif key == 3:
        phone_number = input("Enter new phone number: ")
        sql_update = "UPDATE students SET phone_number = '{phone_number}' WHERE student_id = {student_id}"
        sql_update = sql_update.format(phone_number=phone_number, student_id=student_id)
        cursor.execute(sql_update)
        conn.commit()
        print("Record updated successfully")
    elif key == 4:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        phone_number = input("Enter new phone number: ")
        sql_update = "UPDATE students SET name = '{name}', age = {age}, phone_number = '{phone_number}' WHERE student_id = {student_id}"
        sql_update = sql_update.format(name=name, age=age, phone_number=phone_number, student_id=student_id)
        cursor.execute(sql_update)
        conn.commit()
        print("Record updated successfully")
    elif key == 5:
        print("Exiting...")
        return
    else:
        print("Invalid choice")
    print("\n")



# ********************************************************************************************************
# delete student details -------------------------------------------------------
def delete_student():
    student_id = input("Enter student id: ")
    if not student_id.isdigit():
        print("Invalid student id\n")
        return
    student_id = int(student_id)
    sql_select = "SELECT * FROM students WHERE student_id = {student_id}"
    cursor.execute(sql_select.format(student_id=student_id))
    result = cursor.fetchall()
    if not result:
        print("Student not found\n")
        return
    print("Student found\n")

    sql_delete = "DELETE FROM students WHERE student_id = {student_id}"
    cursor.execute(sql_delete.format(student_id=student_id))
    conn.commit()
    print("Record deleted successfully")
    print("\n")

# ********************************************************************************************************
# master menu ------------------------------------------------------------------
def master_menu():
    while True:
        print("1. Insert Student")
        print("2. All Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        key = int(input("Enter your choice: "))
        if key == 1:
            insert_student()
        elif key == 2:
            read_student()
        elif key == 3:
            update_student()
        elif key == 4:
            delete_student()
        elif key == 5:
            exit()
        else:
            print("Invalid choice")

master_menu()

cursor.close()
conn.close()
