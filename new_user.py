class NewUserName:

    def __init__(self, first_name, middle_name, last_name, nickname):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname


class NewUserWork:

    def __init__(self, tittle, company, address):
        self.tittle = tittle
        self.company = company
        self.address = address


class NewUserTetelephone:

    def __init__(self, telephone_home, telephone_mobile, telephone_work, fax):
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.fax = fax


class NewUserEmail:

    def __init__(self, email_1, email_2, email_3):
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3


class NewUserHomepage:
    def __init__(self, homepage):
        self.homepage = homepage


class NewUserSecondary:
    def __init__(self, secondary_addres, secondary_home, secondary_notes):
        self.secondary_addres = secondary_addres
        self.secondary_home = secondary_home
        self.secondary_notes = secondary_notes


class NewUserBday:
    def __init__(self, bday_day, bday_month, bday_year):
        self.bday_day = bday_day
        self.bday_month = bday_month
        self.bday_year = bday_year


class NewUserAday:
    def __init__(self, aday_day, aday_month, aday_year):
        self.aday_day = aday_day
        self.aday_month = aday_month
        self.aday_year = aday_year
