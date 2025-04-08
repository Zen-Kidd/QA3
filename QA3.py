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

# Define placeholder questions for each course.
# Each tuple: (question, option_a, option_b, option_c, option_d, correct_answer)
placeholder_questions = {
    "ACCT-2110": [
        ("[ACCT-2110 Q1] What is the accounting equation?", 
         "Assets = Liabilities + Equity", "Assets = Expenses + Equity", 
         "Assets = Revenues - Expenses", "None of the above", 
         "Assets = Liabilities + Equity"),
        ("[ACCT-2110 Q2] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ACCT-2110 Q3] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ACCT-2110 Q4] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ACCT-2110 Q5] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ACCT-2110 Q6] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ACCT-2110 Q7] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ACCT-2110 Q8] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ACCT-2110 Q9] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ACCT-2110 Q10] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
    ],
    "DS-3850": [
        ("[DS-3850 Q1] What is data science?", 
         "Definition A", "Definition B", "Definition C", "Definition D", 
         "Definition B"),
        ("[DS-3850 Q2] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[DS-3850 Q3] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[DS-3850 Q4] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[DS-3850 Q5] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[DS-3850 Q6] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[DS-3850 Q7] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[DS-3850 Q8] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[DS-3850 Q9] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[DS-3850 Q10] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
    ],
    "DS-3860": [
        ("[DS-3860 Q1] What is machine learning?", 
         "Definition A", "Definition B", "Definition C", "Definition D", 
         "Definition C"),
        ("[DS-3860 Q2] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[DS-3860 Q3] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[DS-3860 Q4] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[DS-3860 Q5] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[DS-3860 Q6] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[DS-3860 Q7] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[DS-3860 Q8] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[DS-3860 Q9] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[DS-3860 Q10] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
    ],
    "ECON-2020": [
        ("[ECON-2020 Q1] What is the law of demand?", 
         "Definition A", "Definition B", "Definition C", "Definition D", 
         "Definition A"),
        ("[ECON-2020 Q2] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ECON-2020 Q3] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ECON-2020 Q4] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ECON-2020 Q5] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ECON-2020 Q6] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ECON-2020 Q7] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ECON-2020 Q8] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ECON-2020 Q9] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ECON-2020 Q10] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
    ],
    "ECON-3610": [
        ("[ECON-3610 Q1] What is macroeconomics?", 
         "Definition A", "Definition B", "Definition C", "Definition D", 
         "Definition D"),
        ("[ECON-3610 Q2] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ECON-3610 Q3] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ECON-3610 Q4] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ECON-3610 Q5] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ECON-3610 Q6] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
        ("[ECON-3610 Q7] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option B"),
        ("[ECON-3610 Q8] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option C"),
        ("[ECON-3610 Q9] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option D"),
        ("[ECON-3610 Q10] Sample question?", "Option A", "Option B", "Option C", "Option D", "Option A"),
    ],
}