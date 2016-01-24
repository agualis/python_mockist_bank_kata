import arrow


class Clock():
    def date_as_string(self):
        return self.today().format('DD-MM-YYYY')

    def today(self):
        utc = arrow.utcnow()
        return utc.to('Europe/Madrid')

