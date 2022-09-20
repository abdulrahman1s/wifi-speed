import questionary as question
from urllib3 import disable_warnings
from os import environ
from .util import *
from .routers import find_router, RouterException


def main():
    disable_warnings()

    def credentials():
        try:
            return environ.get("ROUTER_USERNAME") or question.text("Username:").unsafe_ask(), environ.get("ROUTER_PASSWORD") or question.password("Password:").unsafe_ask()
        except KeyboardInterrupt:
            return credentials()

    username, password = credentials()

    # TODO: Add more routers
    router = find_router("hg630_v2")

    speed = question.select(
        "Enter the speed you want",
        choices=router.speeds,
        default=router.speeds[0]
    ).ask()

    try:
        router.login(username, password)
        router.set_speed(speed)
    except RouterException as err:
        print(err.message)
    except Exception as err:
        print("Unknown error has occurred")
        print(err)
