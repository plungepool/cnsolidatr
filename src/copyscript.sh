#!/bin/sh
options=$1
config=$2

i=0
cat $config | while read -r line; do #loops thru lines in config file
	if [[ $i -eq 0 ]]; then #grabs destination from line 1
		echo "Destination folder is $line"
		destination=$line
		cd $destination
		if [[ $options -eq 2 ]]; then #backup current files in destination to backup folder
			backup=$destination
			backup+="/"
			mkdir "$(date +"%d-%m-%Y-%r")" && backup+=$_
			find "$destination" -type f -print0 | xargs -0 mv -t "$backup"
		else
			mv *.* ~/.Trash #moves all contents with file extensions to trash, excludes sub directories
		fi
	else
  	echo "Source folder is $line"
  	cd $line
  	unset -v latest
    for file in "$line"/*; do #finds latest file
      [[ $file -nt $latest ]] && latest=$file
    done
    cp $latest $destination #copies latest file to destination
  fi
  i=$i+1
done

echo "Task completed :)"
#exit 0