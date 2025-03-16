# finance_tracker
This is my first stab at making a more personalized interpretation of Microsoft Money.


# Usage Concepts
- Track all financial transactions made for a single household.
- Track individual accounts, as well as the institutions where those accounts are held.
- Track non-cash assets. (Real estate, gold, etc.)
- Track Payees and Payors.
- Maintain and track spending categories.
- Basic reporting on all of the above.
- Basic DBDiagram available here: [https://dbdiagram.io/d/Finances-6788aadf6b7fa355c30cd88a](https://dbdiagram.io/d/Finances-6788aadf6b7fa355c30cd88a)


# Tech Concepts
- Coded in Python.
  - Pandas to perform any complex calcs that cannot/should not be done in the DB itself.
- Use PostgreSQL for the actual data storage.
  - Start with a local DB. Look into hosting later. (Even w/ hosting, it'll likely only be on a local network.)
- Use Flask to connect and build a simple front end.
- Look into Poetry for package management??
- 
