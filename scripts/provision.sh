#!/bin/bash

PROJECT_NAME="PEW-EFH"

BASE_DIR=/usr/local/apps/$PROJECT_NAME
PROJECT_DIR=$BASE_DIR/mp
VIRTUALENV_DIR=/$BASE_DIR/pew-env
APP_DB_NAME="efh"
APP_DB_USER="postgres"

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip

PIP_DOWNLOAD_CACHE=/home/ubuntu/.pip_download_cache

USER="ubuntu"

# see https://docs.google.com/a/pointnineseven.com/document/d/1MbPbDp-Om1iIRb6bqhaKELqyU6x6E2KZ3Wm04tYAxak/edit#
cat << EOF | su - $APP_DB_USER -c psql
CREATE DATABASE $APP_DB_NAME;
\connect $APP_DB_NAME
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

insert into spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text)
values (99996, 'EPSG', 99996, 'Marco Albers', '+proj=aea +lat_1=37.25 +lat_2=40.25 +lat_0=36 +lon_0=-72 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs');

CREATE OPERATOR CLASS gist_geometry_ops
FOR TYPE geometry USING GIST AS
STORAGE box2df,
OPERATOR        1        <<  ,
OPERATOR        2        &<  ,
OPERATOR        3        &&  ,
OPERATOR        4        &>  ,
OPERATOR        5        >>  ,
OPERATOR        6        ~=  ,
OPERATOR        7        ~   ,
OPERATOR        8        @   ,
OPERATOR        9        &<| ,
OPERATOR        10       <<| ,
OPERATOR        11       |>> ,
OPERATOR        12       |&> ,

OPERATOR        13       <-> FOR ORDER BY pg_catalog.float_ops,
OPERATOR        14       <#> FOR ORDER BY pg_catalog.float_ops,
FUNCTION        8        geometry_gist_distance_2d (internal, geometry, int4),

FUNCTION        1        geometry_gist_consistent_2d (internal, geometry, int4),
FUNCTION        2        geometry_gist_union_2d (bytea, internal),
FUNCTION        3        geometry_gist_compress_2d (internal),
FUNCTION        4        geometry_gist_decompress_2d (internal),
FUNCTION        5        geometry_gist_penalty_2d (internal, internal, internal),
FUNCTION        6        geometry_gist_picksplit_2d (internal, internal),
FUNCTION        7        geometry_gist_same_2d (geom1 geometry, geom2 geometry, internal);

EOF

apt-get install python-gdal -y

# Virtualenv setup for project
bash -c "/usr/bin/virtualenv --python=/usr/bin/python2.7 --system-site-packages $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    PIP_DOWNLOAD_CACHE=$PIP_DOWNLOAD_CACHE $PIP install pillow && \
    PIP_DOWNLOAD_CACHE=$PIP_DOWNLOAD_CACHE $PIP install -r $PROJECT_DIR/../requirements.txt"

echo "workon $PROJECT_NAME" >> /home/$USER/.bashrc

# Run syncdb/migrate/update_index
bash -c "$PYTHON $PROJECT_DIR/manage.py syncdb"
bash -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput"
bash -c "$PYTHON $PROJECT_DIR/manage.py install_media"
bash -c "$PYTHON $PROJECT_DIR/manage.py enable_sharing --all"

# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/$USER/.bashrc
export PIP_DOWNLOAD_CACHE=$PIP_DOWNLOAD_CACHE
alias dj="$PYTHON $PROJECT_DIR/manage.py"
alias djrun="dj runserver 0.0.0.0:8000"
EOF
