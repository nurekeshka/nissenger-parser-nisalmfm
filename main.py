from rest_framework import status
from flask import Flask

from launcher import main
import responses
import settings
import requests
import senders


bot = senders.bot
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
        bot.send_to_admins(text='[FAIL] API is not accessible')
        return responses.APINotAccessible()
    except Exception as exception:
        bot.send_to_admins(
            text=f'[FAIL] Parsing failed because of the: {exception.__class__.__name__}')
        return responses.ReportError(exception)

    if response:
        if response.status_code == status.HTTP_201_CREATED:
            bot.send_to_admins(
                text='[OK] Timetable was successfully updated')
            return responses.SuccessfullyUpdated()
        else:
            bot.send_to_admins(
                text=f'[FAIL] API responded with status code: {response.status_code}')
            return responses.APIError()
    else:
        bot.send_to_admins(text='[OK] Timetable was not changed')
        return responses.TimetableDidNotChange()


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
