import datetime
class Date:
    def __init__(self, date, month, year):
        assert date>0 and date<32, f"date must be between 1 to 31"
        assert month>0 and month<13, f"month must be between 1 and 12"
        assert year>0, f"year must be positive"
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.date:02d}/{self.month:02d}/{self.year}"
    
    def compare(self, o):
        if self.date == o.date and self.month == o.month and self.year == o.year:
            print(self, " is equal to ", o)
        if self.date > o.date and self.month > o.month and self.year > o.year:
            print(self, " is later to ", o)
        else:
            print(self, " is earlier to ", o)

    def AddDays(self, add):
        current = datetime.datetime(self.year, self.month, self.date)
        new = current + datetime.timedelta(add)

        self.date = new.day
        self.month = new.month
        self.year = new.year


date = Date(20,1,2001)
date2 = Date(31,12,2012)

print(date)
print(date2)

date.compare(date2)

date.AddDays(10)
print(date)