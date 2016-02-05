import datetime as dt

class YairLapid(object):
    _BIRTH_DATE = dt.date(1963, 11, 5)

    def __init__(self):
        super(YairLapid, self).__init__()

    @property
    def birthdate(self):
        return str(self._BIRTH_DATE)

    @property
    def days_since_birth(self):
        return (dt.date.today() - self._BIRTH_DATE).days

    def _get_current_year(self):
        return dt.date.today().year

    def _get_next_birthday(self):
        current_year = self._get_current_year()
        current_birthday = dt.date(current_year, self._BIRTH_DATE.month, self._BIRTH_DATE.day)
        if current_birthday > dt.date.today():
            return current_birthday
        else:
            return dt.date(current_year + 1, self._BIRTH_DATE.month, self._BIRTH_DATE.day)

    @property
    def next_birthday(self):
        return str(self._get_next_birthday())


    def is_birthday_passed(self):
        current_year = self._get_current_year()
        return self._get_next_birthday().year > current_year

    def __repr__(self):
        return 'Yair Lapid, born in {0}'.format(self.birthdate)