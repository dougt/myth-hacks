from MythTV import MythDB, Record

my_myth_db = MythDB(args=(('DBHostName', 'localhost'),
                                  ('DBName', 'mythconverg'),
                                  ('DBUserName', 'root'),
                                  ('DBPassword', ''),
                                  ('DBPort', '3306')))

shows = my_myth_db.searchGuide(category="Special")
for x in shows:
  x.record(Record.kFindOneRecord)

