# Library System

A simple Library System in Python that allows adding, borrowing, and returning books. The system is developed using Test-Driven Development (TDD) principles and adheres to SOLID design principles.

## Features

- **Add Book**: Add a book to the library.
- **Borrow Book**: Borrow a book from the library if available.
- **Return Book**: Return a borrowed book to the library.
- **Search Books**: Search for available books by title.
- **Get Available Books**: Retrieve a list of all available books in the library.
  
## Requirements

### Add Books:

- Users should be able to add new books to the library.
- Each book should have a unique identifier (e.g., ISBN), title, author, and publication year.

### Borrow Books:

- Users should be able to borrow a book from the library.
- The system should ensure that the book is available before allowing it to be borrowed.
- If the book is not available, the system should raise an appropriate error.

### Return Books:

- Users should be able to return a borrowed book.
- The system should update the availability of the book accordingly.

### View Available Books:

- Users should be able to view a list of all available books in the library.

## Solution
The project is developed using Test-Driven Development (TDD) principles and follows clean coding practices.
## Installation

### Prerequisites

Ensure you have Python installed. You can check your Python version using the command:

```bash
python --version
```

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Dhruv942/Library-management-system--tdd-kata.git
cd Library-management-system--tdd-kata
```

### Test Result

![Test Result](https://github.com/Dhruv942/Library-management-system--tdd-kata/blob/main/test%20result.jpg)

### Test Report

```bash
   python -m unittest discover -v > test_report.txt
```

![Test Report](https://github.com/Dhruv942/Library-management-system--tdd-kata/blob/main/test%20report.jpg)
