#shell 的空格很重要
file_number=22
new_file_path=0000
flag=9
while :
do
	if [ ! -d "$new_file_path" ]; then
		mkdir "$new_file_path"
		cd "$new_file_path"
		touch readme.md
		exit 0
	fi
	file_number=$[$file_number+1]
	if [ $file_number -gt $flag ]; then
		new_file_path="00"$file_number""
	else
		new_file_path="000"$file_number""
	fi
done