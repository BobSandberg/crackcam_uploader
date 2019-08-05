#!/bin/bash

image_path=`/home/pi/crackcam_uploader/take_photo.py | tail -n 1`
/home/pi/crackcam_uploader/uploader.py /home/pi/crackcam_uploader/uploader.cfg $image_path snap
