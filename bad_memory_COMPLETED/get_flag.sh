#!/bin/bash

echo -n goldfish# | md5sum | awk '{print "flag{" $1 "}"}'
