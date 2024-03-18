# OpenAI Data Extraction and Processing Utility

This utility script is designed to automate the extraction of specific data from HTML content stored in an Excel file and to process this data for further use. The script utilizes OpenAI's GPT model to intelligently parse HTML content and extract relevant information, which is then formatted into JSON data. This data is subsequently processed and organized into a structured Excel file, facilitating easy access and analysis. The tool is particularly useful for scenarios requiring the extraction of structured information from unstructured HTML content, such as product details from web pages.

![Project Image Overview](https://github.com/DevRex-0201/Project-Images/blob/main/Py-OpenAI-HTML-Data-Extractor.png)

## Features

- **Data Extraction with OpenAI**: Leverages OpenAI's GPT model to extract specific pieces of information from HTML content.
- **JSON Data Formatting**: Formats the extracted information into JSON for easy manipulation and storage.
- **Excel Integration**: Reads from and writes to Excel files, allowing for straightforward input and output handling.
- **Error Handling**: Incorporates error handling for common issues like JSON parsing errors and file encoding problems.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.6 or later installed on your system.
- `pandas` library installed for handling Excel files.
- `openai` library installed and configured with your OpenAI API key for accessing GPT models.
- An Excel file (`source.xlsx`) containing the HTML content from which data will be extracted.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python libraries by running `pip install pandas openai`.
3. Place your source Excel file in the same directory as the script or modify the `file_path` variable to point to its location.

## Usage

1. **Data Extraction**: Execute the script to start the data extraction process. The script reads each row of the `Body HTML` column from the input Excel file, extracts data using the OpenAI API, and writes the extracted JSON data into `extracted_data.txt`.

2. **Data Processing**: After extraction, the script processes the JSON data, converting it into a structured format, and exports it to an output Excel file (`output_data.xlsx`).

3. **Configuration**: Modify the extraction and processing parameters within the script as needed to fit your specific requirements.

## Script Overview

The script comprises two main sections:

1. **Data Extraction**: Utilizes OpenAI's GPT model to parse HTML content and extract data based on predefined criteria. The extracted data is then formatted into JSON and saved to a text file.

2. **Data Processing**: Reads the JSON data from the text file, processes it to extract specific fields (e.g., "Spring-Rates" and "Fitment Warning"), and organizes the data into a pandas DataFrame. This DataFrame is then saved to an Excel file for easy access and analysis.

## Troubleshooting

- **JSON Parsing Errors**: If you encounter JSON parsing errors, check the format of the extracted data to ensure it's valid JSON.
- **File Not Found Errors**: Verify the paths to your input and output files are correct.
- **Unicode Decoding Errors**: Try opening your files with a different encoding if you encounter unicode decoding issues.

## License

This script is released under the MIT License. Feel free to modify, distribute, and use it in your projects with attribution.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

For any questions or issues, please open an issue in the repository, and we'll get back to you as soon as possible.
