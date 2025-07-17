# Sweet Shop Management System
The Sweet Shop Management System is a lightweight, Python-based web application built using Flask. It allows users to efficiently manage a sweet inventory and simulate basic point-of-sale operations without relying on external databases or JavaScript.

# Key Features Implemented
1. Add New Sweets (with ID, name, category, price, quantity)
2. Edit Sweet Details (update any field except ID)
3. Delete Sweets from inventory
4. Purchase Sweets (with quantity check & stock reduction)
5. Restock Sweets (update quantity)
6. Search by ID, Name, Category, or Max Price
7. Sort sweets by name, price, or quantity
8. Add to Cart feature to collect items before checkout
9. Checkout Page with:
    Item-wise subtotal
    Grand total
    Well-designed bill page
10. Fully integrated and styled HTML + CSS UI (no JavaScript used)

# Technical Stack
1. Backend: Python with Flask
2. Frontend: HTML, CSS (No JavaScript used)
3. Data Storage: In-memory dictionary (dict) for sweets & session-based cart
4. Testing: unittest module for test-driven development

# Test Coverage (TDD)
 Comprehensive unit tests using Python's unittest cover:
1. Adding a sweet
2. Deleting a sweet
3. Editing a sweet
4. Searching sweets
5. Sorting sweets
6. Valid & invalid purchase
7. Checkout + total bill calculation

# Notes
1. Not performed from admin/ user point of view. Just as asked for assessment part it was performed
2. All operations are stored in-memory (not using a database).
3. Focused on functionality + UI alignment.
4. I came up with the idea as mentioned in the Assessment pdf and looked for the solution and tried it implementing
5. I took help from AI tools to guide me while building the project. It helped me with:
    Writing and improving the code
    Making the design and layout look better
    Creating test cases to check if everything works
"In this project, I have written all the routes and method logic directly inside app.py for simplicity and to keep everything in one place. However, in larger or more complex projects, it is a good practice to separate route definitions, logic, and configurations into different files or modules to improve readability, maintainability, and scalability."
# Run
## 1. Clone or Download the Project
Clone the repository and navigate into the folder:
```bash
git clone "project" from here
cd your-project-folder
```
## 2. Set Up Python Environment
```bash
python --version
```
## 3. Run the Test Cases
```bash
 python test_app.py
```
## 4. Install Flask & Run the application 
```bash
pip install flask
python app.py
```
Then open a browser and go to:
http://127.0.0.1:5000
Then you will see the Sweet Shop UI

# Screenshots
<img width="940" height="266" alt="image" src="https://github.com/user-attachments/assets/8f4350e2-3f3a-48f8-9815-c115c8af125e" />
<img width="940" height="588" alt="image" src="https://github.com/user-attachments/assets/c1912342-9df4-4002-a766-ac27a1469212" />
<img width="940" height="588" alt="image" src="https://github.com/user-attachments/assets/95498d28-dfbc-4f6a-bca3-7e85e92f6030" />
<img width="940" height="874" alt="image" src="https://github.com/user-attachments/assets/e845de31-e646-44d9-a6e2-b1506524f828" />
<img width="940" height="581" alt="image" src="https://github.com/user-attachments/assets/251a2c44-5537-44f6-9e9e-3d6e0d422eb9" /> 
<img width="940" height="602" alt="image" src="https://github.com/user-attachments/assets/7c9b0ffe-4bc8-45ab-b786-798251f737c2" />
<img width="940" height="452" alt="image" src="https://github.com/user-attachments/assets/f5c3fde9-80ed-43b6-b8e8-66e17617943b" />
<img width="940" height="485" alt="image" src="https://github.com/user-attachments/assets/241f346f-3b92-48e0-8fde-250e41fffda8" />
<img width="940" height="785" alt="image" src="https://github.com/user-attachments/assets/468717ff-052b-4357-86a4-bc2fb8ba469a" />
<img width="940" height="767" alt="image" src="https://github.com/user-attachments/assets/43da9bf1-2c82-45bb-93ba-a6163a71078d" />
<img width="940" height="985" alt="image" src="https://github.com/user-attachments/assets/58b0822d-63fd-4aa7-b84e-4c1a899efe5b" />
<img width="940" height="589" alt="image" src="https://github.com/user-attachments/assets/cd76a6a5-8fdc-4eb3-a4c3-064e81b90bd2" />









