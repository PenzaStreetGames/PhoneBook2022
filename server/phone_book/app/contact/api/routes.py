import typing

from phone_book.app.contact.api.views import ContactListView, ContactView

if typing.TYPE_CHECKING:
    from aiohttp.web_app import Application


def setup_routes(app: "Application"):
    app.router.add_view("/v1/contact", ContactListView)
    app.router.add_view("/v1/contact/{uid}", ContactView)

