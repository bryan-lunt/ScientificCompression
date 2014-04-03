rm *.zip test2 reconstituted

#curl http://www.gutenberg.org/cache/epub/1122/pg1122.txt > hamlet.txt


python test.py
python separate.py test2
zip -9 normal.zip test2
zip -9 sep.zip test2_*

python combine.py test2_text test2_numeric test2_table > reconstituted
