# def kUserVerificationFailed():
#     return kErrorResponse(
#         message="User verification failed"
#     )


# def kDatabaseErrorResponse():
#     return kErrorResponse(
#         message="Something went wrong"
#     )


def kSuccessResponse( data):
    return {
        "status": True,
        "message": "Data found",
        "data": data
    }


def kErrorResponse(message):
    return {
        "status": False,
        "message": message,
        "data": []
    }
