PharmaPulse: Pharmaceutical Inventory Management System - Detailed Report

 Introduction :-
The PharmaPulse project is a Python-based application designed to manage pharmaceutical inventory efficiently. It uses SQLite3 for database management and 
provides a user-friendly interface for performing essential operations such as inserting, updating, searching, viewing, and billing medicines. The system ensures
accurate stock management, low-stock alerts, and profit calculations, making it a valuable tool for pharmacies to streamline their operations.



Key Features and Functionality :-

1. Database and Table Creation
   - The system uses SQLite3 to create a database named `PharmaPulse` and a table with the same name.
   - The table stores details such as Medicine ID (MedID), Medicine Name (MedName), Purchase Cost (PCost), Selling Cost (SCost), Availability 
    (stock quantity) , Expiry Date (ExpiryDate), and Profit of each Medicine (Profit).

2. Insert Operation
   - Users can add new medicines to the inventory by providing details like MedID, MedName, PCost, SCost, Availability, and ExpiryDate.
   - The system checks for duplicate `MedID` and ensures no two medicines have the same ID.
   - If the stock level is below 10, a low-stock alert is displayed.

3. Update Operation
   - Users can update:
     - Cost: Modify the selling cost of a medicine.
     - Availability: Add more stock to existing medicines.
     - Delete: Remove a medicine from the inventory.
   - Low-stock alerts are triggered if the updated stock falls below 10.

4. Search Operation
   - Users can search for medicines using:
     - Medicine ID: Fetch details of a specific medicine by its ID.
     - First Letter of Medicine Name: Retrieve all medicines starting with a specific letter.
     - Cost Range: Find medicines within a specified price range.

5. View Operation
   - Displays the entire inventory in a tabular format, showing all details of each medicine, including MedID, MedName, PCost, SCost, Availability,
    ExpiryDate, and Profit.

6. Bill Generation
   - Users can generate bills for purchased medicines.
   - The system calculates the total cost, updates the stock levels, and accumulates the profit for each transaction.
   - It checks for sufficient stock before processing the purchase and provides a detailed bill summary.


Technical Implementation :-

1. Database Connectivity
   - The sqlite3 module is used to connect to the database and perform CRUD (Create, Read, Update, Delete) operations.
   - A cursor object (`cur`) is created to execute SQL queries.

2. User Interaction
   - The program provides a menu-driven interface for users to select operations (Insert, Update, Search, View, Bill).
   - Input validation is implemented to ensure data integrity (e.g., negative stock values are rejected).

3. Error Handling
   - The system checks for duplicate IDs, insufficient stock, and invalid inputs to prevent errors.
   - Appropriate messages are displayed to guide the user.

4. Profit Calculation
   - Profit is calculated as the difference between the selling cost (SCost) and purchase cost (PCost) for each transaction.
   - The total profit is updated in the database for each medicine.



Outcome and Benefits :-

1. Efficient Inventory Management
   - The system automates stock management, reducing manual errors and ensuring accurate records.

2. Low-Stock Alerts
   - Timely alerts for low stock levels help pharmacies avoid stockouts and maintain adequate inventory.

3. Profit Tracking
   - The system calculates and tracks profits for each medicine, providing insights into business performance.

4. User-Friendly Interface
   - The menu-driven interface makes it easy for users to perform operations without technical expertise.

5. Scalability
   - The system can handle a large number of medicines and transactions, making it suitable for small to medium-sized pharmacies.

Conclusion :-
The PharmaPulse project is a robust and efficient solution for managing pharmaceutical inventory. It simplifies operations, ensures accurate stock management, 
and provides valuable insights into business performance. With further enhancements, it can become an indispensable tool for pharmacies to optimize their 
operations and improve customer satisfaction.
