import csv
from pathlib import Path

from connect import get_connection


def import_from_csv(file_path: str):
    try:
        base_dir = Path(__file__).resolve().parent
        file = base_dir / file_path

        if not file.exists():
            print(f"File not found: {file}")
            return

        names = []
        phones = []

        with open(file, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)

            required_columns = {"first_name", "phone_number"}
            if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
                print("CSV must contain these headers: first_name, phone_number")
                return

            for row in reader:
                name = (row.get("first_name") or "").strip()
                phone = (row.get("phone_number") or "").strip()

                if name or phone:
                    names.append(name)
                    phones.append(phone)

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
            conn.commit()

        print("Contacts import finished.")
        print("No incorrect data found.")

    except Exception as e:
        print(f"Error importing contacts: {e}")


def add_or_update_contact(name: str, phone: str):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
            conn.commit()

        print("Contact added/updated successfully.")

    except Exception as e:
        print(f"Error adding/updating contact: {e}")


def search_contacts(term: str):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s);", (term,))
                rows = cur.fetchall()

        if not rows:
            print("No contacts found.")
        else:
            print("\n--- Search Results ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    except Exception as e:
        print(f"Error searching contacts: {e}")


def show_paginated_contacts(limit: int, offset: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
                rows = cur.fetchall()

        if not rows:
            print("No contacts found.")
        else:
            print("\n--- Paginated Contacts ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    except Exception as e:
        print(f"Error showing contacts: {e}")


def delete_contact(value: str):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s);", (value,))
            conn.commit()

        print("Contact deleted successfully.")

    except Exception as e:
        print(f"Error deleting contact: {e}")


def main_menu():
    while True:
        print("\n===== PhoneBook Application =====")
        print("1. Import contacts from CSV")
        print("2. Add or update contact")
        print("3. Search contacts")
        print("4. Show contacts with pagination")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            path = input("Enter CSV file path (e.g., contacts.csv): ").strip()
            import_from_csv(path)

        elif choice == "2":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            add_or_update_contact(name, phone)

        elif choice == "3":
            term = input("Enter search term: ").strip()
            search_contacts(term)

        elif choice == "4":
            limit = int(input("Enter limit: ").strip())
            offset = int(input("Enter offset: ").strip())
            show_paginated_contacts(limit, offset)

        elif choice == "5":
            value = input("Enter username or phone: ").strip()
            delete_contact(value)

        elif choice == "6":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main_menu()