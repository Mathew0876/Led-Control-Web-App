# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

import time
import lirccontrol
#import subprocess

#GPIO.setwarnings(False)

# Decodes the request and calls the function
# to execute the button request
def remote(request):
    if '1' in request.POST:
        lirccontrol.lightup()
    elif '2' in request.POST:
        lirccontrol.lightdown()
    elif '3' in request.POST:
        lirccontrol.pause()
    elif '4' in request.POST:
        lirccontrol.on()
    elif '5' in request.POST:
        lirccontrol.red()
    elif '6' in request.POST:
        lirccontrol.green()
    elif '7' in request.POST:
        lirccontrol.blue()
    elif '8' in request.POST:
        lirccontrol.white()
    elif '9' in request.POST:
        lirccontrol.orange()
    elif '10' in request.POST:
        lirccontrol.lightgreen()
    elif '11' in request.POST:
        lirccontrol.deepblue()
    elif '12' in request.POST:
        lirccontrol.milkwhite()
    elif '13' in request.POST:
        lirccontrol.deepyellow()
    elif '14' in request.POST:
        lirccontrol.cyan()
    elif '15' in request.POST:
        lirccontrol.bluepurple()
    elif '16' in request.POST:
        lirccontrol.pinkwhite()
    elif '17' in request.POST:
        lirccontrol.yellow()
    elif '18' in request.POST:
        lirccontrol.lightblue()
    elif '19' in request.POST:
        lirccontrol.purple()
    elif '20' in request.POST:
        lirccontrol.greenwhite()
    elif '21' in request.POST:
        lirccontrol.lightyellow()
    elif '22' in request.POST:
        lirccontrol.skyblue()
    elif '23' in request.POST:
        lirccontrol.brown()
    elif '24' in request.POST:
        lirccontrol.bluewhite()
    elif '25' in request.POST:
        lirccontrol.increasered()
    elif '26' in request.POST:
        lirccontrol.increaseblue()
    elif '27' in request.POST:
        lirccontrol.increasegreen()
    elif '28' in request.POST:
        lirccontrol.faster()
    elif '29' in request.POST:
        lirccontrol.reducered()
    elif '30' in request.POST:
        lirccontrol.reduceblue()
    elif '31' in request.POST:
        lirccontrol.reducegreen()
    elif '32' in request.POST:
        lirccontrol.slower()
    elif '33' in request.POST:
        lirccontrol.diy1()
    elif '34' in request.POST:
        lirccontrol.diy2()
    elif '35' in request.POST:
        lirccontrol.diy3()
    elif '36' in request.POST:
        lirccontrol.auto()
    elif '37' in request.POST:
        lirccontrol.diy4()
    elif '38' in request.POST:
        lirccontrol.diy5()
    elif '39' in request.POST:
        lirccontrol.diy6()
    elif '40' in request.POST:
        lirccontrol.flash()
    elif '41' in request.POST:
        lirccontrol.jump3()
    elif '42' in request.POST:
        lirccontrol.jump7()
    elif '43' in request.POST:
        lirccontrol.fade3()
    elif '44' in request.POST:
        lirccontrol.fade7()
    return render(request,'control_page.html')

