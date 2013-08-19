from MythTV import MythDB, MythBE

db = None
db = MythDB()

if db == None:
  print "Database could not be open or found"
  exit()


be = None
be = MythBE()

if be == None:
  print "Backend could not be found."
  #exit()


for x in be.getRecorderList():
  print "Tuner " + str(x) + " is recording: " + str(be.getCurrentRecording(x).title)


fs = be.getFreeSpace()
print "----------------------------------"
for x in fs:
  print "Host: " + x.host
  print "\tPath: " + x.path
  print "\t\tTotal space: " + str(x.totalspace / 1024 / 1024) + "MB"
  print "\t\tFree  space: " + str(x.freespace / 1024  / 1024) + "MB"
  print "\t\tUsed  space: " + str(x.usedspace / 1024  / 1024) + "MB"
  print "----------------------------------"


