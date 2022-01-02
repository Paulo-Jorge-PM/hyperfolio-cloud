#!/bin/bash

echo "STARTING APIGATEWAY"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

exec docker-compose up

#exec bash