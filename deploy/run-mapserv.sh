#!/bin/sh
### BEGIN INIT INFO
# Provides:           mapserv
# Required-Start:     $all
# Required-Stop:
# Default-Start:      2 3 4 5
# Default-Stop:
# Short-Description:  Starts mapserv service
### END INIT INFO

service mapserv start
sleep 5
service mapserv restart
