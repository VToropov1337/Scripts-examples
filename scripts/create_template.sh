#!/usr/local/bin/bash

html_report="/path/to/result/file.html"
result_file="/path/to/reports/for/show"


#create table
echo "<html><head><body><style>" >> $html_report
echo "*{font-family:Helvetica;}" >> $html_report
echo "table{border-collapse:collapse;table-layout:fixed;width:100%;}" >> $html_report
echo "table td, th{border:solid 1px #fab;word-wrap:break-word;}" >> $html_report
echo "</style></head><body>" >> $html_report

#create a title
echo "<h1>Title $(date) </h1>" >> $html_report

test_counter=0

#create a variable for all files in dir
files=$result_file/*.txt

#iterate for file and create a table for represent
for text_res_file in $files; do
	((test_counter++))
	echo "<h2> TEST $test_counter. $text_res_file</h2>" >> $html_report
	echo "<table border='1' width='100%'>" >> $html_report
	echo "<tr bgcolor='Tan'><th width='5%'>#</th><th width='20%'>ID</th><th width='69%'>Result</th><th width='6%'>Status</th></tr>" >> $html_report

	z=$(cat $text_res_file)
	counter=0
    #iterate for each line in file
	for i in $z; do
		((counter++))
		echo "<tr><td>$counter</td><td>$i</td><td>text from file</td><td>SUCCESS</td></tr>" >> $html_report
	done
	echo "</table>" >> $html_report
done