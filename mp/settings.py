# Django settings for lot project.
from madrona.common.default_settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIME_ZONE = 'America/Vancouver'
ROOT_URLCONF = 'urls'
LOGIN_REDIRECT_URL = '/visualize'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'efh',
        'USER': 'postgres',
    }
}

FEEDBACK_RECIPIENT = ["madrona@ecotrust.org"] # default value, actual emails are assigned in settings_local.py
FEEDBACK_SUBJECT = "PEW Essential Fish Habitat Marine Planner Feedback"


LOG_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__),
                            '..', 'mp.log'))
LOG_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), 'logs'))
UPLOAD_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'mediaroot', 'upload'))
ZIPFILE_DIR = '/tmp'
ZIPFILE_PATH = os.path.realpath(os.path.join(ZIPFILE_DIR, 'import_shp.zip'))
UPLOAD_ACTION_ATTR = 'RegAction'
UPLOAD_NAME_ATTR = 'SiteName'
UPLOAD_DESCRIPTION_ATTR = 'Desc'
DEFAULT_UPLOAD_LAYER_COLOR_HEX = '#FF4'

ADMIN_MEDIA_PATH = "/usr/local/venv/marine-planner/lib/python2.7/site-packages/django/contrib/admin/static/admin/"

INSTALLED_APPS += ('django_extensions',
                   'social.apps.django_app.default',
                   'general',
                   'scenarios',
                   'data_manager',
                   'mp_settings',
                   'drawing',
                   'explore',
                   'visualize',
                   'django.contrib.humanize',
                   'flatblocks',
                   'mp_proxy',
                   'map_proxy'
                   )

GEOMETRY_DB_SRID = 3857
GEOMETRY_CLIENT_SRID = 3857  # for latlon
GEOJSON_SRID = 3857

APP_NAME = "PEW EFH Marine Planner"
SERVER_ADMIN = 'rhodges@ecotrust.org'
DEFAULT_FROM_EMAIL = 'EFH Marine Planner Support <madrona@ecotrust.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = 'PEW EFH Marine Planner'
ADMINS = (
    ('Ryan Hodges', 'rhodges@ecotrust.org')
)
HELP_EMAIL = "efhsupport@ecotrust.org"

CONTENT_TYPES = ['image', 'video']

MAX_UPLOAD_SIZE = "5242880"

# FEEDBACK_RECIPIENT = "Marine Planning Team <mp-team@marineplanner.org>"
# DEFAULT_FROM_EMAIL = "Marine Planning Team <mp-team@marineplanner.org>"

# url for socket.io printing
SOCKET_URL = 'http://pewmp.ecotrust.org:8080'
# SOCKET_URL = False

# Change the following line to True,
# to display the 'under maintenance' template
UNDER_MAINTENANCE_TEMPLATE = False

TEMPLATE_DIRS = (
    os.path.realpath(os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/')),
    os.path.realpath(os.path.join(os.path.dirname(__file__), 'mp_profile/templates').replace('\\', '/')),
)


AUTHENTICATION_BACKENDS = (
    # 'social.backends.google.GooglePlusAuth',
    'auth.CustomGooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES += (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware'

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                     '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            # 'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'ERROR',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file':{
            'level' : 'ERROR',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(LOG_DIR, 'main.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount' : 7,
            'formatter': 'main_formatter',
            # 'filters': ['require_debug_false'],
        },
        'debug_file':{
            'level' : 'ERROR',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(LOG_DIR, 'main_debug.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount' : 7,
            'formatter': 'main_formatter',
            # 'filters': ['require_debug_true'],
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console', 'production_file',],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        'apps': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "ERROR",
        },
        'tracekit': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "ERROR",
        },
    }
}

SCENARIO_NAME = 'Drawing'
COLLECTION_NAME = 'Scenario'  #Confusing choice, I know. RDH

MAX_DETAIL_REPORT_AREA_SQMI = 50000     #Southern CA Bight is 16,250 sq mi
MAX_INTERSECTING_CELLS = 400000         #Southern CA Bight is 101,466
MAX_DETAIL_REPORT_AREA_VARIANCE = 0.3   #False or 1 to ignore, otherwise float between 0 and 1


