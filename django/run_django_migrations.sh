#!/bin/bash

echo "Starting migrations"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

cd posts

exec python3 manage.py makemigrations

echo "Done 1: python3 manage.py makemigrations"

exec python3 manage.py migrate

echo "Done 2: python3 manage.py migrate"

exec bash
