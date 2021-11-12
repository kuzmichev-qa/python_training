from selenium.webdriver.support.select import Select


class NewUserHelper:
    def __init__(self, app):
        self.app = app

    def submit_user_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_new_user_page(self, NewUserPage):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
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

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    # def init_user_creation(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("add new").click()