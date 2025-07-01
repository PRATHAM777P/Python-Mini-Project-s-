# Expense Tracker

A feature-rich command-line application for tracking and analyzing personal expenses.

**Author:** Prathamesh  
**Version:** 1.0.0

## Features

- 📊 Track expenses by category and date
- 💾 Persistent data storage using JSON
- 🔍 Filter expenses by category or month
- 📈 Analyze spending patterns
- 🎨 Colorful and user-friendly interface

## Requirements

- Python 3.6 or higher
- Colorama package for colored terminal output

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install colorama
```

## Usage

Run the application using Python:

```bash
python Expense_Tracker.py
```

### Main Menu Options

1. **Add Expense** - Record a new expense with date, amount, category, and description
2. **Add Category** - Create a new expense category
3. **View All Expenses** - Display all recorded expenses
4. **View Expenses by Category** - Filter expenses by a specific category
5. **View Expenses by Month** - Filter expenses by a specific month (YYYY-MM)
6. **View Categories** - List all available expense categories
7. **Analyze Expenses** - View spending analysis by category and month
8. **Exit** - Close the application

### Data Storage

All expense data is automatically saved to a file named `expenses.json` in the same directory as the application. This ensures your data persists between sessions.

## Example Usage

1. Start by adding some expense categories (e.g., Food, Transportation, Entertainment)
2. Add expenses with dates, amounts, and appropriate categories
3. View your expenses filtered by category or month
4. Analyze your spending patterns to identify areas for potential savings

## Tips

- Use the YYYY-MM-DD format for dates (e.g., 2023-05-15)
- Add descriptive notes to your expenses for better tracking
- Regularly analyze your spending patterns to identify trends

## License

This project is open source and available for personal and educational use.

## 🛠️ Description

- **Add Expense:** Users can input the date, amount, and category of their expenses. The expenses are stored and categorized for future reference.
  
- **Add Category:** Users can create new categories to classify their expenses, ensuring a customized tracking experience.

- **View Expenses:** Users can view the total expenses for each category, helping them understand where their money is going.

- **View Categories:** Users can view a list of available categories, making it convenient to track expenses related to specific areas of their life.



1. **Add Expense:**
    - Select option 1 from the menu.
    - Enter the date of the expense in the format `YYYY-MM-DD`.
    - Enter the amount of the expense.
    - Enter the category of the expense.
    
2. **Add Category:**
    - Select option 2 from the menu.
    - Enter the name of the new category.
    
3. **View Expenses:**
    - Select option 3 from the menu.
    - The application will display the total expenses for each category.
    
4. **View Categories:**
    - Select option 4 from the menu.
    - The application will display a list of available categories.
    
5. **Exit:**
    - Select option 5 from the menu to exit the Expense Tracker application.

## ⚙️ Languages or Frameworks Used

This application requires Python to run. No external libraries are used, making it easy to set up and run on any system with Python installed.

## 🌟 How to run

1. Ensure you have Python installed on your system.

2. Download the `expense_tracker.py` file from this repository.

3. Open a terminal or command prompt and navigate to the directory where `expense_tracker.py` is saved.

4. Run the following command:

 ```sh
python expense_tracker.py
```

## 📝 Acknowledgments
- [Python](https://www.python.org/)
- [VS Code](https://code.visualstudio.com/)

