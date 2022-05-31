rm *.zip test2.txt* reconstituted.txt

#curl http://www.gutenberg.org/cache/epub/1122/pg1122.txt > hamlet.txt


python produce_random_input.py > test2.txt
python separate.py test2.txt
zip -9 normal.zip test2.txt
zip -9 sep.zip test2.txt_*

NORMAL_SIZE=$(ls -l normal.zip | awk '{print $5;}')
SEPARATE_SIZE=$(ls -l sep.zip | awk '{print $5;}')

echo ratio of zip file sizes is $(bc <<< "scale=3; ${SEPARATE_SIZE} / ${NORMAL_SIZE} ")

python combine.py test2.txt_text test2.txt_numeric test2.txt_table > reconstituted.txt
diff -q test2.txt reconstituted.txt

if [ "$?" -ne "0" ]
then
	echo "files differed"
else
	echo "files identical"
fi
