#!/bin/bash

cat base64_extracted | rev | tr 'A-Za-z' 'N-ZA-Mn-za-m' | base64 -d | grep -o 'flag{[^}]*}' | sed 's/| //'
