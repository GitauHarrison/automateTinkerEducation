import datetime
from time import sleep

end = datetime.datetime(2020, 5, 18, 7, 50, 0)
now = datetime.datetime.now()
delta = datetime.timedelta(hours = 0, minutes = 1, seconds =0)
print(delta)

a = 1
while now < end:
    print(now)
    print('Keep me logged in slack')
    sleep(3)

    #end += delta
if now == end:
    print('Log me out of slack')
    sleep(2)
    #break