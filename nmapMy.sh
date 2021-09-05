#!/bin/bash
ports=$(nmap -p- --min-rate=1000 -T4 10.10.10.27 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
echo $ports
nmap -sC -sV -p$ports 10.10.10.27
