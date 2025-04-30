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
- Coded in Python, with the following libraries:
 - Flask
 - SQLAlchemy
 - Flask-SQLAlchemy
 - Flask-WTF
 - Email-Validator
 - Flask-Migrate
 - Flask-Mail
 - Flask-Login
 - Flask-Moment
 - Look into Poetry for package management??

# Random BS because I'm dumb as hell and can't remember shit
 - Setting the Flask app in a virtual environment:
    -> $env:FLASK_APP="app.py"

 - Clearing content from the flask database:
    -> flask db downgrade base
    -> flask db upgrade
