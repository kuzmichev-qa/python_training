import time

from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("title").send_keys(contact.tittle)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)

        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bday_month)
        wd.find_element_by_name("byear").send_keys(contact.bday_year)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.aday_month)
        wd.find_element_by_name("ayear").send_keys(contact.aday_year)

        wd.find_element_by_xpath("//div[@id='content']/form/label[22]/b").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@onclick= 'MassSelection()']").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title= 'Edit']").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("title").send_keys(contact.tittle)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)

        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bday_month)
        wd.find_element_by_name("byear").send_keys(contact.bday_year)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.aday_month)
        wd.find_element_by_name("ayear").send_keys(contact.aday_year)

        wd.find_element_by_xpath("//div[@id='content']/form/label[22]/b").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        wd.find_element_by_xpath("//input[@name='update' ]").click()