rm *.zip

python separate.py test2
zip -9 normal.zip test2
zip -9 sep.zip test2_*
