import jinja2
from aiohttp.web import Application as AiohttpApplication, \
    run_app as aiohttp_run_app, View as AiohttpView, Request as AoihttpRequest
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_jinja2 import setup as jinja2_setup


class Application(AiohttpApplication):
    from phone_book.app.contact.store.accessor import ContactAccessor

    database: dict = {}
    contact_accessor: ContactAccessor = None


class Request(AoihttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    from phone_book.app.web.routes import setup_routes
    from phone_book.app.web.accessors import setup_accessors

    setup_routes(app)
    setup_aiohttp_apispec(app, title="Rutabaga", url="/docs/json",
                          swagger_path="/docs")

    jinja2_setup(app, loader=jinja2.FileSystemLoader("templates"))
    setup_accessors(app)
    aiohttp_run_app(app)
