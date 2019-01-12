#!/bin/sh

DB=localmunch
USER=$1
PASS=$2

mysql -u $USER -p$PASS < create_database.sql
mysql -u $USER -p$PASS $DB < drop_tables.sql
mysql -u $USER -p$PASS $DB < create_tables.sql
