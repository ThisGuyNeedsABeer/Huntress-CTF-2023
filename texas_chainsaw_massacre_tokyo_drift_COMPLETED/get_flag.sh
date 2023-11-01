#!/bin/bash

echo "U3RhcnQtUHJvY2VzcyAiaHR0cHM6Ly95b3V0dS5iZS81NjFubmQ5RWJzcz90PTE2IgojZmxhZ3s0MDk1MzczNDdjMmZhZTAxZWY5ODI2YzI1MDZhYzY2MH0jCg==" | base64 -d | grep -oE flag{.*?} --color=none
