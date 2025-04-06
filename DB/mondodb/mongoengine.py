from mongoengine import (
    connect,
    Document,
    StringField,
    ReferenceField,
    DateTimeField,
    LongField,
    SequenceField,
)

from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("MONGO_URI")

connect(
    db="echo-bot",
    host=URI,
)


class User(Document):
    id = LongField(primary_key=True)
    username = StringField(max_length=34)
    email = StringField(max_length=50)
    phone = StringField(max_length=20)
    created_at = DateTimeField(default=datetime.utcnow)


class MessageText(Document):
    id = SequenceField(primary_key=True)
    user_id = ReferenceField(User, required=True, reverse_delete_rule=2)
    message_text = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
