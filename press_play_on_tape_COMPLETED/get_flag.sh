#!/bin/bash

cat default.prg| tr '[:upper:]' '[:lower:]' | sed -n 's/flag\[\([^]]*\)]/flag{\1}/p' | cut -d "\"" -f2
