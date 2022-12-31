import requests
from flask import Flask
from rest_framework import status

import responses
import senders
import settings
from launcher import main

bot = senders.bot
app = Flask(__name__)


@app.route("/timetable/update/", methods=["GET"])
def launch_parser():
    try:
        sender = senders.Online()
        sender.request()

        if sender.response.status_code != status.HTTP_200_OK:
            raise requests.exceptions.ConnectionError

        response = main()
    except requests.exceptions.ConnectionError:
        bot.send_to_admins(
            text=f"[FAIL] API is not accessible at {settings.SERVER_DOMAIN}"
        )
        return responses.APINotAccessible()
    except Exception as exception:
        bot.send_to_admins(
            text=f"[FAIL] Parsing failed at {settings.SERVER_DOMAIN} because of the: {exception.__class__.__name__}"
        )
        return responses.ReportError(exception)

    if response:
        if response.status_code == status.HTTP_201_CREATED:
            bot.send_to_admins(
                text=f"[OK] Timetable was successfully updated at {settings.SERVER_DOMAIN}"
            )
            return responses.SuccessfullyUpdated()
        else:
            bot.send_to_admins(
                text=f"[FAIL] API at {settings.SERVER_DOMAIN} responded with status code: {response.status_code}"
            )
            return responses.APIError()
    else:
        bot.send_to_admins(
            text=f"[OK] Timetable was not changed for {settings.SERVER_DOMAIN}"
        )
        return responses.TimetableDidNotChange()


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
