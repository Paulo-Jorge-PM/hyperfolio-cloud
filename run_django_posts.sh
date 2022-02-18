#!/bin/bash

POSTS="./django/run_posts.sh"


echo "POSTS at: http://localhost:8003"

gnome-terminal --tab --title="POSTS" -- "$POSTS"
echo "POSTS = DONE"

xdg-open http://localhost:8003/admin
xdg-open http://localhost:8003/api

exec bash
