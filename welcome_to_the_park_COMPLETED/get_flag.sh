#!/bin/bash

exiftool -v5 JohnHammond.jpg | grep -A 4 'flag' | cut -d ";" -f2 | cut -d "[" -f2 | cut -d "]" -f1 | tr "\n" " " | tr -d '[:space:]'
