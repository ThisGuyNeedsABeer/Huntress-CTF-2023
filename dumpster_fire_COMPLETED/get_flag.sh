#!/bin/bash

python ~/CTF/tools/firepwd/firepwd.py -d ~/CTF/huntress2023/forensics/dumpster_fire/dumpster_fire_extracted/home/challenge/.mozilla/firefox/bc1m1zlr.default-release/ | grep -o "flag{[^}]*}"
