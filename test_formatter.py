from backend.rag.response_formatter import ResponseFormatter

formatter = ResponseFormatter()

response = formatter.success(

    question="How many leaves?",

    answer="Employees receive 20 annual leaves.",

    citations=[

        {

            "section":"Leave Policy",

            "page":3

        }

    ]

)

print(response)