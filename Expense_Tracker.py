import json
import os
import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

# Author information
__author__ = "Prathamesh"
__version__ = "1.0.0"

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.categories = set()
        self.data_file = "expenses.json"
        self.load_data()

    def load_data(self):
        """Load expense data from JSON file if it exists"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    self.expenses = data.get('expenses', {})
                    self.categories = set(data.get('categories', []))
                print(f"{Fore.GREEN}Data loaded successfully!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error loading data: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No existing data found. Starting fresh.{Style.RESET_ALL}")

    def save_data(self):
        """Save expense data to JSON file"""
        try:
            with open(self.data_file, 'w') as file:
                json.dump({
                    'expenses': self.expenses,
                    'categories': list(self.categories)
                }, file, indent=4)
            print(f"{Fore.GREEN}Data saved successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error saving data: {e}{Style.RESET_ALL}")

    def add_expense(self, date, amount, category, description=""):
        """Add a new expense"""
        if not self.is_valid_date(date):
            print(f"{Fore.RED}Invalid date format. Please use YYYY-MM-DD.{Style.RESET_ALL}")
            return False
            
        if category not in self.expenses:
            self.expenses[category] = []
        
        self.expenses[category].append({
            "date": date,
            "amount": amount,
            "description": description
        })
        
        self.categories.add(category)
        self.save_data()
        return True

    def is_valid_date(self, date_str):
        """Validate date format"""
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def add_category(self, category):
        """Add a new expense category"""
        if category not in self.categories:
            self.categories.add(category)
            print(f"{Fore.GREEN}Category '{category}' added successfully!{Style.RESET_ALL}")
            self.save_data()
        else:
            print(f"{Fore.YELLOW}Category '{category}' already exists.{Style.RESET_ALL}")

    def view_expenses(self, filter_category=None, filter_month=None):
        """View expenses with optional filtering"""
        if not self.expenses:
            print(f"{Fore.YELLOW}No expenses recorded yet.{Style.RESET_ALL}")
            return

        total_overall = 0
        categories_to_show = [filter_category] if filter_category else self.expenses.keys()
        
        print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'EXPENSE SUMMARY':^50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        
        for category in categories_to_show:
            if category not in self.expenses:
                print(f"{Fore.YELLOW}No expenses found for category '{category}'.{Style.RESET_ALL}")
                continue
                
            category_total = 0
            print(f"\n{Fore.MAGENTA}Category: {category}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'-' * 50}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'Date':<12} {'Amount':<10} {'Description'}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'-' * 50}{Style.RESET_ALL}")
            
            for expense in self.expenses[category]:
                date = expense["date"]
                
                # Apply month filter if specified
                if filter_month and not date.startswith(filter_month):
                    continue
                    
                amount = expense["amount"]
                description = expense.get("description", "")
                
                print(f"{date:<12} ${amount:<9.2f} {description}")
                category_total += amount
                
            total_overall += category_total
            print(f"{Fore.CYAN}{'-' * 50}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Category Total: ${category_total:.2f}{Style.RESET_ALL}")
            
        print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}OVERALL TOTAL: ${total_overall:.2f}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

    def view_categories(self):
        """View all expense categories"""
        if not self.categories:
            print(f"{Fore.YELLOW}No categories defined yet.{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.CYAN}{'=' * 30}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'EXPENSE CATEGORIES':^30}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 30}{Style.RESET_ALL}")
        
        for i, category in enumerate(sorted(self.categories), 1):
            print(f"{Fore.GREEN}{i}. {category}{Style.RESET_ALL}")
            
        print(f"{Fore.CYAN}{'=' * 30}{Style.RESET_ALL}")

    def analyze_expenses(self):
        """Analyze expenses by category and month"""
        if not self.expenses:
            print(f"{Fore.YELLOW}No expenses recorded yet for analysis.{Style.RESET_ALL}")
            return
            
        # Category analysis
        category_totals = {}
        for category, expenses in self.expenses.items():
            category_totals[category] = sum(expense["amount"] for expense in expenses)
            
        # Month analysis
        month_totals = {}
        for category, expenses in self.expenses.items():
            for expense in expenses:
                month = expense["date"][:7]  # YYYY-MM
                if month not in month_totals:
                    month_totals[month] = 0
                month_totals[month] += expense["amount"]
        
        # Display category analysis
        print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'EXPENSE ANALYSIS BY CATEGORY':^50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        
        total = sum(category_totals.values())
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100 if total > 0 else 0
            print(f"{Fore.GREEN}{category:<20} ${amount:<10.2f} ({percentage:.1f}%){Style.RESET_ALL}")
            
        # Display month analysis
        print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'EXPENSE ANALYSIS BY MONTH':^50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        
        for month, amount in sorted(month_totals.items()):
            print(f"{Fore.GREEN}{month:<10} ${amount:.2f}{Style.RESET_ALL}")
            
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

def display_header():
    """Display application header"""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'EXPENSE TRACKER':^60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'Author: ' + __author__:^60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'Version: ' + __version__:^60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

def display_menu():
    """Display main menu options"""
    print(f"\n{Fore.CYAN}EXPENSE TRACKER MENU:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1. Add Expense{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Add Category{Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. View All Expenses{Style.RESET_ALL}")
    print(f"{Fore.GREEN}4. View Expenses by Category{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5. View Expenses by Month{Style.RESET_ALL}")
    print(f"{Fore.GREEN}6. View Categories{Style.RESET_ALL}")
    print(f"{Fore.GREEN}7. Analyze Expenses{Style.RESET_ALL}")
    print(f"{Fore.GREEN}8. Exit{Style.RESET_ALL}")

def main():
    """Main application function"""
    tracker = ExpenseTracker()
    
    while True:
        display_header()
        display_menu()
        
        choice = input(f"\n{Fore.YELLOW}Enter your choice (1-8): {Style.RESET_ALL}")
        
        if choice == "1":
            date = input(f"{Fore.YELLOW}Enter date (YYYY-MM-DD): {Style.RESET_ALL}")
            try:
                amount = float(input(f"{Fore.YELLOW}Enter amount: ${Style.RESET_ALL}"))
                if amount <= 0:
                    print(f"{Fore.RED}Amount must be greater than zero.{Style.RESET_ALL}")
                    continue
            except ValueError:
                print(f"{Fore.RED}Invalid amount. Please enter a number.{Style.RESET_ALL}")
                continue
                
            category = input(f"{Fore.YELLOW}Enter category: {Style.RESET_ALL}")
            description = input(f"{Fore.YELLOW}Enter description (optional): {Style.RESET_ALL}")
            
            if tracker.add_expense(date, amount, category, description):
                print(f"{Fore.GREEN}Expense added successfully!{Style.RESET_ALL}")
                
        elif choice == "2":
            category = input(f"{Fore.YELLOW}Enter new category: {Style.RESET_ALL}")
            tracker.add_category(category)
            
        elif choice == "3":
            tracker.view_expenses()
            
        elif choice == "4":
            tracker.view_categories()
            category = input(f"{Fore.YELLOW}Enter category to view (or press Enter for all): {Style.RESET_ALL}")
            if category:
                tracker.view_expenses(filter_category=category)
            else:
                tracker.view_expenses()
                
        elif choice == "5":
            month = input(f"{Fore.YELLOW}Enter month (YYYY-MM): {Style.RESET_ALL}")
            tracker.view_expenses(filter_month=month)
            
        elif choice == "6":
            tracker.view_categories()
            
        elif choice == "7":
            tracker.analyze_expenses()
            
        elif choice == "8":
            print(f"{Fore.YELLOW}Exiting Expense Tracker. Goodbye!{Style.RESET_ALL}")
            break
            
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
