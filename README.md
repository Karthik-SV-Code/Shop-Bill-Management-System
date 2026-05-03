# Shop Bill Management System (Python + MySQL)

A console-based billing system developed in Python that allows users to generate and manage bills for different product categories such as Stationary, Clothing, Electronics, and Grocery. The system stores transaction data in a MySQL database and calculates final prices with GST and discounts.

---

## Features

- Category-based billing:
  - Stationary
  - Clothing
  - Electrical Appliances
  - Grocery
- Automatic calculation of:
  - Total price
  - GST (varies by category)
  - Discounts (based on total amount)
- MySQL database integration for storing items
- Displays complete bill summary
- Continuous execution loop for multiple bills

---

## Tech Stack

- Language: Python
- Database: MySQL
- Library Used: mysql-connector-python

---

## Installation & Setup

### 1. Install Dependencies

```bash
pip install mysql-connector-python
```

---

### 2. Setup MySQL Database

Login to MySQL and create the database:

```sql
CREATE DATABASE Store;
USE Store;
```

Create required tables:

```sql
CREATE TABLE STATIONARY (
    bill_no INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    price FLOAT,
    quantity INT
);

CREATE TABLE CLOTHING (
    bill_no INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    price FLOAT,
    quantity INT
);

CREATE TABLE ELECTRONICS (
    bill_no INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    price FLOAT,
    quantity INT
);

CREATE TABLE GROCERY (
    bill_no INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    price FLOAT,
    quantity INT
);
```

---

### 3. Update Database Credentials

In your Python file, modify:

```python
mysql.connect(user='root', password='mysql', host='localhost', database='Store')
```

Replace with your MySQL credentials.

---

### 4. Run the Program

```bash
python your_script_name.py
```

---

## How It Works

1. User selects a category:
   - S → Stationary
   - C → Clothing
   - E → Electronics
   - G → Grocery

2. User enters:
   - Customer details
   - Number of items
   - Item name, price, quantity

3. System:
   - Calculates total
   - Applies GST
   - Applies discount (based on slab)
   - Stores data in MySQL
   - Displays full bill

---

## Tax & Discount Logic

### GST Rates

| Category     | GST |
|--------------|-----|
| Stationary   | 18% |
| Clothing     | 12% |
| Electronics  | 18% |
| Grocery      | 12% |

---

### Discount Slabs (Example: Stationary)

| Total Amount | Discount |
|--------------|----------|
| < 100        | 0%       |
| 100–800      | 5%       |
| 800–5000     | 15%      |
| 5000–14000   | 20%      |
| > 14000      | 25%      |

(Other categories have similar slab logic with different thresholds.)

---

## Sample Output (Console)

```
----STATIONARY BILL----
Invoice date: 01-05-2026
Customer Name: Rahul
Item: Pen
Price: 10
Quantity: 5

Total Amount: 50
Final price inclusive of taxes: 59.0
```

---

## Limitations

- No GUI (console-based only)
- No input validation (may crash on wrong inputs)
- SQL queries not parameterized (risk of SQL injection)
- Repetitive code (can be optimized using functions)

---

## Possible Improvements

- Add GUI using Tkinter / PyQt
- Use parameterized queries (%s) for security
- Modularize code using functions/classes
- Add invoice export (PDF)
- Add user authentication
- Add product inventory system

---

## Author

Karthik 
CSE Student 

