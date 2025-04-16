import psycopg2
import csv

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="87779626062",
    port="5432",
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    surname VARCHAR(255),
    name VARCHAR(255),
    number VARCHAR(20)
);
""")
conn.commit()

#Add contact manually
def add_manual():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (surname, name, number) VALUES (%s, %s, %s)", (surname, name, number))
    conn.commit()
    print("Contact added successfully.\n")

#Import from CSV
def add_from_csv():
    filename = input("Enter filename (without .csv): ")
    try:
        with open(f"{filename}.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 3:
                    cur.execute("INSERT INTO PhoneBook (surname, name, number) VALUES (%s, %s, %s)", row)
            conn.commit()
            print("Import completed successfully.\n")
    except FileNotFoundError:
        print("File not found.\n")

#Update contact
def update_contact():
    show_all()
    contact_id = input("Enter contact ID to update: ")
    field = input("What to update? (surname/name/number): ")
    new_value = input("Enter new value: ")

    if field not in ["surname", "name", "number"]:
        print("Invalid field.")
        return

    sql = f"UPDATE PhoneBook SET {field} = %s WHERE id = %s"
    cur.execute(sql, (new_value, contact_id))
    conn.commit()
    print("Contact updated successfully.\n")

#Delete contact
def delete_contact():
    show_all()
    contact_id = input("Enter contact ID to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE id = %s", (contact_id,))
    conn.commit()
    print("Contact deleted successfully.\n")

# Search contacts
def search_contacts():
    print("\nSearch filters:")
    print("1. By surname")
    print("2. By name")
    print("3. By phone number")
    print("4. Show all")
    choice = input("Select filter: ")

    if choice == '1':
        val = input("Enter surname: ")
        cur.execute("SELECT * FROM PhoneBook WHERE surname ILIKE %s", (f"%{val}%",))
    elif choice == '2':
        val = input("Enter name: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s", (f"%{val}%",))
    elif choice == '3':
        val = input("Enter phone number: ")
        cur.execute("SELECT * FROM PhoneBook WHERE number LIKE %s", (f"%{val}%",))
    elif choice == '4':
        cur.execute("SELECT * FROM PhoneBook")
    else:
        print("Invalid choice.")
        return

    rows = cur.fetchall()
    if rows:
        print("\nSearch results:")
        for r in rows:
            print(f"ID: {r[0]}, Surname: {r[1]}, Name: {r[2]}, Phone: {r[3]}")
    else:
        print("No contacts found.\n")

#Show all contacts
def show_all():
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    print("\nCurrent contacts:")
    for r in rows:
        print(f"ID: {r[0]}, Surname: {r[1]}, Name: {r[2]}, Phone: {r[3]}")
    print()

#Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add contact manually")
        print("2. Import from CSV")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search contacts")
        print("6. Show all contacts")
        print("7. Exit")

        choice = input("Select action (1-7): ")
        if choice == '1':
            add_manual()
        elif choice == '2':
            add_from_csv()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contacts()
        elif choice == '6':
            show_all()
        elif choice == '7':
            break
        else:
            print("Invalid input.\n")

    cur.close()
    conn.close()
    print("Application closed.")

if __name__ == "__main__":
    main()