import argparse

def remove_duplicates(input_file, output_file):
  """
  Removes duplicate subdomains from an input file and writes unique ones to an output file.

  Args:
    input_file: Path to the file containing subdomains.
    output_file: Path to the file where unique subdomains will be written.
  """
  seen_subdomains = set()  # Use a set to store unique subdomains efficiently

  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    print("Processing input file:", input_file)
    print("Writing output to:", output_file)

    for line in infile:
      subdomain = line.strip()  # Remove leading/trailing whitespace

      # Check if subdomain is unique and add it to the set if so
      if subdomain not in seen_subdomains:
        seen_subdomains.add(subdomain)
        outfile.write(subdomain + '\n')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Remove duplicate subdomains from a text file.")
  parser.add_argument("-i", "--input-file", required=True, help="Path to the input file")
  parser.add_argument("-o", "--output-file", required=True, help="Path to the output file")
  args = parser.parse_args()

  remove_duplicates(args.input_file, args.output_file)

  print("Script execution completed.")