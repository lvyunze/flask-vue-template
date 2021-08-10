from apps.models import db
from peewee import CharField, Model


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    username = CharField()
    password = CharField()
