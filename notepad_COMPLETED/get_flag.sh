#!/bin/bash

strings notepad | grep -o 'flag{[^}]*}' | sed 's/| //'
