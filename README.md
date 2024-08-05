# FKey
Threat Hunting - CSV Analysis tool


[Threat Hunting]

This tool can be used to speed up searching of data within csv files. 

It works by specifiying:

1.) Input file (csv ext)

2.) Output file (csv ext)

3.) Keywords (multiple can be specified)

The tool will iterate through each row & column within the specified input file and if the keyword is found it will extract the whole row that contains the keyword and write it to the output file. 

Example usage: 
python3 filter_keywords.py -i input_filename.csv -o output_filename.csv -k psexec netsh firewall mimikat  
