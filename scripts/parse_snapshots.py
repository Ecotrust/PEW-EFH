import sys
import json
import pytz
from dateutil import parser
from datetime import datetime, timedelta

snap_json = sys.argv[1]
old_days = int(sys.argv[2])
if len(sys.argv) > 3:
    start_year = int(sys.argv[3])
else:
    start_year = False
snaps = json.loads(snap_json)
old_snaps = []
for snap in snaps["Snapshots"]:
    old_time = parser.parse(snap["StartTime"])
    new_time = datetime.now()
    new_time = new_time.replace(tzinfo=pytz.utc)
    diff = timedelta(days=old_days)
    if old_time < (new_time - diff):
        if not start_year or old_time.year >= start_year:
            old_snaps.append(snap['SnapshotId'])

print '|'.join([str(x) for x in old_snaps])
