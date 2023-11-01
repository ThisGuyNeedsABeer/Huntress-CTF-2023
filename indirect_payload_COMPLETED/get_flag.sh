#!/bin/bash

cat curl_results.txt | cut -d "s" -f2 | tr -d '\n' | tr -d ' ' | rev | cut -c 2- | rev
