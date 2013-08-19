#!/bin/bash
#
# Script to fix HVR-1600 audio initialization problems (v2):
#
# (1) fix stuttering of first analog recording, by tuning/recording a fragment.
# (2) fix(?) "no analog audio" problem by reloading driver if audio comes up muted.
#

for prog in ivtv-tune v4l2-ctl logger rmmod modprobe ; do
        if ! type -all "$prog" &>/dev/null ; then
                echo "$0: '$prog' not found on PATH, aborted." >&2
                exit 1
        fi
done

function initialize_tuner(){
        logger -- "$dev: $MYNAME: Pre-initializing"
        ivtv-tune -c 24 $dev &>/dev/null
        dd if=$dev bs=256k count=1 &>/dev/null  ## Fix "stuttering audio"
}

function check_mute(){
        for t in {0..15} ; do
                sleep 0.1
                mute=`v4l2-ctl -d $dev -C mute`
                [ "$mute" = "mute: 0" ] && exit
        done
        echo "muted"
}

function fix_tuners(){
        for dev in /dev/video[0-9] ; do
                if v4l2-ctl -D -d $dev | grep -q 'Hauppauge HVR-1600' &>/dev/null ; then
                        initialize_tuner
                        muted="`check_mute`"
                        if [ "$muted" != "muted" ]; then
                                logger -- "$dev: $MYNAME: HVR1600/cx18 audio ok."
                        else
                                logger -- "$dev: $MYNAME: HVR1600/cx18 audio bug, reloading cx18 driver"
                                rmmod cx18_alsa &>/dev/null
                                rmmod cx18 || logger -- "$dev: $MYNAME: rmmod cx18 failed"
                                modprobe cx18
                                break
                        fi
                fi
        done
        echo "$muted"
}

export MYNAME="${0##*/}"

rmmod cx18_alsa &>/dev/null     ## don't need this loaded, so get rid of it!
for t in {0..4} ; do
        [ "`fix_tuners 2>/dev/null`" == "muted" ] || exit 0
done
logger -- "$dev: $MYNAME: HVR1600/cx18 audio bug, reloading failed to fix it"
exit 1
