import time


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_user()
    app.session.logout()
