import time

from model.new_user import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact(Contact(first_name=""))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert old_contact == new_contact


def test_delete_all_contacts(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact(Contact(first_name=""))
    app.contact.delete_all_contacts()
    new_contact = app.contact.get_contact_list()
    assert len(new_contact) == 0