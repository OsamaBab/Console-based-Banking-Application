Library Management System
Project Overview
This project aims to create a Python application that simulates a simple real-world library management system scenario involving the use of Object-Oriented Programming (OOP) techniques and principles such as classes, inheritance, encapsulation, abstraction and polymorphism in terms of managing a collection of library members and books via enabling the basic functionalities such as:

Add books / new members
Remove books / existent members
Borrow books
Return books
List available books
List borrowed books. Documentation is included to ensure clarity as well as Testing for usability and maintainability.
The System Features
Book Management Feature: Add and remove books from the library system. Member Management Feature: Add and remove members from the the library system. Borrowing/Returning Books Features: Enable the library members to borrow and return books. Books' Availability Checking Feature: List all exsistant and borrowed books with borrower's information. Library User' Types: Differentiate between members types as student and teacher.

System Structure
library_management_system 1.library_management/ 1.1. init.py 1.2. library.py
1.3. book.py
1.4. member.py
1.5. test_library.py
2. README.md
3. requirements.txt

Classes and Methods
Library
The Library class manages a collection of books and members.

Methods: add_book(book): Adds a book to the library's collection. remove_book(book): Removes a book from the collection. add_member(member): Registers a new member. remove_member(member): Removes an existing member. borrow_book(book, member): Allows a member to borrow a book if it is available. return_book(book, member): Allows a member to return a borrowed book. list_available_books(): Lists all books that are currently available. list_borrowed_books(): Lists all books currently borrowed, along with borrower details.

Book
The Book class represents each book in the library.

Attributes: title (str): Title of the book. author (str): Author of the book. is_borrowed (bool): Tracks if the book is currently borrowed.

Member
The Member class represents a library member with basic details.

Attributes: name (str): Name of the member. borrowed_books (list): List of books currently borrowed by the member. StudentMember and TeacherMember StudentMember and TeacherMember are subclasses of Member. StudentMember: May have additional borrowing restrictions. TeacherMember: Might have extended borrowing privileges.

Setup Instructions:
Python version or packages required. Instructions to install dependencies listed in requirements.txt (e.g., pip install -r requirements.txt

Usage Examples:
Examples such as adding books, borrowing books, etc usage. Classes and Methods: Explain each class and method with its purpose and parameters.

Detailed Problem-Solving Processse
Testing
Learning Outcomes By completing this assessment, you will be able to:

Evaluate Object-Oriented Programming techniques, associated tools, and Application Program Interfaces.

Analyze and document a complex task utilizing a range of problem-solving skills.

Functionality
The Library class should manage a collection of books and members.
Implement methods to:
Add and remove books from the library.
Add and remove members from the library.
Borrow and return books.
List available books.
List borrowed books and their borrowers.
Documentation and Analysis:
Document the problem-solving process, including:
Initial problem analysis.
Design decisions and rationale.
Challenges faced and solutions implemented.
Example usage of the classes and methods.
Use docstrings to document the classes and methods.
Include test cases to demonstrate the functionality of your code.
Project Structure
Here is a suggested project structure for your library management system:

library_management_system/
├── library_management/
│   ├── __init__.py
│   ├── library.py
│   ├── book.py
│   ├── member.py
│   └── test_library.py
├── README.md
└── requirements.txt
Detailed Instructions
Step 1: Create the Git Repository
  - Create a new repository on GitHub named library_management_system.
  - Clone the repository to your local machine.
  - Set up a basic directory structure as shown above.
Step 2: Implement the Classes and Methods
  - Library Class (library.py)
  - Book Class (book.py)
  - Member Class and Subclasses (member.py)
  - Test Cases (test_library.py)
Step 3: Documentation and Analysis
  1. README.md:
      - Provide an overview of the project.
      - Include setup instructions and usage examples.
      - Document the classes, methods, and their functionality.
      #### Classes and Methods
          - Library: Manages a collection of books and members.
              - add_book(book): Adds a book to the library.
              - remove_book(book): Removes a book from the library.
              - add_member(member): Adds a member to the library.
              - remove_member(member): Removes a member from the library.
              - borrow_book(book, member): Allows a member to borrow a book.
              - return_book(book, member): Allows a member to return a book.
              - list_available_books(): Lists all available books in the library.
              - list_borrowed_books(): Lists all borrowed books and their borrowers.
          - Book: Represents a book with a title and author.
          - Member: Represents a library member with a name and borrowed books.
          - StudentMember and TeacherMember: Subclasses of Member with additional attributes.
  2. Docstrings:
      - Add docstrings to all classes and methods explaining their purpose and usage.
Step 4: Submission
  1. GitHub Repository:
      - Ensure your repository is complete with all necessary files and documentation.
      - Provide a link to your GitHub repository.

  2. README.md:
      - Ensure the README file is comprehensive and clearly explains the project, setup instructions, and usage.

  3. Documentation:
      - Ensure all classes and methods are well-documented with docstrings.
      - Include a detailed analysis of the problem-solving process in the README or a separate documentation file.

  4. Test Cases:
      - Ensure the test cases cover all major functionalities and edge cases.
      - Verify that all tests pass successfully.
