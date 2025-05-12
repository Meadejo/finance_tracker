This file exists only as a personal reference and has no direct value to this codebase.
That said, it is tangentially useful if anyone else wants to do anything with it and has some of the same questions that I do/did, so if that's you: Here you go.


#  Random stuff I forget because it so rarely comes up
##  - Setting the Flask app in a virtual environment:
    -> $env:FLASK_APP="app_name.py"

##  - Clearing all content from the flask database with Flask-Migrate:
    -> flask db downgrade base
    -> flask db upgrade



# Common ORM Queries
Full documentation here: https://docs.sqlalchemy.org/en/20/core/expression_api.html

## Queries
sa.select([Class])
 - This creates the basis of the query, which determines what table will be queried.

sa.select([Class]).where([criteria])
 - Filters objects of the noted class by the provided criteria
    sa.select(User).where(User.username.like('s%')) would query for all users with a username that starts with the letter 's'.
    sa.select(Vehicle).where(Vehicle.registration = 'HOTBODY') would query for all vehicles with the registration of 'HOTBODY'.

sa.select([Class]).order_by([Object.Attribute])
 - This does what you think it does.
 - You can provide multiple criteria, and it will order them in the priority provided.


### Returns
db.session.scalar(query)
 - Returns a single result based on the query, or None if there is no result.
 - db.session.scalars(query).first() could also be used to guarantee a return of only a single result, but bear in mind this could lead to the mistaken belief that there is only a single valid return.

db.first_or_404(query)
 - A special query provided by Flask-SQLAlchemy that functions as db.session.scalar(query), but returns a 404 error to the client if no results are found.

db.session.scalars(query)
 - This returns a group of results as an iterator. So you can use something like:
    users = db.session.scalars(query)
    for u in users:
        [do whatever]

db.session.scalars(query).all()
 - This returns a results list, which can be manipulated or index referenced.

db.session.get([Class], [primary_key])
 - This retrieves an item directly, by primary key. (Usually .id)
    u = db.session.get(User, 13)
    [u] would be the user in the table with User.id of 13.

## Adds and Commits
db.session.add([object])
 - This stages a change to be made to the database, but does not make the change.

db.session.commit()
 - This commits all staged changes to the database.
