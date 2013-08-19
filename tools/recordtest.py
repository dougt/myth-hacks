
import time
import datetime
from MythTV import Record

today = datetime.date.today()
starttime = time.localtime().tm_hour * (60 * 60) + (time.localtime().tm_min + 1) * (60)
endtime   = starttime + 60


print today
print starttime
print endtime

rec = Record()
rec.chanid = 1234
rec.startdate = datetime.date(2011,1,28)
rec.enddate   = datetime.date(2011,1,28)
rec.starttime = datetime.timedelta(0,75600)
rec.endtime   = datetime.timedelta(0,75660)
rec.type = Record.kSingleRecord
rec.create()

rec = Record()
rec.chanid = 702
rec.startdate = today
rec.enddate   = today
rec.starttime = starttime
rec.endtime   = endtime
rec.type = Record.kSingleRecord
rec.create()


