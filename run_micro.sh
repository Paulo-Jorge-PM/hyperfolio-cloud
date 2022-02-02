#!/bin/bash
#teste
#DJANGO_PATH="./django/run.sh"
APIGATEWAY_PATH="./apigateway/run.sh"
AUTH="./django/run_auth.sh"
USERS="./django/run_users.sh"
POSTS="./django/run_posts.sh"
ASSETS="./django/run_assets.sh"
COCKROACHDB_PATH="./cockroachdb/run.sh"
STARDOG="./Stardog/start_stardog.sh"
STARDOG_STUDIO="./Stardog/start_studio_stardog.sh"

echo "KONGA Frontend: http://localhost:1337"
echo "KONG Requests: http://localhost:8000"
#echo "DJANGO at: http://localhost:8080"
echo "AUTH at: http://localhost:8001"
echo "USERS at: http://localhost:8002"
echo "POSTS at: http://localhost:8003"
echo "ASSETS at: http://localhost:8004"
echo "CockroachDB Admin at: http://localhost:8008"
echo "Stardog API at: http://localhost:5820"
echo "Stardog Studio at: http://localhost:7888"



gnome-terminal --tab --title="POSTS" -- "$POSTS"
echo "POSTS = DONE"

gnome-terminal --tab --title="STARTDOG" -- "$STARDOG"
echo "STARDOG API = DONE"

xdg-open http://localhost:8003/admin
xdg-open http://localhost:8003/api

exec bash
