#!/bin/bash

cat output.txt | grep -o 'FLAG{[^}]*}' | tr '[:upper:]' '[:lower:]'
