#!/bin/bash

# Input file containing URLs, one per line
input_file="url_list.txt"

# Output file to record the response data
output_file="curl_results.txt"

# Create or overwrite the output file
> "$output_file"

# Loop through the URLs in the input file
while IFS= read -r url; do
  # Use curl to fetch the URL and append the response to the output file
  curl -s "$url" >> "$output_file"
done < "$input_file"

echo "Curl results have been saved to $output_file"
