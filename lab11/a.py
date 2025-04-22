import psycopg2
import csv
import re

conn = psycopg2.connect(
    database="phone_book",
    host="localhost",
    user="postgres",
    password="87779626062",
    port="5432"
)

def create_tables_and_procedures():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY, 
            name VARCHAR(50), 
            surname VARCHAR(50), 
            phone_number VARCHAR(50)
        """,
        """
        CREATE OR REPLACE FUNCTION search_records(pattern TEXT)
        RETURNS SETOF users AS $$
        BEGIN
            RETURN QUERY 
            SELECT * FROM users 
            WHERE name ILIKE '%' || pattern || '%' 
               OR surname ILIKE '%' || pattern || '%'
               OR phone_number ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE PROCEDURE insert_or_update_user(
            user_name VARCHAR, 
            user_phone VARCHAR
        )
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM users WHERE name = user_name) THEN
                UPDATE users SET phone_number = user_phone WHERE name = user_name;
            ELSE
                INSERT INTO users (name, phone_number) VALUES (user_name, user_phone);
            END IF;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE PROCEDURE insert_many_users(
            INOUT invalid_data REFCURSOR,
            names_phones TEXT[][]
        )
        AS $$
        DECLARE
            item TEXT[];
            phone_pattern TEXT := '^[0-9]{10,15}$';
        BEGIN
            OPEN invalid_data FOR 
                SELECT 'Invalid data' as error_message;
                
            FOR item IN SELECT unnest(names_phones) LOOP
                IF array_length(item, 1) = 2 AND item[2] ~ phone_pattern THEN
                    CALL insert_or_update_user(item[1], item[2]);
                ELSE
                    OPEN invalid_data FOR 
                        SELECT item[1] as name, item[2] as phone 
                        WHERE array_length(item, 1) = 2
                        UNION ALL
                        SELECT * FROM invalid_data;
                END IF;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION get_users_paginated(
            lim INTEGER,
            offs INTEGER
        )
        RETURNS SETOF users AS $$
        BEGIN
            RETURN QUERY 
            SELECT * FROM users
            ORDER BY id
            LIMIT lim OFFSET offs;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE PROCEDURE delete_user(
            user_name VARCHAR DEFAULT NULL,
            user_phone VARCHAR DEFAULT NULL
        )
        AS $$
        BEGIN
            IF user_name IS NOT NULL THEN
                DELETE FROM users WHERE name = user_name;
            ELSIF user_phone IS NOT NULL THEN
                DELETE FROM users WHERE phone_number = user_phone;
            END IF;
        END;
        $$ LANGUAGE plpgsql;
        """
    ]
    
    try:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def search_by_pattern(pattern):
    try:
        with conn.cursor() as cur:
            cur.callproc('search_records', (pattern,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_or_update_user(name, phone):
    try:
        with conn.cursor() as cur:
            cur.callproc('insert_or_update_user', (name, phone))
            conn.commit()
            print(f"User '{name}' processed successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_many_users(users_list):
    try:
        with conn.cursor() as cur:
            # Convert Python list to PostgreSQL array format
            array_literal = "ARRAY[" + ",".join(["ARRAY[" + ",".join([f"'{u[0]}'", f"'{u[1]}'"]) + "]" for u in users_list]) + "]"
            
            # Call the procedure and get the invalid data
            cur.execute(f"BEGIN; DECLARE invalid_data CURSOR FOR CALL insert_many_users(NULL, {array_literal}); FETCH ALL FROM invalid_data; COMMIT;")
            
            # Get and print invalid data
            invalid_rows = cur.fetchall()
            if invalid_rows and invalid_rows[0][0] != 'Invalid data':
                print("Invalid data found:")
                for row in invalid_rows:
                    print(row)
            else:
                print("All data was valid and processed successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_users_paginated(limit, offset):
    try:
        with conn.cursor() as cur:
            cur.callproc('get_users_paginated', (limit, offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def delete_user(name=None, phone=None):
    try:
        with conn.cursor() as cur:
            if name:
                cur.callproc('delete_user', (name, None))
            elif phone:
                cur.callproc('delete_user', (None, phone))
            conn.commit()
            print("Delete operation completed")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Original functions from the previous implementation
def create_phone_book():
    create_tables_and_procedures()

def insert_console(name, surname, phone_number):
    command="INSERT INTO users(name, surname, phone_number) VALUES (%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, surname, phone_number)) 
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_from_csv(filename):
    command = """INSERT INTO users(name, surname, phone_number) VALUES(%s, %s, %s)"""
    try:
        with conn.cursor() as cur:
            with open(filename, "r") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                _ = next(csvreader) 
                for row in csvreader:
                    name, surname, telephone = row
                    cur.execute(command, (name, surname, telephone))
                    conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def change_name(old, new):
    command="UPDATE users SET name=%s WHERE name=%s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (new, old))
            conn.commit()
            print(f"Name '{old}' successfully changed to '{new}'")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def change_number(old, new):
    command="UPDATE users SET phone_number=%s WHERE phone_number=%s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (new, old))
            conn.commit()
            print(f"Number '{old}' successfully changed to '{new}'")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def show():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            print(row)

def query_by_name(name):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE name = %s", (name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

def query_by_surname(surname):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE surname = %s", (surname,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

def query_by_name_length():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE LENGTH(name)>5")
        rows = cur.fetchall()
        for row in rows:
            print(row)

def delete_by_name(name):
    delete_user(name=name)

def delete_all():
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users")
        conn.commit()

while True:
    print("\nWelcome to my PhoneBook! This is the menu I created:")
    print("0. Create phone book and setup procedures")
    print("1. Add contact through Console")
    print("2. Add contact through CSV file")
    print("3. Update contacts (name or phone)")
    print("4. Search by pattern (name, surname or phone part)")
    print("5. Insert or update user by name and phone")
    print("6. Insert many users with validation")
    print("7. Get users with pagination")
    print("8. Delete user by name or phone")
    print("9. Query by name")
    print("10. Query by surname")
    print("11. Query by name length (>5 chars)")
    print("12. Show all contacts")
    print("13. Delete all contacts")
    print("14. Exit")
   
    try:
        a = int(input("Choose an option: "))
        
        if a == 0:
            create_phone_book()
        elif a == 1:
            name = input("Input name: ")
            surname = input("Input surname: ")
            phone_number = input("Input phone number: ")
            insert_console(name, surname, phone_number)
        elif a == 2:
            insert_from_csv("contacts.csv")
        elif a == 3:
            b = int(input("What do you want to change?\n1. Name\n2. Phone number\n"))
            if b == 1:
                old = input("What name do you want to change? ")
                new = input("What is the new name? ")
                change_name(old, new)
            elif b == 2:
                old = input("What number do you want to change? ")
                new = input("What is the new number? ")
                change_number(old, new)
        elif a == 4:
            pattern = input("Enter search pattern: ")
            search_by_pattern(pattern)
        elif a == 5:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif a == 6:
            users = []
            print("Enter users (name and phone), type 'done' when finished:")
            while True:
                entry = input("Enter name and phone separated by space: ")
                if entry.lower() == 'done':
                    break
                parts = entry.split()
                if len(parts) >= 2:
                    users.append((parts[0], ' '.join(parts[1:])))
            if users:
                insert_many_users(users)
        elif a == 7:
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            get_users_paginated(limit, offset)
        elif a == 8:
            b = int(input("Delete by:\n1. Name\n2. Phone\n"))
            if b == 1:
                name = input("Enter name to delete: ")
                delete_user(name=name)
            elif b == 2:
                phone = input("Enter phone to delete: ")
                delete_user(phone=phone)
        elif a == 9:
            name = input("Enter name to search: ")
            query_by_name(name)
        elif a == 10:
            surname = input("Enter surname to search: ")
            query_by_surname(surname)
        elif a == 11:
            query_by_name_length()
        elif a == 12:
            show()
        elif a == 13:
            delete_all()
        elif a == 14:
            break
        else:
            print("Invalid option, please try again.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

conn.close()