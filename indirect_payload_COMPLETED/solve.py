import requests

# Input file containing URLs, one per line
input_file = 'url_list.txt'

# Output file to record curl results
output_file = 'curl_results.txt'

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        url = line.strip()  # Remove leading/trailing whitespace

        # Make an HTTP GET request using requests
        try:
            response = requests.get(url)
            response_text = response.text
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            response_text = f"Error: {str(e)}"
            status_code = -1  # An arbitrary value for error

        # Write the URL, status code, and response to the output file
        outfile.write(f"URL: {url}\n")
        outfile.write(f"Status Code: {status_code}\n")
        outfile.write(f"Response:\n{response_text}\n")
        outfile.write("\n")

print(f"Curl results have been saved to {output_file}")
