"""
Namedtuple
In Python, namedtuple is a factory function in the collections
module that allows you to create simple classes
(similar to tuples) with named fields.
It's a convenient way to define classes for
storing data without the need to write a full class definition
"""


from collections import namedtuple

# Define a named tuple named 'Person' with fields 'name', 'age', and 'city'
Person = namedtuple('Person',
                    ['name', 'age', 'city'])

# Create instances of the named tuple
person1 = Person(name='Alice', age=25, city='New York')
person2 = Person(name='Bob', age=30, city='San Francisco')

# Accessing fields using dot notation
print("Person 1:", person1.name, person1.age, person1.city)
print("Person 2:", person2.name, person2.age, person2.city)
