import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from new_user import NewUserName, NewUserWork, NewUserTetelephone, NewUserEmail, NewUserHomepage, NewUserSecondary, \
    NewUserBday, NewUserAday


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_user_creation(wd)
        self.fill_user_name(wd, NewUserName(first_name="first_name", middle_name="middle_name",
                                            last_name="last_name", nickname="nickname"))
        self.fill_user_work(wd, NewUserWork(tittle="tittle", company="company", address="address"))
        self.fill_user_telephone(wd, NewUserTetelephone(telephone_home="telephone_home",
                                                        telephone_mobile="telephone_mobile",
                                                        telephone_work="telephone_work", fax="fax"))
        self.fill_user_email(wd, NewUserEmail(email_1="mail_1", email_2="mail_2", email_3="mail_3"))
        self.fill_user_homepage(wd, NewUserHomepage(homepage="homepage"))
        self.fill_user_bday(wd, NewUserBday(bday_day="15", bday_month="June", bday_year="2000"))
        self.fill_user_aday(wd, NewUserAday(aday_day="15", aday_month="June", aday_year="2000"))
        self.fill_user_secondary(wd, NewUserSecondary(secondary_addres="secondary_addres",
                                                      secondary_home="secondary_home",
                                                      secondary_notes="secondary_notes"))
        self.submit_user_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_user_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def fill_user_secondary(self, wd, NewUserSecondary):
        wd.find_element_by_xpath("//div[@id='content']/form/label[22]/b").click()
        wd.find_element_by_xpath("//div[@id='content']/form/label[22]/b").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(NewUserSecondary.secondary_addres)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(NewUserSecondary.secondary_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(NewUserSecondary.secondary_notes)

    def fill_user_aday(self, wd, NewUserAday):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(NewUserAday.aday_day)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[20]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(NewUserAday.aday_month)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(NewUserAday.aday_year)

    def fill_user_bday(self, wd, NewUserBday):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(NewUserBday.bday_day)
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(NewUserBday.bday_month)
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(NewUserBday.bday_year)

    def fill_user_homepage(self, wd, NewUserHomepage):
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(NewUserHomepage.homepage)

    def fill_user_email(self, wd, NewUserEmail):
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(NewUserEmail.email_1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(NewUserEmail.email_2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(NewUserEmail.email_3)

    def fill_user_telephone(self, wd, NewUserTetelephone):
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(NewUserTetelephone.telephone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(NewUserTetelephone.telephone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(NewUserTetelephone.telephone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(NewUserTetelephone.fax)

    def fill_user_work(self, wd, NewUserWork):
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(NewUserWork.tittle)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(NewUserWork.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(NewUserWork.address)

    def fill_user_name(self, wd, NewUserName):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(NewUserName.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(NewUserName.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(NewUserName.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(NewUserName.nickname)

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
