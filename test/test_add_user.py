import time
from model.new_user import Contact


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill(Contact(first_name="first_name", middle_name="middle_name",
                             last_name="last_name", nickname="nickname",
                             tittle="tittle", company="company", address="address",
                             telephone_home="telephone_home",
                             telephone_mobile="telephone_mobile",
                             telephone_work="telephone_work", fax="fax",
                             email_1="mail_1", email_2="mail_2", email_3="mail_3",
                             homepage="homepage",
                             secondary_address="secondary_address",
                             secondary_home="secondary_home",
                             secondary_notes="secondary_notes",
                             bday_day="15", bday_month="June", bday_year="2000",
                             aday_day="15", aday_month="June", aday_year="2000"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill(Contact(first_name="", middle_name="",
                             last_name="", nickname="",
                             tittle="", company="", address="",
                             telephone_home="",
                             telephone_mobile="",
                             telephone_work="", fax="",
                             email_1="", email_2="", email_3="",
                             homepage="",
                             secondary_address="",
                             secondary_home="",
                             secondary_notes="",
                             bday_day="-", bday_month="-", bday_year="",
                             aday_day="-", aday_month="-", aday_year=""))
    app.session.logout()