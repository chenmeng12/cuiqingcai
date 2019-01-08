import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

student1 = {
    'id':20170101,
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2 = {
    'id':20170102,
    'name':'BOb',
    'age':21,
    'gender':'female'
}
db = client.test
collection = db.students

# result = collection.insert_many([student1,student2])
# print(result.inserted_ids)

result = collection.find_one({'name':'BOb'})
print(result)