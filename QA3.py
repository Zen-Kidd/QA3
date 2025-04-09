#Ian Neely
#Quarterly Assessment 3
#DS 3850-001
#Due: April 13, 2025

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ----------------------------
# Database Setup & Placeholders
# ----------------------------

DATABASE_FILENAME = "quiz_bowl.db"
course_tables = ["ACCT-2110", "DS-3850", "DS-3860", "ECON-2020", "ECON-3610"]

# Updated placeholder questions for each course.
# Each tuple: (question, option_a, option_b, option_c, option_d, correct_answer)
placeholder_questions = {
    "ACCT-2110": [
        ("[ACCT-2110 Q1] What is the accounting equation?",
         "Assets = Liabilities + Equity",
         "Assets = Expenses + Equity",
         "Assets = Revenues - Expenses",
         "None of the above",
         "Assets = Liabilities + Equity"),
        ("[ACCT-2110 Q2] What is the primary purpose of financial accounting?",
         "To determine tax liability",
         "To track personal expenses",
         "To provide information to external users",
         "To manage employee performance",
         "To provide information to external users"),
        ("[ACCT-2110 Q3] Which of the following is classified as an asset?",
         "Accounts payable",
         "Equipment",
         "Owner's Equity",
         "Sales revenue",
         "Equipment"),
        ("[ACCT-2110 Q4] Which financial statement shows a companys financial position at a specific point in time?",
         "Income Statement",
         "Satement of cash flows",
         "Balance Sheet",
         "Statement of Taxes",
         "Balance Sheet"),
        ("[ACCT-2110 Q5] Which account would typically have a credit balance?",
         "Service Revenue",
         "Cash",
         "Accounts Receivable",
         "Supplies",
         "Service Revenue"),
        ("[ACCT-2110 Q6] Which of the following is considered a liability?",
         "Inventory",
         "Prepaid Rent",
         "Office Equipment",
         "Wages Payable",
         "Wages Payable"),
        ("[ACCT-2110 Q7] What does the income statement report?",
         "Financial position at year-end",
         "Financial position at year-end",
         "Financial position at year-end",
         "Financial position at year-end",
         "Financial position at year-end"),
        ("[ACCT-2110 Q8] Which of the following is an example of an expense?",
         "Accounts receivable",
         "Utilities expense",
         "Retained earnings",
         "Notes payable",
         "Utilities expense"),
        ("[ACCT-2110 Q9] A debit to an asset account indicates",
         "A decrease in the asset",
         "An increase in the asset",
         "A decrease in owners equity",
         "An increase in liability",
         "An increase in the asset"),
        ("[ACCT-2110 Q10] When a company receives cash from a customer for a future service, it should record:",
         "Revenue",
         "Owners equity",
         "An expense",
         "An asset and a liability",
         "An asset and a liability"),
    ],
    "DS-3850": [
        ("[DS-3850 Q1] What is the correct way to output \"Hello, World!\" in Python?",
         "echo \"Hello, World!\"",
         "printf(\"Hello, World!\")",
         "print(\"Hello, World!\")",
         "println(\"Hello, World!\")",
         "print(\"Hello, World!\")"),
        ("[DS-3850 Q2] What will the following code output?: print(type(\"5\"))",
         "<class 'int'>",
         "<class 'float'>",
         "<class 'str'>",
         "<class 'bool'>",
         "<class 'str'>"),
        ("[DS-3850 Q3] Which of the following is a correct variable name in Python?",
         "first_name",
         "first_name",
         "first-name",
         "1st_name",
         "first_name"),
        ("[DS-3850 Q4] What class type contains a decimal point?",
         "String",
         "Integer",
         "Boolean",
         "Float",
         "Float"),
        ("[DS-3850 Q5] What does the len() function do?",
         "Returns the length of a list or string",
         "Converts an integer to a string",
         "Adds two numbers",
         "Terminates a loop",
         "Returns the length of a list or string"),
        ("[DS-3850 Q6] Which of the following is used to define a function in Python?",
         "define",
         "func",
         "def",
         "function",
         "def"),
        ("[DS-3850 Q7] Which of the following is a valid Python list?",
         "{1, 2, 3}",
         "[1, 2, 3]",
         "(1, 2, 3)",
         "<1, 2, 3>",
         "[1, 2, 3]"),
        ("[DS-3850 Q8] Which class type returns a true/false value?",
         "int",
         "str",
         "bool",
         "float",
         "bool"),
        ("[DS-3850 Q9] How do you start a comment in Python?",
         "*",
         "//",
         "~",
         "#",
         "#"),
        ("[DS-3850 Q10] What is the output of this code?: print(10 // 3)",
         "3.33",
         "3",
         "4",
         "3.0",
         "3"),
    ],
    "DS-3860": [
        ("[DS-3860 Q1] What does SQL stand for?",
         "Structured Query Language",
         "Standard Question Language",
         "Sequential Query Language",
         "Simple Query Language",
         "Structured Query Language"),
        ("[DS-3860 Q2] Which SQL command is used to retrieve data from a database?",
         "GET",
         "SELECT",
         "FETCH",
         "SHOW",
         "SELECT"),
        ("[DS-3860 Q3] In a relational database, data is organized into:",
         "Arrays",
         "Trees",
         "Tables",
         "Graphs",
         "Tables"),
        ("[DS-3860 Q4] Which of the following is used to remove all records from a table, but not the table itself?",
         "DELETE",
         "DROP",
         "REMOVE",
         "TRUNCATE",
         "TRUNCATE"),
        ("[DS-3860 Q5] What is a primary key?",
         "A column that stores the name of a table",
         "A column that uniquely identifies each row in a table",
         "A column that allows null values",
         "A duplicate column in the table",
         "A column that uniquely identifies each row in a table"),
        ("[DS-3860 Q6] What does the WHERE clause do in an SQL statement?",
         "Specifies the database",
         "Adds a new table",
         "Filters records based on conditions",
         "Sorts the output",
         "Filters records based on conditions"),
        ("[DS-3860 Q7] Which of the following is a valid SQL data type?",
         "textfile",
         "numberfield",
         "VARCHAR",
         "charstr",
         "VARCHAR"),
        ("[DS-3860 Q8] What is the purpose of a foreign key?",
         "To uniquely identify rows within its own table",
         "To encrypt data",
         "To establish a link between two tables",
         "To prevent data from being deleted",
         "To establish a link between two tables"),
        ("[DS-3860 Q9] What is normalization in databases?",
         "Organizing data to reduce redundancy",
         "Backing up data",
         "Creating indexes",
         "Deleting duplicate records",
         "Organizing data to reduce redundancy"),
        ("[DS-3860 Q10] Which SQL command is used to update data in a table?",
         "MODIFY",
         "UPDATE",
         "CHANGE",
         "SET",
         "UPDATE"),
    ],
    "ECON-2020": [
        ("[ECON-2020 Q1] What does GDP stand for?",
         "Gross Domestic Product",
         "General Domestic Price",
         "Government Debt Policy",
         "Gross Development Plan",
         "Gross Domestic Product"),
        ("[ECON-2020 Q2] Which of the following is not included in GDP?",
         "Consumer spending",
         "Government spending",
         "Illegal drug sales",
         "Business investment",
         "Illegal drug sales"),
        ("[ECON-2020 Q3] What is inflation?",
         "A rise in employment",
         "A general increase in prices",
         "A decrease in taxes",
         "A decline in interest rates",
         "A general increase in prices"),
        ("[ECON-2020 Q4] Who controls monetary policy in the United States?",
         "Congress",
         "The Department of Commerce",
         "The President",
         "The Federal Reserve",
         "The Federal Reserve"),
        ("[ECON-2020 Q5] What is the natural rate of unemployment?",
         "Zero unemployment",
         "Unemployment due to economic recession",
         "Unemployment that exists when the economy is at full employment",
         "Only part-time job losses",
         "Unemployment that exists when the economy is at full employment"),
        ("[ECON-2020 Q6] Which of the following is a tool of fiscal policy?",
         "Interest rates",
         "Reserve requirements",
         "Government spending",
         "Open market operations",
         "Government spending"),
        ("[ECON-2020 Q7] A budget deficit occurs when:",
         "Imports exceed exports",
         "GDP falls below potential",
         "Government spending exceeds government revenue",
         "Inflation falls to zero",
         "Government spending exceeds government revenue"),
        ("[ECON-2020 Q8] Which of the following best describes aggregate demand?",
         "The total demand for a single product",
         "The total quantity of goods and services demanded across all levels of an economy",
         "The demand of the government",
         "The total supply in the market",
         "The total quantity of goods and services demanded across all levels of an economy"),
        ("[ECON-2020 Q9] What is the term for a period of declining GDP and rising unemployment?",
         "Recession",
         "Recovery",
         "Inflation",
         "Boom",
         "Recession"),
        ("[ECON-2020 Q10] What happens during an economic expansion?",
         "GDP contracts and unemployment rises",
         "GDP grows and unemployment falls",
         "Taxes increase and spending decreases",
         "Interest rates are always high",
         "GDP grows and unemployment falls"),
    ],
    "ECON-3610": [
        ("[ECON-3610 Q1] What is the mean of the numbers 5, 10, 15, and 20?",
         "10",
         "12.5",
         "15",
         "11",
         "12.5"),
        ("[ECON-3610 Q2] Which measure of central tendency is most affected by outliers?",
         "Mean",
         "Mode",
         "Median",
         "Range",
         "Mean"),
        ("[ECON-3610 Q3] What does the standard deviation measure?",
         "The average value",
         "The middle value",
         "The spread or dispersion of data",
         "The most frequent value",
         "The spread or dispersion of data"),
        ("[ECON-3610 Q4] If the data distribution is symmetrical, then:",
         "Mean = Median = Mode",
         "Mean < Median < Mode",
         "Mean > Median > Mode",
         "Mode < Median < Mean",
         "Mean = Median = Mode"),
        ("[ECON-3610 Q5] Which of the following is a qualitative data type?",
         "Age",
         "Revenue",
         "Product category",
         "Weight",
         "Product category"),
        ("[ECON-3610 Q6] What is the probability of getting heads in a single fair coin toss?",
         "1",
         "0.5",
         "0.75",
         "0.25",
         "0.5"),
        ("[ECON-3610 Q7] A histogram is used to display:",
         "Categorical data",
         "Qualitative data",
         "Frequency of numerical data",
         " Relationships between two variables",
         "Frequency of numerical data"),
        ("[ECON-3610 Q8] What type of graph is best for showing parts of a whole?",
         "Line graph",
         "Bar chart",
         "Histogram",
         "Pie chart",
         "Pie chart"),
        ("[ECON-3610 Q9] Which term describes the likelihood of an event occurring?",
         "Variance",
         "Probability",
         "Correlation",
         "Distribution",
         "Probability"),
        ("[ECON-3610 Q10] In a normal distribution, approximately what percentage of data falls within one standard deviation of the mean?",
         "50%",
         "68%",
         "Option C",
         "99.7%",
         "68%"),
    ],
}

