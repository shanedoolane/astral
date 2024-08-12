import datetime
import astral
from astral.sun import sun
import matplotlib.pyplot as plt


start_date = datetime.date(2023,1,1)
end_date = datetime.date(2024,1,1)
latitude = 41.908
longitude = -87.655
observer = astral.sun.Observer(latitude, longitude)

def daylight_hours(current_date):
    sunrise = astral.sun.sunrise(observer, date=current_date)  # returns UTC
    sunset = astral.sun.sunset(observer, date=current_date) # returns UTC

    daylight_hours = (sunset - sunrise).total_seconds() / 3600
    return daylight_hours

## loop over every day from start_date to end_date
current_date = start_date
while current_date < end_date:
    # calculate daylight hours
    this_daylight_hours = daylight_hours(current_date)

    # print the hours
    print(f"Date: {current_date}, Daylight Hours: {this_daylight_hours}")

    # Increment current_date by one day
    current_date += datetime.timedelta(days=1)
