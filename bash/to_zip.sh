#!/usr/local/bin/bash

log_file="users.txt"

log=$(stat -f%s $log_file)
#archive if file more than (bytes)
if [[ log > 4500 ]]; then
	time=$(date +"%F")
	zip "$time.zip" $log_file
fi