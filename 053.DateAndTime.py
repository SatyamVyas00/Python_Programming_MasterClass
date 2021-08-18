# import datetime
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

import pytz
import datetime
# country = "Asia/Kolkata"
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("Print the Time in {} is {}".format(country,local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))
#
# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ":" + pytz.country_names[x])
#
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))
#
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x,pytz.country_names[x]),end=':')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone,pytz.country_timezones[x]))
#     else:
#         print("\t\tNo TimeZone Defined")

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC time {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {},time zone {}".format(aware_local_time,aware_local_time.tzinfo))
print("Aware UTC time {},time zone {}".format(aware_utc_time,aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015,10,25,1,30,0,0)
print(gap_time)
print(gap_time.timestamp())