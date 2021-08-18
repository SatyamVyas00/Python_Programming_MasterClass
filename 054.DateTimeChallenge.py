import pytz,datetime
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x,pytz.country_names[x]),end=':')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone,pytz.country_timezones[x]))



while True:
    timezones=  ("CN","FR","GB","IN","JP","US")
    zone_list = []
    zone_tupple = ()
    choice = None
    zone_choice = None


    print("Countries:")
    for index,country in enumerate(timezones):
        print("{}: {}".format(index+1,pytz.country_names[country]))

    choice = int(input("Choose Country: "))-1

    if choice < 0:
        break

    if choice in range(len(timezones)):
        country_choice = pytz.country_names[timezones[choice]]
        if timezones[choice] in pytz.country_timezones:
            for zone in sorted(pytz.country_timezones[timezones[choice]]):
                zone_list.append(zone)

        zone_tupple = tuple(zone_list)
        zone_list = []
        print("\tZones:")

        for index,zone in enumerate(zone_tupple):
            print("\t{}: {}".format(index+1,zone))
        zone_choice = int(input("\tChoose Zone: "))-1
        if zone_choice < 0:
            choice

    if zone_choice in range(len(zone_tupple)):
        tz_to_display = pytz.timezone(zone_tupple[zone_choice])
        local_time = datetime.datetime.now(tz=tz_to_display)
        utc_time = datetime.datetime.utcnow()

        print("Local time is {}".format(local_time))
        print("UTC time is {}".format(utc_time))