import datetime

class Yair_Lapid(object):
    days_since_birth = datetime.date.today() - datetime.date(1963, 11, 5)
    alive = days_since_birth.days
