#!/bin/bash

echo "Run Anzo Docker"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

#Stardog Studio
xdg-open http://localhost:7888

exec docker start stardog-studio

exec docker run --name=stardog-studio -p 7888:8080 -d stardog/stardog-studio:current



#Default Admin log in:
#admin
#Passw0rd1

#exec bash