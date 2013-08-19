import re
import os

from MythTV import MythDB, MythBE

import smtplib
from email.mime.text import MIMEText

import commands



def sendMessage(error):
  print "sending email: " + error

  msg = MIMEText(error)
  msg['Subject'] = 'Myth Server had a problem'
  msg['From'] = 'myth@dougt.org'
  msg['To'] = 'dougt@dougt.org'
  s = smtplib.SMTP('mail.dougt.org')
  s.sendmail('myth@dougt.org', 'dougt@dougt.org', msg.as_string())
  s.quit()

output = commands.getoutput('ps -A')
if 'mythbackend' not in output:
  sendMessage("Could not find mythbackend process!");
  exit(-1)

db = None
try:
  db = MythDB()
except:
  db = None

if db == None:
  sendMessage("Database could not be open or found")
  exit(-1)

be = None
try:
  be = MythBE()
except:
  be = None

if be == None:
  sendMessage("Backend could not be found")
  exit(-1)

if len(be.getRecorderList()) != 2:
  sendMessage("Tuner list is not what we expected")
  exit (-1)

#if strftime("%S") == str('00') || strftime("%S") == str('30'):
#  exit(0)

for x in be.getRecorderList():

  filename = str(be.getCurrentRecording(x).filename)
  title    = str(be.getCurrentRecording(x).title)
  channel  = str(be.getCurrentRecording(x).channum)
  start    = str(be.getCurrentRecording(x).starttime)

  # this is weird.  x still returns something (a None program)
  # even though nothing is being recorded
  if be.getCurrentRecording(x).title == None:
    continue

  if os.path.exists(filename) == False:
     sendMessage("Current recording (" + title + ") on channel (" + channel + ") does not have a file.  See " + filename + " time: " + start);
     exit (-1)

  size = os.path.getsize(filename)
  if (size <= 0):
    sendMessage("Current recording (" + title + ") on channel  (" + channel + ") does not have a file size");
    exit (-1)

exit(0)
