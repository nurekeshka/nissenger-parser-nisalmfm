from rest_framework import status
from flask import Flask

from launcher import main
import responses
import settings
import requests
import senders


app = Flask(__name__)


@app.route('/timetable/update/', methods=['GET'])
def launch_parser():
    try:
        sender = senders.Online()
        sender.request()

        if sender.response.status_code != status.HTTP_200_OK:
            raise requests.exceptions.ConnectionError

        response = main()
    except requests.exceptions.ConnectionError:
        return responses.APINotAccessible()
    except Exception as exception:
        return responses.ReportError(exception)

    if response:
        if response.status_code == status.HTTP_201_CREATED:
            return responses.SuccessfullyUpdated()
        else:
            return responses.APIError()
    else:
        return responses.TimetableDidNotChange()


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
