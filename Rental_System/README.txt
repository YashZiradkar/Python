# Bicycle Rental Management System

## Overview
The **Bicycle Rental Management System** is a comprehensive tool for managing bicycle rentals and inventory. 
It enables store managers to track bicycle availability, handle rentals and returns, manage inventory conditions, 
and generate purchase recommendations. This system relies on an SQLite database for inventory and transaction logging, 
while member verification is handled through an external module.

## Features
- **Inventory Management**: Store details for each bicycle, including brand, type, frame size, condition, 
							rental rates (daily and weekly), purchase date, and a unique ID.
- **Member Verification**: Verify active memberships and enforce rental limits using the `membershipManager.pyc` module.
- **Bicycle Search**: Search for available bicycles by brand, type, or frame size with real-time rental status updates.
- **Rental Process**: Ensure bicycle availability, check member rental limits, and log rental transactions.
- **Return Process**: Record returns, apply damage or late fees, and update bicycle condition and availability.
- **Inventory Recommendations**: Suggest purchase orders based on rental frequency, age, condition, and budget.

## Further Improvements
- A new table containing membership details can be created to update the rental limit upon renting and returning a bicycle
- Images can be added to the Menu screen

## Note
Database gets generate upon calling __initiate_db__() function of DataBaseManager in database.py, it can be done from menu.ipynb.
Therefore I haven't added db file in the folder.
