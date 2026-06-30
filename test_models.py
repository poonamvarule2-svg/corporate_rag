from backend.database.models import Models

document = Models.create_document(

    filename="Employee_Handbook.pdf",

    total_pages=30,

    total_chunks=180

)

print(document)