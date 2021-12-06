from django.forms import (
    Form,
    CharField,
    EmailField,
    FileField,
)


class CreateUserForm(Form):
    username = CharField()
    e_mail = EmailField()


class UserNameForm(Form):
    username = CharField()


class UserCsvForm(Form):
    csv = FileField()
