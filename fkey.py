import pandas as pd
import argparse

def main(input_file, output_file, keywords):
    df = pd.read_csv(input_file)

    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains('|'.join(keywords), case=False).any(), axis=1)]

    filtered_df.to_csv(output_file, index=False)

    print(f'Filtered rows have been written to {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract rows from a CSV file based on specified keywords.')

    parser.add_argument('-i', '--input_file', type=str, required=True, help='Input file name (CSV)')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Output file name (CSV)')
    parser.add_argument('-k', '--keywords', nargs='+', required=True, help='List of keywords to filter on')

    args = parser.parse_args()

    main(args.input_file, args.output_file, args.keywords)
