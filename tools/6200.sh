#!/bin/bash
#

GUID=`echo "$1"|sed -r "s/[A-Z]+/\L&/g"`
CHANNEL=$2

NODE=`plugreport | grep $GUID | awk '{if (($1 == "Node")  && ($4 == "'"0x$GUID"'")) print $2}'`
echo "Node: '$NODE'"
echo "Changing to channel $CHANNEL"
6200ch -v -n $NODE $CHANNEL
#maybe a pause is needed?
sleep 4

exit 0

