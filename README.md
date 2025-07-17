# Sweet Shop Management System
The Sweet Shop Management System is a lightweight, Python-based web application built using Flask. It allows users to efficiently manage a sweet inventory and simulate basic point-of-sale operations without relying on external databases or JavaScript.

# Key Features Implemented
Add New Sweets (with ID, name, category, price, quantity)
Edit Sweet Details (update any field except ID)
Delete Sweets from inventory
Purchase Sweets (with quantity check & stock reduction)
Restock Sweets (update quantity)
Search by ID, Name, Category, or Max Price
Sort sweets by name, price, or quantity
Add to Cart feature to collect items before checkout
Checkout Page with:
    Item-wise subtotal
    Grand total
    Well-designed bill page
Fully integrated and styled HTML + CSS UI (no JavaScript used)

# Technical Stack
Backend: Python 3.x with Flask
Frontend: HTML5, CSS3 (No JavaScript used)
Data Storage: In-memory dictionary (dict) for sweets & session-based cart
Testing: unittest module for test-driven development

# Test Coverage (TDD)
Comprehensive unit tests using Python's unittest cover:
Adding a sweet
Deleting a sweet
Editing a sweet
Searching sweets
Sorting sweets
Valid & invalid purchase
Checkout + total bill calculation

# Project Structure 
Incubyte/
│
├── app.py              # Main Flask application
├── test_app.py         # All unit tests
├── templates/
│   ├── index.html      # Main dashboard
│   ├── edit.html       # Edit sweet page
│   ├── cart.html       # Cart summary page
│   └── bill.html       # Final checkout bill
├── static/
│   ├── style.css       # Main styling
│   └── cart.css        # Styling for cart 
|   └── bill.css        # Styling for bill
└── README.md           # Project documentation

# Notes
Admin/user roles are not implemented (not required in the spec).
All operations are stored in-memory (not using a database).
Focused on functionality + UI alignment.

## Run
1. Clone or Download the Project
    git clone "project" from here
    cd sweet-shop
2. Set Up Python Environment
    python --version
3. Run the Test Cases
     python test_app.py
4. Run the application , install flask 
    pip install flask
    python app.py
Then open a browser and go to:
http://127.0.0.1:5000
Then you will see the Sweet Shop UI

# Screenshots
<img width="940" height="588" alt="image" src="https://github.com/user-attachments/assets/c1912342-9df4-4002-a766-ac27a1469212" />
