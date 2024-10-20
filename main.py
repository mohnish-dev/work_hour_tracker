from work_hour_tracker import WorkHourTracker

def main():
    tracker = WorkHourTracker()
    print("Welcome to Work Hour Tracker!", "\n")

    while True:
        print("0 - Input data")
        print("1 - Read data")
        print("2 - Edit data")
        print("3 - Delete a line")
        print("4 - Erase everything (Select this ONLY if you want to erase all data)")
        print("5 - Exit", "\n")

        choice = input("Make selection: ").strip()

        if choice == "0":
            print(tracker.read_data())
            date = input("Enter date (YYYY-MM-DD): ").strip()
            hours = input("Enter hours worked: ").strip()
            employer = input("Enter the employer: ").strip()
            tracker.input_data(date, hours, employer)

        elif choice == "1":
            print(tracker.read_data())

        elif choice == "2":
            print(tracker.read_data())
            line_number = input("Enter line number: ").strip()
            if line_number.isdigit():
                line_number = int(line_number)
                new_date = input("Enter new date (YYYY-MM-DD): ").strip()
                new_hours = input("Enter new hours: ").strip()
                new_employer = input("Enter new employer: ").strip()
                tracker.edit_line(line_number, new_date, new_hours, new_employer)
            else:
                print("Invalid line number.")

        elif choice == "3":
            print(tracker.read_data())
            line_number = input("Enter line number: ").strip()
            if line_number.isdigit():
                line_number = int(line_number)
                tracker.delete_line(line_number)
            else:
                print("Invalid line number.")

        elif choice == "4":
            confirmation = input("Are you sure you want to erase all data? (y/n): ").strip().lower()
            if confirmation == "y":
                tracker.first_time_use()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        # Ask user if they want to return to the main menu
        continue_more = input("Would you like to go to the main menu? [y/n] ").strip().lower()
        if continue_more in ['n', 'no']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
