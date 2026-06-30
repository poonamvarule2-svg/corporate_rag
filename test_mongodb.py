from backend.database.mongodb import db

print()

print("Database Name")

print(db.name)

print()

print("Collections")

print(db.list_collection_names())