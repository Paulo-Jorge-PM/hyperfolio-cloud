#!/bin/bash

echo "Run Stardog Docker"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

docker run -it -p 5820:5820 -v ~/stardog-home/:/var/opt/stardog stardog/stardog

#Stardog API
xdg-open http://localhost:5820


#Default Admin log in:
#admin
#Passw0rd1

#exec bash