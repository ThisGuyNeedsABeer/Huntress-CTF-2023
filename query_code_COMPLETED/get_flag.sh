#!/bin/bash

zbarimg query_code.png | grep -o 'flag{[^}]*}' | sed 's/| //'
