#!/bin/bash

cat purview.csv | grep flag | sed 's/""//g'| grep -o "Name,Value:." | cut -d ':' -f2| tr '\n' ' ' | sed 's/ //g'
