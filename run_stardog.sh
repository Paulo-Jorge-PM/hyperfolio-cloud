#!/bin/bash


STARDOG="./Stardog/start_stardog.sh"
STARDOG_STUDIO="./Stardog/start_studio_stardog.sh"


echo "Stardog API at: http://localhost:5820"
echo "Stardog Studio at: http://localhost:7888"

gnome-terminal --tab --title="STARTDOG" -- "$STARDOG"
echo "STARDOG API = DONE"

gnome-terminal --tab --title="STARDOG_STUDIO" -- "$STARDOG_STUDIO"
echo "STARDOG STUDIO = DONE"

xdg-open http://localhost:7888

exec bash
