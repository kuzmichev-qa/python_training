import time

from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.first_name)
        self.change_contact_field_value("middlename", contact.middle_name)
        self.change_contact_field_value("lastname", contact.last_name)
        self.change_contact_field_value("nickname", contact.nick_name)

        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)

        self.change_contact_field_value("home", contact.telephone_home)
        self.change_contact_field_value("mobile", contact.telephone_mobile)
        self.change_contact_field_value("work", contact.telephone_work)
        self.change_contact_field_value("fax", contact.fax)

        self.change_contact_field_value("email", contact.email_1)
        self.change_contact_field_value("email2", contact.email_2)
        self.change_contact_field_value("email3", contact.email_3)

        self.change_contact_field_value("homepage", contact.homepage)

        self.change_contact_field_value_dates("bday", contact.bday_day)
        self.change_contact_field_value_dates("bmonth", contact.bday_month)
        self.change_contact_field_value("byear", contact.bday_year)
        self.change_contact_field_value_dates("aday", contact.aday_day)
        self.change_contact_field_value_dates("amonth", contact.aday_month)
        self.change_contact_field_value("ayear", contact.aday_year)

        self.change_contact_field_value("address2", contact.secondary_address)
        self.change_contact_field_value("phone2", contact.secondary_home)
        self.change_contact_field_value("notes", contact.secondary_notes)

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).send_keys(text)

    def change_contact_field_value_dates(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@onclick= 'MassSelection()']").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()

    def edit(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//*[@title= 'Edit']").click()

    def modify_first_contact(self, new_conatact_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//*[@title= 'Edit']").click()
        self.fill(new_conatact_data)
        wd.find_element_by_xpath("//input[@name='update']").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def contact_count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//*[@title= 'Edit']"))

    def save_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
