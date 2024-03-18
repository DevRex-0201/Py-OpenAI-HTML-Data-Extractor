import pandas as pd
import json
import openai
import time
import re

# Function to extract data using OpenAI
def extract_data_with_openai(html_content):
    openai.api_key = 'API-Key'

    prompt = ("Please give me 'Part-Number', 'Spring-Rates', 'Fitment', and 'Fitment Warning' as only 1 level "
              "flat JSON data such as the below template from the above code. \n"
              "{\"Part-Number\": \"part_number\", \"Spring-Rates\": \"spring_rates\", "
              "\"Fitment\": \"fitment\", \"Fitment Warning\": \"fitment_warning\"} \n"
              "If some values are not exist, you must replace '' for not exist values.\n\n"
              "Keep in mind that you must give me only JSON data without any other texts or description")

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"{html_content}\n\n{prompt}",
        temperature=1,
        max_tokens=500,
        n=1,
        stop=None,
        presence_penalty=0,
        frequency_penalty=0.1,
    )   
    result = response.choices[0].text.strip().replace("\n", "").replace("  ", "").replace("'", '"')
    result = re.sub(r'.*?({.*?}).*', r'\1', result)
    return result

# Read the Excel file
file_path = 'source.xlsx'
df = pd.read_excel(file_path)

# Open a .txt file to write the extracted data
with open('extracted_data.txt', 'w') as file:
    # Extract data from each row
    for html_content in df['Body HTML']:
        json_data = extract_data_with_openai(html_content)
        print(json_data)
        try:
            # Write the JSON data to the file
            file.write(json_data + "\n")
        except json.JSONDecodeError:
            print("Error in JSON parsing:", json_data)
        time.sleep(5)
