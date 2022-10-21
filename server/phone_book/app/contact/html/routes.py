import typing

from phone_book.app.contact.html.views import ContactListWebView

if typing.TYPE_CHECKING:
    from aiohttp.web_app import Application


def setup_routes(app: "Application"):
    app.router.add_view("/web/contact", ContactListWebView)
