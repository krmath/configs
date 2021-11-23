#!/bin/bash
# Places external monitor to the left of the laptop
xrandr --output eDP1 --auto --output HDMI2 --auto --left-of eDP1
nitrogen --restore
