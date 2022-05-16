import argparse

argparser = argparse.ArgumentParser(
    "Replaces spaces in FASTA sequence headers with underlines.")
argparser.add_argument("input", type=str,
                       help="The original (input) file containing the FASTA headers.")
argparser.add_argument("output", type=str,
                       help="The destination path including the name of the modified files.")

args = argparser.parse_args()

input_file = open(args.input, "r")
output_file = open(args.output, "w+")
for line in input_file:
    if (line.startswith(">")):
        output_file.write(line.replace(" ", "_"))
    else:
        output_file.write(line)

input_file.close()
output_file.close()
