# Record Manager

## Overview
This is a simple inventory record management system implemented in Python using the Tkinter library for the graphical user interface. The program allows users to input quantities of various materials, such as Kota, Marble, Granite, etc., and save these records to a CSV file. Additionally, it provides options to create new records, save records, calculate totals, create new CSV files, and clear input boxes.

## Requirements
- Python 3.x
- Tkinter
- pandas

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/JILSPATEL/record_manager.git
   cd your-repo
   ```

2. Run the program:
   ```bash
   python Final.py
   ```

## Features
- **Graphical User Interface:** Utilizes Tkinter for a user-friendly interface.
- **Data Storage:** Records are stored in CSV files, and a new CSV file is created for each day's records.
- **Options:**
  - **Save Record:** Save the current input record to the daily CSV file.
  - **Add New Record:** Create a new CSV file for the current day.
  - **Create New File:** Create a new CSV file (not necessarily for the current day).
  - **Clear Boxes:** Clear all input boxes.
  - **Total All Records:** Calculate the sum of specified columns and save the totals to a separate CSV file.

## Notes
- Each day's records are stored in a separate CSV file named `record_YYYY-MM-DD.csv`.
- The program automatically creates a new CSV file for each day if it doesn't exist.
- The total of all records is calculated and saved to `daily_records_2023-24.csv`.

## Contributors
- Jils Patel (@JILSPATEL)

Feel free to contribute, report issues, or suggest improvements!