def initialize_database():
    """Initialize the SQLite database, creating tables and inserting placeholders if needed."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    for table in course_tables:
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS "{table}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_answer TEXT
        );
        '''
        cursor.execute(create_table_sql)
        print(f"Table '{table}' created (or already exists).")

        cursor.execute(f'SELECT COUNT(*) FROM "{table}";')
        count = cursor.fetchone()[0]
        print(f"'{table}' currently has {count} rows.")

        if count < 10:
            rows_to_insert = 10 - count
            if table in placeholder_questions:
                insert_values = placeholder_questions[table][count:count + rows_to_insert]
                insert_sql = f'''
                INSERT INTO "{table}" (question, option_a, option_b, option_c, option_d, correct_answer)
                VALUES (?, ?, ?, ?, ?, ?);
                '''
                cursor.executemany(insert_sql, insert_values)
                conn.commit()
                print(f"Inserted {rows_to_insert} placeholder rows into '{table}'.")
            else:
                print(f"No placeholder questions defined for table '{table}'.")
        else:
            print(f"No new rows inserted into '{table}', already has 10 or more rows.")

    conn.close()
    print("Database initialization complete.")

# ----------------------------
# Database Helper Functions (Updated)
# ----------------------------

def get_questions(course):
    """Retrieve all questions for a given course as a list of Question objects."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    cursor.execute(f'SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM "{course}" ORDER BY id ASC;')
    rows = cursor.fetchall()
    conn.close()
    return [Question(*row) for row in rows]

