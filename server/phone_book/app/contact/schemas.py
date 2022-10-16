from marshmallow import Schema, fields


class NewContactSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    mobile = fields.Str(required=True)
    home = fields.Str(required=True)


class ContactIdSchema(Schema):
    id = fields.Str(required=True)


class ExistedContactSchema(ContactIdSchema, NewContactSchema):
    pass


class ContactListSchema(Schema):
    contacts = fields.Nested(ExistedContactSchema, many=True)

