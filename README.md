# Your Task

This assignment is to use Django REST framework and a fresh Django server to create an API as a potential demo for a shoe store with the following models, broken out for standardization:

Manufacturer
name: str
website: url
ShoeType
style: str
ShoeColor
color_name: str (ROYGBIV + white / black) --> hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices (Links to an external site.)Links to an external site.
Shoe
size: int
brand name: str
manufacturer: FK (Foreign Key)
color: FK
material: str
shoe_type: FK
fasten_type: str
Use the documentation on creating a custom management command (Links to an external site.)Links to an external site. to add a `bootstrap_data` command for manage.py. This command should do the following things:

Populate the ShoeType table with the following entries:
sneaker
boot
sandal
dress
other
Populate the ShoeColor table with the following entries:
Red
Orange
Yellow
Green
Blue
Indigo
Violet
White
Black
The above can also be done with a built-in system called loaddata and fixtures, but we're going to kill two birds with one stone and do it the slightly longer way.

Don't worry about authentication, we just want it to be usable.
