from rest_framework import status
from flask import Response
from flask import jsonify
import requests


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


class ReportError(MessageJsonResponse):
    def __init__(self, exception: Exception):
        super(ReportError, self).__init__(
            text=f'Error occurred while parsing: {exception.__class__.__name__}',
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class SuccessfullyUpdated(MessageJsonResponse):
    def __init__(self):
        super(SuccessfullyUpdated, self).__init__(
            text='Successfully updated timetable. Timetable waiting for being uploaded!',
        )


class APIError(MessageJsonResponse):
    def __init__(self, response: requests.Response):
        super(SuccessfullyUpdated, self).__init__(
            text=f'Something went wrong... This an output from the server: {response.json()}',
            status=status.HTTP_400_BAD_REQUEST,
        )
