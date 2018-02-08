#!/usr/bin/env python3
import sys,gffutils
from optparse import OptionParser

def main(gff_file, output_file):

    db = gffutils.create_db(gff_file, dbfn="gff.db", merge_strategy="merge", force=True)

    output_file = open(output_file, 'w')
    output_file.write('transcript,gene\n')
    for i in db.features_of_type('mRNA'):
        gene = None
        transcript = None

        parent = i.attributes['Parent'][0]
        if parent.startswith('gene:'):
            gene = parent.replace('gene:', '')
        
        ID = i.attributes['ID'][0]
        if ID.startswith('transcript:'):
            transcript = ID.replace('transcript:', '') 

        if gene != None and transcript != None:
            output_file.write(transcript + "," + gene + '\n')
    output_file.close()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--gff", dest="gff_filename", help="GFF input file")
    parser.add_option("-o", "--output", dest="output_filename", help="Output filename")

    (options, args) = parser.parse_args()

    gff_file = options.gff_filename
    output_file = options.output_filename
   
    if gff_file == None:
        print("Must specify input GFF with --gff") 
        sys.exit(0)

    if output_file == None:
        print("Must specify output file with -o")
        sys.exit(0) 

    main(gff_file, output_file)

