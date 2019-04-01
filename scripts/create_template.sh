#!/usr/local/bin/bash



html_report="/Users/mac/Desktop/practice/index3.html"
result_file="/Users/mac/Desktop/practice/temp"

#create table
echo "<html><head><body><style>" >> $html_report
echo "*{font-family:Helvetica;}" >> $html_report
echo "table{border-collapse:collapse;table-layout:fixed;width:100%;}" >> $html_report
echo "table td, th{border:solid 1px #fab;word-wrap:break-word;}" >> $html_report
echo "</style></head><body>" >> $html_report
echo "<h1>Tests $(date) </h1>" >> $html_report


test_counter=0
files=$result_file/*.txt
#iterate for files
for text_res_file in $files; do
	((test_counter++))
	echo "<h2> TEST $test_counter. $text_res_file</h2>" >> $html_report
	echo "<table border='1' width='100%'>" >> $html_report
	echo "<tr bgcolor='Tan'><th width='5%'>#</th><th width='20%'>ID</th><th width='69%'>Result</th><th width='6%'>Status</th></tr>" >> $html_report
	first_line=$(head -n 1 < $text_res_file)
	counter=0
	{
		read;
		while read line; do
			((counter++))
			echo "<tr><td>$counter</td><td>$line</td><td>text from file</td><td>SUCCESS</td></tr>" >> $html_report
			# if [ -z "$line" ]; then
			echo $counter-$text_res_file
		done
		#check for empty files
		if [ $counter -eq 0 ]; then
			echo "<tr bgcolor='IndianRed'><td>1</td><td>$text_res_file</td><td>File is empty</td><td>FAILED</td></tr>" >> $html_report
		fi
	} < $text_res_file
	echo "</table>" >> $html_report
done