import time
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group_name_1", header="group_header_1", footer="group_footer_1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification(Group(name="group_name_edited", header="group_header_edited", footer="group_footer_edited"))
    app.session.logout()