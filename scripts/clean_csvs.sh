#!/bin/bash

find /usr/local/apps/PEW-EFH/mediaroot/csvs/*.csv -ctime +1 -exec rm {} \;

