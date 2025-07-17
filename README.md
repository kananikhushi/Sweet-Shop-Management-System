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

# Notes
Not performed from admin/ user side . Just sake of performing operations it is done
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
<img width="940" height="266" alt="image" src="https://github.com/user-attachments/assets/8f4350e2-3f3a-48f8-9815-c115c8af125e" />
<img width="940" height="588" alt="image" src="https://github.com/user-attachments/assets/c1912342-9df4-4002-a766-ac27a1469212" />
<img width="940" height="588" alt="image" src="https://github.com/user-attachments/assets/95498d28-dfbc-4f6a-bca3-7e85e92f6030" />
<img width="940" height="874" alt="image" src="https://github.com/user-attachments/assets/e845de31-e646-44d9-a6e2-b1506524f828" />
Searching on basis of Sweet Name
<img width="940" height="581" alt="image" src="https://github.com/user-attachments/assets/251a2c44-5537-44f6-9e9e-3d6e0d422eb9" />
Sorted on basis of specific column
<img width="940" height="581" alt="image" src="https://github.com/user-attachments/assets/857e6c15-d395-4305-9d5a-643e4bd1d66b" />
Add to cart 
<img width="940" height="602" alt="image" src="https://github.com/user-attachments/assets/7c9b0ffe-4bc8-45ab-b786-798251f737c2" />
<img width="940" height="452" alt="image" src="https://github.com/user-attachments/assets/f5c3fde9-80ed-43b6-b8e8-66e17617943b" />
Adding Multiple Items in Cart
<img width="940" height="485" alt="image" src="https://github.com/user-attachments/assets/241f346f-3b92-48e0-8fde-250e41fffda8" />
<img width="940" height="785" alt="image" src="https://github.com/user-attachments/assets/468717ff-052b-4357-86a4-bc2fb8ba469a" />
Restocking items as per requirements
<img width="940" height="767" alt="image" src="https://github.com/user-attachments/assets/43da9bf1-2c82-45bb-93ba-a6163a71078d" />
Editing Items
<img width="940" height="985" alt="image" src="https://github.com/user-attachments/assets/58b0822d-63fd-4aa7-b84e-4c1a899efe5b" />
Deleting Items
<img width="940" height="589" alt="image" src="https://github.com/user-attachments/assets/cd76a6a5-8fdc-4eb3-a4c3-064e81b90bd2" />