COMPARISON_FIELD_LOOKUP = [
    {'name': 'Total Area', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Total Area Closed', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Total Area Reopened', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Depth Range', 'type': str, 'aggregate': 'minmax', 'unit': (' to ',' fathoms')},
    {'name': 'Mean Depth', 'type': int, 'aggregate': 'mean', 'unit': ' fathoms'},
    {'name': 'Soft', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Mixed', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Hard', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Inferred Rock', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 1 for all coral and sponges', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 2 for all coral and sponges', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 3 for all coral and sponges', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 4 for all coral and sponges', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 1 for Scleractinia coral', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 2 for Scleractinia coral', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 3 for Scleractinia coral', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
]

STRATUM_COMPARISON_FIELD_LOOKUP = [
    {'name': 'Total Area', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Total Area Closed', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Total Area Reopened', 'type': int, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Depth Range', 'type': str, 'aggregate': 'minmax', 'unit': (' to ',' fathoms')},
    {'name': 'Mean Depth', 'type': float, 'aggregate': 'mean', 'unit': ' fathoms'},
    {'name': 'Soft', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Mixed', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Hard', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'Inferred Rock', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 1 for all coral and sponges', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 2 for all coral and sponges', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 3 for all coral and sponges', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 4 for all coral and sponges', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 1 for Scleractinia coral', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 2 for Scleractinia coral', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
    {'name': 'PHS 3 for Scleractinia coral', 'type': float, 'aggregate': 'sum', 'unit': ' sq mi'},
]

COMPARISON_FIELD_LIST = ['name', 'Description'] + [x['name'] for x in COMPARISON_FIELD_LOOKUP]


SUMMARY_DEFAULT = '{"all": [{"title":"Status", "data":"Loading..."}]}'

CSV_URL = '/media/csvs/'
CSV_DIR = './mediaroot/csvs/'

# Must be a field on the drawings.models.GridCell model
# Must be present in STRATA_MAP
#REPORT_STRATA = ['strata_3x3']
REPORT_STRATA = ['strata_5x5']

STRATA_MAP = {
    'all':{
        'all':'all'
    },
    'strata_3x3':{
        '1':'Northern Shelf',
        '2':'Northern Upper Slope',
        '3':'Northern Lower Slope',
        '4':'Central Shelf',
        '5':'Central Upper Slope',
        '6':'Central Lower Slope',
        '7':'Southern Shelf',
        '8':'Southern Upper Slope',
        '9':'Southern Lower Slope'
    },
    'strata_5x5':{
        '1':'1 Cape Flattery to Pt Chehalis | 0fm-30fm',
        '2':'1 Cape Flattery to Pt Chehalis | 30fm-100fm',
        '3':'1 Cape Flattery to Pt Chehalis | 100fm-150fm',
        '4':'1 Cape Flattery to Pt Chehalis | 150fm-700fm',
        '5':'1 Cape Flattery to Pt Chehalis | greater than 700fm',
        '6':'2 Pt Chehalis to Cape Blanco | 0fm-30fm',
        '7':'2 Pt Chehalis to Cape Blanco | 30fm-100fm',
        '8':'2 Pt Chehalis to Cape Blanco | 100fm-150fm',
        '9':'2 Pt Chehalis to Cape Blanco | 150fm-700fm',
        '10':'2 Pt Chehalis to Cape Blanco | greater than 700fm',
        '11':'3 Cape Blanco to Cape Mendocino | 0fm-30fm',
        '12':'3 Cape Blanco to Cape Mendocino | 30fm-100fm',
        '13':'3 Cape Blanco to Cape Mendocino | 100fm-150fm',
        '14':'3 Cape Blanco to Cape Mendocino | 150fm-700fm',
        '15':'3 Cape Blanco to Cape Mendocino | greater than 700fm',
        '16':'4 Cape Mendocino to Pt Conception | 0fm-30fm',
        '17':'4 Cape Mendocino to Pt Conception | 30fm-100fm',
        '18':'4 Cape Mendocino to Pt Conception | 100fm-150fm',
        '19':'4 Cape Mendocino to Pt Conception | 150fm-700fm',
        '20':'4 Cape Mendocino to Pt Conception | greater than 700fm',
        '21':'5 Pt Conception to US/Mexico Border | 0fm-30fm',
        '22':'5 Pt Conception to US/Mexico Border | 30fm-100fm',
        '23':'5 Pt Conception to US/Mexico Border | 100fm-150fm',
        '24':'5 Pt Conception to US/Mexico Border | 150fm-700fm',
        '25':'5 Pt Conception to US/Mexico Border | greater than 700fm'
    }
}

import logging
logging.getLogger('django.db.backends').setLevel(logging.ERROR)

from settings_local import *
