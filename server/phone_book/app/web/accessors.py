import typing

from phone_book.app.contact.store.accessor import ContactAccessor

if typing.TYPE_CHECKING:
    from phone_book.app.web.app import Application


def setup_accessors(app: "Application"):
    app.contact_accessor = ContactAccessor()
    app.on_startup.append(app.contact_accessor.connect)
    app.on_cleanup.append(app.contact_accessor.disconnect)
