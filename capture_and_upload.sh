#!/bin/bash

set -e

PROGNAME=$(basename $0)

function exit_handler
{
    control_lights ALL_LIGHTS_OFF
    echo "$PROGNAME: ${:- "Unknown Error"}" 1>&2
    exit 1
}

trap exit_handler 0 1 2 3 6 9 15

cd /home/pi/crackcam_uploader/

# Turn on photo lighting
python3 bright-pi.py ON --gain 9 --pause 3

# Take picture (and retrieve jpg file of picture)
image_path=`python take_photo.py | tail -n 1`

# Upload file to Google Drive folder
python uploader.py uploader.cfg $image_path snap

# Turn off photo lighting
python3 bright-pi.py OFF

cd -