import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from new_user import NewUserPage


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_user_creation(wd)
        self.fill_new_user_page(wd, NewUserPage(first_name="first_name", middle_name="middle_name",
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
                                                aday_day="15", aday_month="June", aday_year="2000", ))
        self.submit_user_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_user_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_new_user_page(self, wd, NewUserPage):
        wd.find_element_by_name("firstname").send_keys(NewUserPage.first_name)
        wd.find_element_by_name("middlename").send_keys(NewUserPage.middle_name)
        wd.find_element_by_name("lastname").send_keys(NewUserPage.last_name)
        wd.find_element_by_name("nickname").send_keys(NewUserPage.nickname)

        wd.find_element_by_name("title").send_keys(NewUserPage.tittle)
        wd.find_element_by_name("company").send_keys(NewUserPage.company)
        wd.find_element_by_name("address").send_keys(NewUserPage.address)

        wd.find_element_by_name("home").send_keys(NewUserPage.telephone_home)
        wd.find_element_by_name("mobile").send_keys(NewUserPage.telephone_mobile)
        wd.find_element_by_name("work").send_keys(NewUserPage.telephone_work)
        wd.find_element_by_name("fax").send_keys(NewUserPage.fax)

        wd.find_element_by_name("email").send_keys(NewUserPage.email_1)
        wd.find_element_by_name("email2").send_keys(NewUserPage.email_2)
        wd.find_element_by_name("email3").send_keys(NewUserPage.email_3)

        wd.find_element_by_name("homepage").send_keys(NewUserPage.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(NewUserPage.bday_day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(NewUserPage.bday_month)
        wd.find_element_by_name("byear").send_keys(NewUserPage.bday_year)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(NewUserPage.aday_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(NewUserPage.aday_month)
        wd.find_element_by_name("ayear").send_keys(NewUserPage.aday_year)

        wd.find_element_by_xpath("//div[@id='content']/form/label[22]/b").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(NewUserPage.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(NewUserPage.secondary_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(NewUserPage.secondary_notes)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def init_user_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
