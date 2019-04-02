#!/usr/local/bin/bash



html_report="/path/to/table/example.html"
result_file="/path/to/folder/tmp"


echo "<html><head><body><style>" >> $html_report
echo "*{font-family:Helvetica;}" >> $html_report
echo "table{border-collapse:collapse;table-layout:fixed;width:100%;}" >> $html_report
echo "table td, th{border:solid 1px #fab;word-wrap:break-word;}" >> $html_report
echo "</style></head><body>" >> $html_report
echo "<h1>All Tests $(date) </h1>" >> $html_report

test_counter=0
result_folder=$result_file/*.txt

for text_res_file in $result_folder; do
	((test_counter++))
	if [ ! -s $text_res_file ]; then
		echo "<h2> TEST $test_counter. $text_res_file</h2>" >> $html_report
		echo "<table border='1' width='100%'>" >> $html_report
		echo "<tr bgcolor='Tan'><th width='5%'>#</th><th width='20%'>ID</th><th width='69%'>Result</th><th width='6%'>Status</th></tr>" >> $html_report
		echo "<tr bgcolor='IndianRed'><td>1</td><td>$text_res_file</td><td>File is empty</td><td>FAILED</td></tr>" >> $html_report
		echo "</table>" >> $html_report
		continue
	fi
	echo "<h2> TEST $test_counter. $text_res_file</h2>" >> $html_report
	echo "<table border='1' width='100%'>" >> $html_report
	echo "<tr bgcolor='Tan'><th width='5%'>#</th><th width='20%'>ID</th><th width='69%'>Result</th><th width='6%'>Status</th></tr>" >> $html_report
	
	line_counter=0
	
	{
		while IFS=';' read -ra item; do
			((line_counter++))
			tr_bg_color="White"
			table_tds="<td>$line_counter</td>"
			
			for i in "${item[@]}"; do
				echo $i
				table_tds="$table_tds<td>$i</td>"
			done
			table_tr="<tr bgcolor='$tr_bg_color'>$table_tds</tr>"
			echo $table_tr >> $html_report
		done
	} < $text_res_file
	echo "</table>" >> $html_report
done