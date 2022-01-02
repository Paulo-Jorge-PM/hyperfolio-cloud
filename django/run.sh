#!/bin/bash

echo "STARTING DJANGO"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

cd project

exec python3 manage.py runserver 8080

#$SHELL
#exec bash
