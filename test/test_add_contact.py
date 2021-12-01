import time
from model.new_user import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    con = (Contact(first_name="first_name"))
    app.contact.add_contact(con)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(con)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.add_contact(Contact())
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
