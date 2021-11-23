from model.new_user import Contact


def test_modifify_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact(Contact(first_name=""))
    app.contact.modify_first_contact(Contact(first_name="name"))

