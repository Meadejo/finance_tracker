# Description
This is my first stab at making a more personally useful (and arguably modernized?) interpretation of Microsoft Money.
This is a work in progress, by a single person as a hobby project.

From concept, this project was started on 3/16/2025.

Project roadmap is roughly mapped with Issue Milestones.


# Concept
 - Track all financial transactions made for a single household.
 - Track individual accounts, as well as the institutions where those accounts are held.
 - Track non-cash assets. (Real estate, gold?, etc??)
 - Track Payees.
 - Maintain and track spending categories.
 - Tagging for simple filtering and reporting.
 - Basic reporting on all of the above.
 - Original basic DBDiagram here: [https://dbdiagram.io/d/Finances-6788aadf6b7fa355c30cd88a](https://dbdiagram.io/d/Finances-6788aadf6b7fa355c30cd88a)
   - Of Note: I started to stray from this concept before I even completed the diagram (and thus did not finish the diagram), but I've left it here for reference. At least for now.


# Tech
- Coded in Python (Barring the requisite HTML/Jinja), with the following libraries:
  - Flask
  - SQLAlchemy
  - Flask-SQLAlchemy
  - Flask-WTF
  - Email-Validator
  - Flask-Migrate
  - Flask-Mail
  - Flask-Login
  - Flask-Moment

# Licensing
Honestly... I've not thought about it yet. 
I'll make some decisions on this when I have a functioning Alpha build. (Milestone 08)