def update_question(course, question_id, question_text, option_a, option_b, option_c, option_d, correct_answer):
    """Update a specific question in the database."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    update_sql = f'''
    UPDATE "{course}"
    SET question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_answer = ?
    WHERE id = ?;
    '''
    cursor.execute(update_sql, (question_text, option_a, option_b, option_c, option_d, correct_answer, question_id))
    conn.commit()
    conn.close()

def add_question(course, question_text, option_a, option_b, option_c, option_d, correct_answer):
    """Insert a new question into the database."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    insert_sql = f'''
    INSERT INTO "{course}" (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(insert_sql, (question_text, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()
    conn.close()

def delete_question(course, question_id):
    """Delete a specific question from the database."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    delete_sql = f'DELETE FROM "{course}" WHERE id = ?;'
    cursor.execute(delete_sql, (question_id,))
    conn.commit()
    conn.close()

# ----------------------------
# Question Class
# ----------------------------

class Question:
    def __init__(self, qid, question, option_a, option_b, option_c, option_d, correct_answer):
        self.qid = qid
        self.question = question
        self.options = {
            'A': option_a,
            'B': option_b,
            'C': option_c,
            'D': option_d
        }
        self.correct_answer = correct_answer.strip()

    def validate_answer(self, given_answer):
        answer = given_answer.strip()
        if answer.upper() in self.options:
            return self.options[answer.upper()] == self.correct_answer
        return answer == self.correct_answer
    
# ----------------------------
# Login Screen
# ----------------------------

def login_screen():
    """Display the login screen with options for Admin Access (password protected) or Quiz Taker Access."""
    root = tk.Tk()
    root.title("Quiz Bowl Login")
    root.geometry("400x300")
    ttk.Label(root, text="Quiz Bowl Application", font=("Arial", 18)).pack(pady=20)
    
    def admin_access():
        password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
        if password == "admin":
            root.destroy()
            app = placeholder()
            app.mainloop()
        else:
            messagebox.showerror("Access Denied", "Incorrect password.")
    
    def quiz_taker_access():
        messagebox.showinfo("placeholder", "not implemented yet")
    
    ttk.Button(root, text="Admin Access", command=admin_access).pack(pady=10, fill=tk.X, padx=20)
    ttk.Button(root, text="Quiz Taker Access", command=quiz_taker_access).pack(pady=10, fill=tk.X, padx=20)
    
    root.mainloop()

# ----------------------------
# Main Execution
# ----------------------------

if __name__ == "__main__":
    initialize_database()
    login_screen()
