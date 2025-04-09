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
    """Initialize the SQLite database by creating tables if they don't exist and inserting placeholder questions if needed."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    # Instead of dropping tables, we create tables only if they do not exist.
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
        print(f"Table '{table}' created or already exists.")

        # Count the current rows in the table.
        cursor.execute(f'SELECT COUNT(*) FROM "{table}";')
        count = cursor.fetchone()[0]
        print(f"'{table}' currently has {count} rows.")

        # Insert placeholder questions only if the table has fewer than 10 rows.
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
    """Update a specific question in the database permanently."""
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
    """Insert a new question into the database permanently."""
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
    """Delete a specific question from the database permanently."""
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()
    delete_sql = f'DELETE FROM "{course}" WHERE id = ?;'
    cursor.execute(delete_sql, (question_id,))
    conn.commit()
    conn.close()

def can_delete_question(course):
    """Return True if the course contains more than 10 questions; otherwise, deletion is not allowed."""
    questions = get_questions(course)
    return len(questions) > 10

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
# Edit Window (Modified to include Delete Prevention)
# ----------------------------

def open_edit_window(course, question_obj, refresh_callback=None):
    """Open a window to edit or delete a selected question permanently."""
    edit_win = tk.Toplevel()
    edit_win.title(f"Edit Question ID {question_obj.qid} - {course}")
    
    fields = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]
    current_values = [question_obj.question,
                      question_obj.options['A'],
                      question_obj.options['B'],
                      question_obj.options['C'],
                      question_obj.options['D'],
                      question_obj.correct_answer]
    entries = {}
    
    for idx, field in enumerate(fields):
        ttk.Label(edit_win, text=field + ":").grid(row=idx, column=0, sticky=tk.W, padx=5, pady=5)
        entry = ttk.Entry(edit_win, width=80)
        entry.insert(0, current_values[idx])
        entry.grid(row=idx, column=1, padx=5, pady=5)
        entries[field] = entry
    
    def save_changes():
        new_question = entries["Question"].get()
        new_a = entries["Option A"].get()
        new_b = entries["Option B"].get()
        new_c = entries["Option C"].get()
        new_d = entries["Option D"].get()
        new_correct = entries["Correct Answer"].get()
        update_question(course, question_obj.qid, new_question, new_a, new_b, new_c, new_d, new_correct)
        messagebox.showinfo("Success", f"Question ID {question_obj.qid} updated permanently.")
        if refresh_callback:
            refresh_callback()
        edit_win.destroy()
    
    def delete_current():
        # Prevent deletion if there are exactly 10 questions.
        if not can_delete_question(course):
            messagebox.showwarning("Deletion Not Allowed", "Cannot delete question because at least 10 questions must be maintained.")
            return
        if messagebox.askyesno("Confirm Delete", f"Delete question ID {question_obj.qid} permanently?"):
            delete_question(course, question_obj.qid)
            messagebox.showinfo("Deleted", f"Question ID {question_obj.qid} deleted permanently.")
            if refresh_callback:
                refresh_callback()
            edit_win.destroy()
    
    button_frame = ttk.Frame(edit_win)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10)
    ttk.Button(button_frame, text="Save Changes", command=save_changes).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="Delete Question", command=delete_current).pack(side=tk.LEFT, padx=5)

# ----------------------------
# Admin Dashboard and Navigation (New)
# ----------------------------

class AdminDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Dashboard")
        self.geometry("800x600")
        self.create_navigation()
        self.create_frames()
        self.show_frame("ViewQuestionsPage")
    
    def create_navigation(self):
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(nav_frame, text="View Questions", command=lambda: self.show_frame("ViewQuestionsPage")).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(nav_frame, text="Add New Question", command=lambda: self.show_frame("AddQuestionPage")).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(nav_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=5, pady=5)
    
    def create_frames(self):
        self.frames = {}
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        
        for F in (ViewQuestionsPage, AddQuestionPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "ViewQuestionsPage":
            frame.load_questions()
    
    def logout(self):
        self.destroy()
        login_screen()

class ViewQuestionsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.course_var = tk.StringVar(value=course_tables[0])
        
        top_frame = ttk.Frame(self)
        top_frame.pack(pady=10)
        ttk.Label(top_frame, text="Select Course:").pack(side=tk.LEFT)
        course_dropdown = ttk.OptionMenu(top_frame, self.course_var, course_tables[0], *course_tables, command=lambda _: self.load_questions())
        course_dropdown.pack(side=tk.LEFT, padx=5)
        
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        self.question_listbox = tk.Listbox(list_frame, width=80)
        self.question_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.question_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.question_listbox.config(yscrollcommand=scrollbar.set)
        
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected_question).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected_question).pack(side=tk.LEFT, padx=5)
    
    def load_questions(self):
        self.question_listbox.delete(0, tk.END)
        questions = get_questions(self.course_var.get())
        self.questions = questions
        for q in questions:
            display_text = f"ID {q.qid}: {q.question[:50]}..." if len(q.question) > 50 else f"ID {q.qid}: {q.question}"
            self.question_listbox.insert(tk.END, display_text)
    
    def edit_selected_question(self):
        try:
            index = self.question_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Selection Error", "Select a question to edit.")
            return
        question_obj = self.questions[index]
        open_edit_window(self.course_var.get(), question_obj, refresh_callback=self.load_questions)
    
    def delete_selected_question(self):
        try:
            index = self.question_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Selection Error", "Select a question to delete.")
            return
        if not can_delete_question(self.course_var.get()):
            messagebox.showwarning("Deletion Not Allowed", "Cannot delete question because at least 10 questions must be maintained.")
            return
        question_obj = self.questions[index]
        if messagebox.askyesno("Confirm Delete", f"Delete question ID {question_obj.qid}?"):
            delete_question(self.course_var.get(), question_obj.qid)
            messagebox.showinfo("Deleted", f"Question ID {question_obj.qid} deleted permanently.")
            self.load_questions()

class AddQuestionPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Add New Question", font=("Arial", 16)).pack(pady=10)
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10)
        ttk.Label(form_frame, text="Select Course:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        # Updated OptionMenu: include command to update self.course_var.
        self.course_var = tk.StringVar(value=course_tables[0])
        course_dropdown = ttk.OptionMenu(form_frame, self.course_var, self.course_var.get(), *course_tables, command=lambda value: self.course_var.set(value))
        course_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        fields = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]
        self.entries = {}
        for idx, field in enumerate(fields, start=1):
            ttk.Label(form_frame, text=field + ":").grid(row=idx, column=0, sticky=tk.W, padx=5, pady=5)
            entry = ttk.Entry(form_frame, width=80)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            self.entries[field] = entry
        
        ttk.Button(self, text="Add Question", command=self.add_question).pack(pady=10)
    
    def add_question(self):
        course = self.course_var.get()
        q_text = self.entries["Question"].get()
        opt_a = self.entries["Option A"].get()
        opt_b = self.entries["Option B"].get()
        opt_c = self.entries["Option C"].get()
        opt_d = self.entries["Option D"].get()
        correct = self.entries["Correct Answer"].get()
        if not (q_text and opt_a and opt_b and opt_c and opt_d and correct):
            messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
            return
        add_question(course, q_text, opt_a, opt_b, opt_c, opt_d, correct)
        messagebox.showinfo("Success", "Question added successfully and saved permanently.")
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# ----------------------------
# New: User Quiz Interface
# ----------------------------
# Critical changes:
# 1. Added QuizWelcomeScreen: provides a welcome and category selection screen.
# 2. Added QuizFrame: presents questions with multiple-choice options, provides immediate feedback, and tracks score.
# 3. Modified show_results() to add a "Return to Main Menu" button.

class QuizWelcomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Taker Welcome Screen")
        self.geometry("400x300")
        ttk.Label(self, text="Welcome to the Quiz!", font=("Arial", 18)).pack(pady=20)
        ttk.Label(self, text="Select a Quiz Category:").pack(pady=10)
        self.category_var = tk.StringVar(value=course_tables[0])
        category_dropdown = ttk.OptionMenu(self, self.category_var, course_tables[0], *course_tables)
        category_dropdown.pack(pady=10)
        ttk.Button(self, text="Start Quiz", command=self.start_quiz).pack(pady=20)
        
    def start_quiz(self):
        selected_course = self.category_var.get()
        self.destroy()  # Close the welcome screen
        quiz_win = tk.Tk()
        quiz_win.title(f"Quiz - {selected_course}")
        quiz_win.geometry("600x400")
        questions = get_questions(selected_course)
        quiz_frame = QuizFrame(quiz_win, selected_course, questions)
        quiz_frame.pack(fill=tk.BOTH, expand=True)
        quiz_win.mainloop()

class QuizFrame(tk.Frame):
    def __init__(self, master, course, questions):
        super().__init__(master)
        self.master = master
        self.course = course
        self.questions = questions
        self.current_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()
        self.processing = False  # Flag to prevent spam clicking.
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = ttk.Label(self, wraplength=500, justify=tk.LEFT)
        self.question_label.pack(pady=10)
        
        self.radio_buttons = {}
        for option in ['A', 'B', 'C', 'D']:
            rb = ttk.Radiobutton(self, text="", variable=self.selected_option, value=option)
            rb.pack(anchor=tk.W)
            self.radio_buttons[option] = rb
            
        self.submit_button = ttk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=10)
        
        self.feedback_label = ttk.Label(self, text="")
        self.feedback_label.pack(pady=5)

    def display_question(self):
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.question_label.config(text=f"Q{self.current_index + 1}: {q.question}")
            for option, rb in self.radio_buttons.items():
                rb.config(text=f"{option}: {q.options[option]}")
            self.selected_option.set("")
            self.feedback_label.config(text="")
            # Reset the processing state and re-enable the submit button.
            self.processing = False
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.show_results()

    def submit_answer(self):
        if self.processing:
            return
        if not self.selected_option.get():
            messagebox.showwarning("No Selection", "Please select an answer.")
            return
        self.processing = True
        self.submit_button.config(state=tk.DISABLED)
        current_q = self.questions[self.current_index]
        if current_q.validate_answer(self.selected_option.get()):
            self.feedback_label.config(text="Correct!", foreground="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect! Correct: {current_q.correct_answer}", foreground="red")
        self.current_index += 1
        self.after(1500, self.display_question)

    def show_results(self):
        for widget in self.winfo_children():
            widget.destroy()
        result_text = f"You scored {self.score} out of {len(self.questions)}."
        ttk.Label(self, text=result_text, font=("Arial", 16)).pack(pady=20)
        def return_to_main_menu():
            self.master.destroy()
            login_screen()
        ttk.Button(self, text="Return to Main Menu", command=return_to_main_menu).pack(pady=10)

# ----------------------------
# Login Screen (Modified)
# ----------------------------

def login_screen():
    """Display the login screen with options for Admin Access or Quiz Taker Access."""
    root = tk.Tk()
    root.title("Quiz Bowl Login")
    root.geometry("400x300")
    ttk.Label(root, text="Quiz Bowl Application", font=("Arial", 18)).pack(pady=20)
    
    def admin_access():
        # Updated admin password.
        password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
        if password == "goldeneagles2025":
            root.destroy()
            app = AdminDashboard()
            app.mainloop()
        else:
            messagebox.showerror("Access Denied", "Incorrect password.")
    
    def quiz_taker_access():
        root.destroy()
        welcome = QuizWelcomeScreen()
        welcome.mainloop()
    
    ttk.Button(root, text="Admin Access", command=admin_access).pack(pady=10, fill=tk.X, padx=20)
    ttk.Button(root, text="Quiz Taker Access", command=quiz_taker_access).pack(pady=10, fill=tk.X, padx=20)
    
    root.mainloop()

# ----------------------------
# Main Execution
# ----------------------------

if __name__ == "__main__":
    initialize_database()
    login_screen()



