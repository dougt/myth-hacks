#!/bin/bash
for dev in /dev/video[0-9] ; do
        if v4l2-ctl -D -d $dev | grep -q 'Hauppauge HVR-1600' &>/dev/null ; then
                dd if=$dev bs=1024k count=2 > /dev/null
        fi
done

