# Library_Management-_System-
This is a Python-based library management system that allows staff to manage students borrowing and returning books.  It tracks borrowing dates, calculates late return fines, and stores data in Excel files.

## Features
- Staff login with ID verification
- Students can borrow books
- Students can return books with automatic fine calculation for late returns
- Maintains records of all students and books in Excel
- Displays staff and student details upon request

## Technologies Used
- Python
- pandas
- datetime
- random
- Excel files for data storage

## How to Run
1. Install Python 3.x
2. Install required libraries: pip install pandas openpyxl
3. Place "staff_details.xlsx" and "Student_details.xlsx" in the same folder as the Python script.
4. Run "Library_management_system.py" using Python.

## Usage
- Follow on-screen prompts for staff login and student borrowing/returning.
- Ensure correct Excel files are present in the folder.

## Notes
- Student IDs are generated automatically when borrowing books.
- Late returns beyond 10 days makes a fine of Rs.100.
