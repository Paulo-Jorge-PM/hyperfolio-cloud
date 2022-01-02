#!/bin/bash

#DJANGO_PATH="./django/run.sh"
APIGATEWAY_PATH="./apigateway/run.sh"
AUTH="./django/run_auth.sh"
USERS="./django/run_users.sh"
POSTS="./django/run_posts.sh"
ASSETS="./django/run_assets.sh"
COCKROACHDB_PATH="./cockroachdb/run.sh"


echo "KONGA Frontend: http://localhost:1337"
echo "KONG Requests: http://localhost:8000"
#echo "DJANGO at: http://localhost:8080"
echo "AUTH at: http://localhost:8001"
echo "USERS at: http://localhost:8002"
echo "POSTS at: http://localhost:8003"
echo "ASSETS at: http://localhost:8004"
echo "CockroachDB Admin at: http://localhost:8008"


gnome-terminal --tab --title="APIGATEWAY" -- "$APIGATEWAY_PATH"
echo "APIGATEWAY = DONE"

gnome-terminal --tab --title="POSTS" -- "$POSTS"
echo "POSTS = DONE"

gnome-terminal --tab --title="COCKROACHDB" -- "$COCKROACHDB_PATH"
echo "COCKROACHDB = DONE"

#xdg-open http://localhost:1337
#xdg-open http://localhost:8008
#xdg-open http://localhost:8003/admin
#xdg-open http://localhost:8003/api

exec bash