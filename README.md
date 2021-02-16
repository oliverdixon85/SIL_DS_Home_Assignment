# SIL_DS_Home_Assignment

# Description 

In this assignment the aim was to convert a bibtex file to csv, then load then load the results into a database
and do some basic data analysis of the data. 
convert.py is a script that takes in BibTex files and writes a CSV. create_sql_database.py takes the csv file 
and loads it into an SQLite database. 

# Installation 

convert.py uses pybtex and can be installed by running "pip install pybtex" in the terminal.

# How to

for convert.py
Execute the following in the terminal to run:
python convert.py --inFile source.bib --outFile out.csv

for create_sql_databse.py
Execute the following in the terminal to run:
python create_sql_database.py 
This will be followed by a request to enter the csv name. Type out.csv 

Both languages.7z.001 and out.7z.001 are zipped files since the originals were too large for GitHub. To access,
download the files, right click, select 7Zip (if installed) and click on "Extract". The extracted files will be 
in the original form. 

The original source file from Glottolog is not included but can be downloaded from 
https://cdstar.shh.mpg.de/bitstreams/EAEA0-9478-C22F-4AAF-0/glottolog_source.bib.zip

# Results

Both programs worked and the SQLite database had one more entry than the csv and that's because the headers were included which added an extra row. I do think the create_sql_database.py could have been done more efficiently, it took very long, and I wasn't willing to risk a change and it take that long again, in which case I would not have had time to complete the assignment. 
