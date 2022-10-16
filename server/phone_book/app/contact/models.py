from dataclasses import dataclass
from mongoengine import Document, StringField


class Contact(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    mobile = StringField(required=True)
    home = StringField(required=True)
