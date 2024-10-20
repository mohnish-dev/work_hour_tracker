import os

class WorkHourTracker:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.first_time_use()

    def first_time_use(self):
        """Initialize the data file with column titles."""
        with open(self.filename, "w") as my_file:
            titles = ["Line No.\t", "Date\t\t", "Hours\t\t", "Employer\n"]
            my_file.writelines(titles)

    def input_data(self, date, hours, employer):
        """Append a new entry to the file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            line_number = len(lines)
            new_line = f"{line_number:<9}\t{date:<16}{hours:<16}{employer}\n"

            with open(self.filename, "a") as file:
                file.write(new_line)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def read_data(self):
        """Read the entire content of the file."""
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
            return ""

    def edit_line(self, line_number, new_date, new_hours, new_employer):
        """Edit an existing entry in the file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            if 0 < line_number < len(lines):
                lines[line_number] = f"{line_number:<9}\t{new_date:<16}{new_hours:<16}{new_employer}\n"

                with open(self.filename, "w") as file:
                    file.writelines(lines)
            else:
                print("Invalid line number.")
        except IOError as e:
            print(f"An error occurred while editing the file: {e}")

    def delete_line(self, line_number):
        """Delete a specific line from the file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            if 0 < line_number < len(lines):
                lines.pop(line_number)

                # Update line numbers
                for i in range(1, len(lines)):
                    parts = lines[i].strip().split()
                    if len(parts) == 4:
                        date, hours, employer = parts[1], parts[2], parts[3]
                        lines[i] = f"{i:<9}\t{date:<16}{hours:<16}{employer}\n"

                with open(self.filename, "w") as file:
                    file.writelines(lines)
            else:
                print("Invalid line number.")
        except IOError as e:
            print(f"An error occurred while deleting the line: {e}")
