from pybtex.database.input import bibtex
import argparse
import csv

def main():
	arg_parser = argparse.ArgumentParser()
		
	arg_parser.add_argument('--inFile', required=True)
	arg_parser.add_argument('--outFile', required=True)
	args = arg_parser.parse_args()

	parser = bibtex.Parser()
	print("Parsing bibtext input")
	bib_data = parser.parse_file(args.inFile).entries.items()
	print("Finished parsing")
	output_table = [['ID', 'title', 'subject_lang', 'year']]

	for tb in bib_data:
	    metadata = tb[1]
	    temp_list = ['', '', '', '']
	    temp_list[0] = tb[0]

	    try:
	        temp_list[1] = metadata.fields['title']
	    except:
	        pass

	    try:
	        temp_list[2] = metadata.fields['lgcode']
	    except:
	        pass

	    try:
	        temp_list[3] = metadata.fields['year']
	    except:
	        pass
        
	    output_table.append(temp_list)

	with open(args.outFile, "w", encoding='utf-8', newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(output_table)

	print("All done! Exported to ", args.outFile)

if __name__ == "__main__":
	main()