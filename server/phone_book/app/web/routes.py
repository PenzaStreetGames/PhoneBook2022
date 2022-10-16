import typing

if typing.TYPE_CHECKING:
    from aiohttp.web_app import Application
from phone_book.app.contact.routes import setup_routes as setup_contact_routes


def setup_routes(app: "Application"):
    setup_contact_routes(app)
