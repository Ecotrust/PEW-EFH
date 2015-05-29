from django.core.management.base import BaseCommand, CommandError
import csv
from scenarios.models import SpeciesHabitatOccurence, Species


class Command(BaseCommand):
    args = '<csv>'
    help = 'Import species-habitat occurence data. 1 argument - the csv to be imported'

    def handle(self, *args, **options):
        header_map = {
            'OBJECTID': {'name': 'object_id', 'type': 'int'},
            'SPECIESCOMMON': {'name': 'species_common', 'type': 'str'},
            'SPECIESSCI': {'name': 'species_sci', 'type': 'str'},
            'LIFESTAGE': {'name': 'lifestage', 'type': 'str'},
            'GENDER': {'name': 'sex', 'type': 'str'},
            'HABITATASSOCIATION': {'name': 'habitat_association', 'type': 'str'},
            'SEASON': {'name': 'season', 'type': 'str'},
            'LEVEL1HABITAT': {'name': 'level_1_habitat', 'type': 'str'},
            'LEVEL2HABITAT': {'name': 'level_2_habitat', 'type': 'str'},
            'LEVEL3HABITAT': {'name': 'level_3_habitat', 'type': 'str'},
            'LEVEL4HABITAT': {'name': 'level_4_habitat', 'type': 'str'},
            'Xwalk_sgh': {'name': 'xwalk_sgh', 'type': 'str'},
            'LU_Code': {'name': 'sgh_lookup_code', 'type': 'str'},
            'ACTIVITY': {'name': 'activity', 'type': 'str'},
            'ACTIVITYASSOCIATION': {'name': 'activity_association', 'type': 'str'},
            'Pmin_depth': {'name': 'preferred_min_depth', 'type': 'int'},
            'Pmax_depth': {'name': 'preferred_max_depth', 'type': 'int'},
            'Amin_depth': {'name': 'absolute_min_depth', 'type': 'int'},
            'Amax_depth': {'name': 'absolute_max_depth', 'type': 'int'}
        }

        SpeciesHabitatOccurence.objects.all().delete()
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
                    elif map_val['type'] == 'str':
                        hab_dict[map_val['name']] = val.lower()
                SpeciesHabitatOccurence.objects.create(**hab_dict)
                Species.objects.get_or_create(common_name=hab_dict['species_common'].lower(), scientific_name=hab_dict['species_sci'].lower())
                import_count += 1

        self.stdout.write('Successfully added %s Species Habitat Occurrence records' % import_count)
