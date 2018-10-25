# Written By: Cameron Newton
# Date: Oct 25, 2018
# Description:  This script will issue commands to UWsim to move robot to certain position and export an image from
#               the front camera at that position. Must specify object name, start index for numbering, and max images

import subprocess, time
import numpy
import math
import os
import argparse

parser = argparse.ArgumentParser(description='Export images from the Uwsim simulator')
parser.add_argument('--object', help='The object in the simulator')

args = parser.parse_args()

dirname = str(os.getcwd()) + "/data/train_images"

image_saver = subprocess.Popen(
    "rosrun image_view image_saver image:=/uwsim/camera2 _save_all_image:=false _filename_format:=" + str(args.object) + "_%04i.jpg __name:=image_saver",
    shell=True,
    cwd=dirname)

time.sleep(1)

counter = 0

for x in numpy.arange(-5,-6,-1):
    for y in numpy.arange(-5, 6, 1):
        for z in numpy.arange(1, 5, 1):
            angle = math.atan(-y / (x+5))
            for newangle in numpy.arange(angle-0.3,angle+0.6,0.3):
                call = subprocess.Popen(
                    "rosrun uwsim setVehiclePosition /dataNavigator " + str(x) + " " + str(y) + " "
                    + str(z) + " 0 0 " + str(newangle),
                shell=True)
                subprocess.call("rosservice call /image_saver/save", shell=True)
            call.kill()
            time.sleep(0.05)
            counter += 1

call.terminate()
image_saver.terminate()

input("Press Enter")
