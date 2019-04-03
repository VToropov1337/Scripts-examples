#!/usr/local/bin/bash

echo "${BASH_SOURCE[0]} is running"
source ./properties.sh



result_folder=`pwd`
api=${result_folder}/api.txt

echo "тест на доступность "$(date) >> $api


for k in ${!sites[*]}
do
    res=$(python3 py1.py -f "https://${sites[$k]}")
    echo "https://${sites[$k]}", ${res}, $(date)  >> $api
  	exitcode=$?
done
echo $exitcode

