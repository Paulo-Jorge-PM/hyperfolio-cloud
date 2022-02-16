#!/bin/bash


APIGATEWAY_PATH="./apigateway/run.sh"


echo "KONGA Frontend: http://localhost:1337"
echo "KONG Requests: http://localhost:8000"

gnome-terminal --tab --title="APIGATEWAY" -- "$APIGATEWAY_PATH"
echo "APIGATEWAY = DONE"

xdg-open http://localhost:1337

exec bash
