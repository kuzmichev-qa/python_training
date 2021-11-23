import time

from model.new_user import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact(Contact(first_name=""))
    app.contact.delete_first_contact()


def test_delete_all_contacts(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact(Contact(first_name=""))
    app.contact.delete_all_contacts()