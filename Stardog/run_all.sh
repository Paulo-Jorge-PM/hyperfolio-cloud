#!/bin/bash

echo "Run Stardog Docker"

#Make it execute relative to here even if called from other script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

#exec docker start stardog
#exec docker start stardog-studio

docker run -it -p 5820:5820 -v ~/stardog-home/:/var/opt/stardog stardog/stardog
exec docker run --name=stardog-studio -p 7888:8080 -d stardog/stardog-studio:current

#Open localhost ports in browser
#Stardog API
xdg-open http://localhost:5820
#Stardog Studio
xdg-open http://localhost:7888


#Default Admin log in:
#admin
#Passw0rd1

#exec bash