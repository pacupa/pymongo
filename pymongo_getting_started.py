
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

#Reference to test database
db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print(item['nombre'])

#ejemplo. add

