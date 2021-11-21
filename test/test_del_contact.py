import time

from model.new_user import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.open_new_contact_page()
        app.contact.fill(Contact(first_name=""))
        app.contact.save_new_contact()
    app.contact.delete_first_contact()


def test_delete_all_contacts(app):
    if app.contact.contact_count() == 0:
        app.contact.open_new_contact_page()
        app.contact.fill(Contact(first_name=""))
        app.contact.save_new_contact()
    app.contact.delete_all_contacts()