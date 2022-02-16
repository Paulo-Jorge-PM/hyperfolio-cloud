#!/bin/bash


COCKROACHDB_PATH="./cockroachdb/run.sh"


echo "CockroachDB Admin at: http://localhost:8008"

gnome-terminal --tab --title="COCKROACHDB" -- "$COCKROACHDB_PATH"
echo "COCKROACHDB = DONE"

xdg-open http://localhost:8008

exec bash
