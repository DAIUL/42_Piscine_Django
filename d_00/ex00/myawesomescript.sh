#!/bin/bash

curl -s -I $1 | grep -i "location" | cut -d" " -f2