from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')

db = client['actividad']
collection = db['notas']

current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
notas = [
{"nombre": "Pedro López", "edad": 25, "email": "pedro@eip.com", "nota": 5.2, "fecha": current_date},
{"nombre": "Julia García", "edad": 22, "email": "julia@eip.com", "nota": 7.3, "fecha": current_date},
{"nombre": "Amparo Mayoral", "edad": 28, "email": "amparo@eip.com", "nota": 8.4, "fecha": current_date},
{"nombre": "Juan Martínez", "edad": 30, "email": "juan@eip.com", "nota": 6.8, "fecha": current_date}
]
result = collection.insert_many(notas)
print(f"Inserted {len(result.inserted_ids)} documents")

collection.update_one({"nombre": "Amparo Mayoral"}, {"$set": {"nota": 9.3}})
collection.update_one({"nombre": "Juan Martínez"}, {"$set": {"nota": 7.2}})

print("Colecion notas")
notas = collection.find()
for nota in notas:
    print(nota)

print("todas las notas entre 7 y 7.5")
notas = collection.find({"nota": {"$gt": 7, "$lt": 7.5}})
for nota in notas:
    print(nota)

result = collection.delete_one({"nombre": "Pedro López"})
print(f"Deleted {result.deleted_count} document")

client.close()