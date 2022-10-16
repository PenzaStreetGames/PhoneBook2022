import typing
from typing import Optional

from bson import ObjectId
from pymongo import MongoClient
from mongoengine import connect

from phone_book.app.contact.models import Contact
if typing.TYPE_CHECKING:
    from phone_book.app.web.app import Application


class ContactAccessor:
    def __init__(self):
        self.app: Optional[Application] = None
        self.client: Optional[MongoClient] = None
        self.db = None

    async def connect(self, app: "Application"):
        self.client = connect(db="contacts", host="localhost", port=27017)
        self.db = self.client["contacts"]
        print("connect to database")

    async def disconnect(self, app: "Application"):
        self.client.close()
        print("disconnect from database")

    async def create_contact(self, contact: Contact) -> Contact:
        contact = contact.save()
        return contact

    async def get_contact_list(self) -> list[Contact]:
        return Contact.objects

    async def get_contact_by_uid(self, uid) -> Optional[Contact]:
        try:
            contact = Contact.objects.get(id=uid)
        except Contact.DoesNotExist:
            contact = None
        return contact

    async def edit_contact(self, contact: Contact) -> Optional[Contact]:
        try:
            old_contact = Contact.objects.get(id=contact.id)
        except Contact.DoesNotExist:
            old_contact = None
        if old_contact is not None:
            contact = contact.save()
            return contact
        else:
            return None

    async def delete_contact_by_uid(self, uid: int) -> Optional[Contact]:
        try:
            contact = Contact.objects.get(id=uid)
        except Contact.DoesNotExist:
            contact = None
        if contact is not None:
            contact.delete()
            return contact
        else:
            return None

    async def delete_all_contacts(self):
        Contact.drop_collection()
