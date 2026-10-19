# PYTHON-FOR-DE
Python for Data Engineering
A hands-on Python learning repository covering core Python, object-oriented programming, decorators, multithreading, and Pydantic as part of my journey toward Data Engineering.
About This Repository
This repository contains practice scripts and a Jupyter Notebook created while learning Python concepts that are useful when building maintainable data-processing applications and data workflows.

The goal is to strengthen Python fundamentals through practical examples and build a foundation for future topics such as data cleaning, ETL pipelines, workflow orchestration, and cloud data platforms.
Status: Learning and practice repository. The examples are for educational purposes and are not presented as a production-ready data engineering solution.

Topics Covered
File	Topic	What I Practise
1_basics.py	Python Basics	Core syntax and fundamental Python concepts
2_constructor.py	Constructors	Initialising objects and using __init__()
3_encapsulation.py	Encapsulation	Organising data and behaviour within classes
4_DataExt_Class.py	Data Extraction Class	Using a class to organise data-extraction examples, including reading JSON or Parquet data where implemented
5_Class Methods And static method.py	Class and Static Methods	Understanding @classmethod and @staticmethod
6_inheritance.py	Inheritance	Reusing and extending class behaviour
7_Polymorphism.py	Polymorphism	Using a common interface with different behaviours
8_Decorators.py	Decorators	Wrapping functions to add reusable behaviour
9_Multi_Threading.py	Multithreading	Exploring concurrent execution with threads
10_Pydantic.ipynb	Pydantic	Practising data validation and typed data models in a notebook


The descriptions above summarise the topics indicated by the filenames. Check each script for the exact examples and implementation details.
Repository Structure
Python-for-Data-Engineering/
├── README.md
├── 1_basics.py
├── 2_constructor.py
├── 3_encapsulation.py
├── 4_DataExt_Class.py
├── 5_Class Methods And static method.py
├── 6_inheritance.py
├── 7_Polymorphism.py
├── 8_Decorators.py
├── 9_Multi_Threading.py
└── 10_Pydantic.ipynb
Getting Started
Prerequisites
- Python 3.11 or a compatible Python 3 version
- A code editor such as Visual Studio Code
- Jupyter support to open and run 10_Pydantic.ipynb
1. Clone the repository
Replace the placeholder with your GitHub repository URL:
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd <YOUR-REPOSITORY-FOLDER>
2. Create a virtual environment (recommended)
Windows PowerShell:
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
You can run scripts using the virtual environment's Python executable even if PowerShell blocks environment activation.
3. Install the dependency for the Pydantic notebook
.\.venv\Scripts\python.exe -m pip install pydantic
Install any other third-party packages only if the particular script requires them.
4. Run a Python script
For example:
.\.venv\Scripts\python.exe 1_basics.py
Run another script by replacing the filename with the script you want to practise. Open 10_Pydantic.ipynb in VS Code with the Jupyter extension or in a Jupyter environment.
Key Learning Goals
- Build confidence with Python syntax and core programming concepts.
- Understand object-oriented programming and code reuse.
- Practise decorators and multithreading.
- Explore validation of structured data with Pydantic.
- Develop a foundation for future data engineering work.
Next Steps
Planned areas to explore as my learning progresses:
- Python file handling and exception handling
- Pandas for data cleaning and transformation
- Working with CSV, JSON, and Parquet files
- SQL and Python integration
- Building a practical ETL pipeline
- Logging, testing, and workflow automation
These are future learning goals, not claims that all of these topics are already implemented in this repository.
