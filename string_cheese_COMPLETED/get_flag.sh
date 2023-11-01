#!/bin/bash

strings cheese.jpg | grep -o 'flag{[^}]*}' | sed 's/| //'
