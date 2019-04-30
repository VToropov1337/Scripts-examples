#!/usr/local/bin/bash

jmx_file='/Users/mac/Desktop/practice/Jmeter/Test_1.jmx'
csv_result_folder='/Users/mac/Desktop/practice/Jmeter/result.csv'
jmeter_path='/Users/mac/Downloads/apache-jmeter-5.1.1/bin/jmeter.sh'
html_result_folder='/Users/mac/Desktop/practice/Jmeter/result.html'



echo "*********** Running ************"

sh $jmeter_path -n -t $jmx_file -l $csv_result_folder -e -o $html_result_folder

