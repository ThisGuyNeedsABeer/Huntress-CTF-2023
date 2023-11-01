#!/bin/bash

curl -sL https://pastebin.com/raw/SiYGwwcz | grep -oE flag{.*} --color=none
