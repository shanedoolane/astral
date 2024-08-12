from datetime import datetime
import astral
from astral.sun import sun

observer = astral.Observer(latitude=-24.6272, longitude=-70.4039, elevation=2200)
timestamp =  datetime(2023, 9, 23)
helios = sun(observer, timestamp, dawn_dusk_depression=18)
dusk = helios['dusk']
dawn = helios['dawn']
print ("dawn", dawn, "dusk", dusk)
