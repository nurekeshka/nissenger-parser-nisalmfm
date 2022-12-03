from rest_framework import status
from flask import Response
from flask import jsonify


class JsonResponse(Response):
    def __init__(self, data: dict = None, status: int = 200):
        super(JsonResponse, self).__init__(
            response=jsonify(**data).data,
            status=status,
            content_type='json',
        )


class MessageJsonResponse(JsonResponse):
    def __init__(self, text: str, status: int = 200):
        super(MessageJsonResponse, self).__init__(
            data={'message': text},
            status=status,
        )


class APINotAccessible(MessageJsonResponse):
    def __init__(self):
        super(APINotAccessible, self).__init__(
            text='The main API is not accessible or offline.',
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
