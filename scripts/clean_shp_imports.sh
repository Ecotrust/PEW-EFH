#!/bin/bash

find /usr/local/apps/PEW-EFH/mediaroot/upload/ -maxdepth 1 -type f -ctime +1 -exec rm {} \;

