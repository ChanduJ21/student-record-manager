import re

FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# Add student record
def add_student():
    try:
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        age = int(input("Enter age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        email = input("Enter email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email address.")

        course = input("Enter course: ").strip()

        if not course:
            raise ValueError("Course cannot be empty.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{email},{course}\n")

        print("\nStudent record saved successfully!")

    except ValueError as e:
        print("Invalid input:", e)

    except IOError as e:
        print("File error:", e)


# Display student records
def display_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\n===== Student Records =====")

        for record in records:
            name, age, email, course = record.strip().split(",")

            print("Name   :", name)
            print("Age    :", age)
            print("Email  :", email)
            print("Course :", course)
            print("-" * 30)

    except FileNotFoundError:
        print("No student record file found.")

    except IOError as e:
        print("File error:", e)

    except ValueError:
        print("Invalid record format in file.")


# Main menu
def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                display_students()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                print("Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid choice. Please enter a number.")


if __name__ == "__main__":
    main()
