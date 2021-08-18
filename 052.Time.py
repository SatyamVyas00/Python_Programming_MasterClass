# import time
# print(time.gmtime(0))
# print(time.localtime(time.time()))
# print(time.time())

# time_here =  time.localtime()
# print(time_here)
# print("Year:",time_here[0],time_here.tm_year)
# print("Month:",time_here[1],time_here.tm_mon)
# print("Day:",time_here[2],time_here.tm_mday)

# import time
#from time import time as my_timer
#from time import perf_counter as my_timer
#from time import monotonic as my_timer
# from time import process_time as my_timer
# import random
#
# input("Press Enter to Start")
# wait_time = random.randint(1,6)
# time.sleep(wait_time)
# start_time = my_timer()
#
# input("Press Enter to Stop")
# end_time = my_timer()
# print("Started At: "+time.strftime("%X",time.localtime(start_time)))
# print("Ended At: "+time.strftime("%X",time.localtime(end_time)))
# print("Your Reaction Time was {} seconds".format(end_time-start_time))

# import time
# print("time():\t\t\t",time.get_clock_info('time'))
# print("perf_counter():\t",time.get_clock_info('perf_counter'))
# print("monotonic():\t",time.get_clock_info('monotonic'))
# print("process_time():\t",time.get_clock_info('process_time'))

import time
print("The epoch on this system starts at "+time.strftime('%c',time.gmtime(0)))

print("The Current Timezone is {0} with an offset of {1}".format(time.tzname[0],time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving is in effect for this location")
    print("\tThe DST timezone is "+time.tzname[1])

print("Local time is "+time.strftime('%Y-%m-%d %H-:%M:%S',time.localtime()))
print("UTC time is "+time.strftime('%Y-%m-%d %H-:%M:%S',time.gmtime()))

