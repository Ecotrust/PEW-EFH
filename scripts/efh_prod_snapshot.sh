#!/bin/bash

#######
# This script will create a snapshot of your current running AWS volume
# It then will remove any snapshots older than 3 months
#
# TODO: Insert values for:
#   * AWS_ACCESS_KEY_ID
#   * AWS_SECRET_ACCESS_KEY
#   * volumeid
#
# THEN:
#    Create cron job to run monthly
#      sudo crontab -e
#      0 10 1 * * /bin/bash /usr/local/apps/PEW-EFH/scripts/efh_prod_snapshot.sh (run at 10AM the first day of each month)

#######

export AWS_DEFAULT_REGION=us-west-2
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
volumeid=''

echo
echo ==========EFH PROD==========
process=`aws ec2 create-snapshot --volume-id $volumeid --description /dev/xvda1`
pid=$(echo $process | perl -nle'print $& if m{"SnapshotId": ".*?[^\\]"}' | sed 's/\"SnapshotId\": \"//g' | sed 's/\"//g')
echo creating snapshot $pid ...
status=`aws ec2 describe-snapshots --snapshot-ids $pid`
pct_done=$(echo $status | perl -nle'print $& if m{"Progress": ".*?[^\\]"}' | sed 's/\"Progress\": \"//g' | sed 's/\%"//g')
while [[ $pct_done != "100" ]]
do
    echo $pct_done% completed...
    sleep 10
    status=`aws ec2 describe-snapshots --snapshot-ids $pid`
    pct_done=$(echo $status | perl -nle'print $& if m{"Progress": ".*?[^\\]"}' | sed 's/\"Progress\": \"//g' | sed 's/\%"//g')
done
echo snapshot $pid completed

snapshots=`aws ec2 describe-snapshots --owner self --output json`

### parse_snapshots.py takes the json list of snapshots and the age at
###     which they are considered to be old in "DAYS"
old_snaps=`/usr/bin/python /usr/local/apps/PEW-EFH/scripts/parse_snapshots.py "$snapshots" 90`
IFS="|" read -a old_array <<< "$old_snaps"

for i in "${old_array[@]}"
  do
    echo ---------------------
    echo DELETING "$i"...
    aws ec2 delete-snapshot --snapshot-id $i
    echo SNAPSHOT "$i" DELETED
  done
echo ========END EFH PROD========
echo
