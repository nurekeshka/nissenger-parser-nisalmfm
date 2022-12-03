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
