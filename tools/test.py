import re
import os

from MythTV import MythDB, MythBE


def filepathFromRecording(recording):
  reuri = re.compile(\
    'myth://((?P<group>.*)@)?(?P<host>[a-zA-Z0-9_\.]*)(:[0-9]*)?/(?P<file>.*)')
  reip = re.compile('(?:\d{1,3}\.){3}\d{1,3}')

  # process URI (myth://<group>@<host>[:<port>]/<path/to/file>)
  match = reuri.match(recording.filename)
  if match is None:
    return None
  
  filename = match.group('file')

  # only use the first one
  sg = db.getStorageGroup( recording.storagegroup ).next()

  return sg.dirname + filename

def filepathToScreenshotFromRecording(recording):
  filepath = filepathFromRecording(recording)
  return filepath + ".png"

  

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


recordings = be.getRecordings()


for r in recordings:
  filepath = filepathFromRecording(r);
  size = -1
  try:
    size = os.path.getsize(filepath) / 1024 / 1024
  except:
    size = "NaN"

  ss_filepath = filepathFromRecording(r)
  ss_size = -1
  try:
    ss_size = os.path.getsize(filepath) / 1024 / 1024
  except:
    ss_size = "NaN"

  print filepath + " is " + str( size ) + "MB. The screen shot it only " + str (ss_size)
  
