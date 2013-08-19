mysql -uroot -p -e 'DROP DATABASE IF EXISTS mythconverg;'
mysql -u root -p < /home/dougt/myth_src/mythtv-trunk/mythtv/database/mc.sql

mysql -uroot -p mysql
UPDATE user SET Password=PASSWORD('PASSWORD') WHERE user='mythtv';
FLUSH PRIVILEGES;

/home/dougt/myth_src/mythtv-trunk/mythtv/programs/scripts/database/mythconverg_restore.pl --verbose


