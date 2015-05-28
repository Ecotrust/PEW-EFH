from django.core.management.base import BaseCommand, CommandError
import csv
from scenarios.models import PlanningUnitHabitatLookup, GridCell


class Command(BaseCommand):
    args = '<csv>'
    help = 'Import habitat/planning-unit lookup table. 1 argument - the csv to be imported'

    def handle(self, *args, **options):
        header_map = {
            'OBJECTID': {'name': 'object_id', 'type': 'int'},
            'PUG_ID': {'name': 'pug', 'type': 'fk'},
            'SGH': {'name': 'sgh_id', 'type': 'int'},
            'LU_CODE': {'name': 'sgh_lookup_code', 'type': 'str'}
        }
        PlanningUnitHabitatLookup.objects.all().delete()
        import_count = 0
        try:
            in_file = args[0]
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the CSV file to be imported! ---')
            import sys
            sys.exit()
        with open(in_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            headers = reader.next()
            for row in reader:
                hab_dict = {}
                for idx, val in enumerate(row):
                    map_val = header_map[headers[idx]]
                    if val == '':
                        hab_dict[map_val['name']] = None
                    elif map_val['type'] == 'int':
                        hab_dict[map_val['name']] = int(float(val))
                    elif map_val['type'] == 'fk':
                        pu = GridCell.objects.get(unique_id=int(float(val)))
                        hab_dict[map_val['name']] = pu
                    elif map_val['type'] == 'str':
                        hab_dict[map_val['name']] = val
                PlanningUnitHabitatLookup.objects.create(**hab_dict)
                import_count += 1

        self.stdout.write('Successfully added %s Habitat/Planning-Unit Lookup records' % import_count)
