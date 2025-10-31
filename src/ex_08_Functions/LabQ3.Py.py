def Validate_status_code(response_code):
    if response_code == 200:
        print("Request is Success")

    else:
        print("Error in request")


Validate_status_code(404)

Validate_status_code(200)
Validate_status_code(300)
Validate_status_code(response_code=200)