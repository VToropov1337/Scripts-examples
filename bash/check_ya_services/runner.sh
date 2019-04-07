#!/usr/local/bin/bash
source ./prop.sh

res=$(
	python3 ya_api.py \
	-k "${!sites[@]}" \
	-v "${sites[@]}" \
	-f "$report_file" \
	)


if [ $? -eq 0 ]; then
	sh constructor.sh
fi
