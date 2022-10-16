from phone_book.app.web.app import View
import aiohttp_jinja2


class ContactListWebView(View):
    @aiohttp_jinja2.template("index.html")
    async def get(self):
        return {}


class ContactWebView(View):
    pass
