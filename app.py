import os
from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

document = LlamaParse(result_type="markdown").load_data("apple10K.pdf")

print(document[0].text[:1000])

file_name = "apple_10k.md"
with open(file_name, 'w') as file:
    file.write(document[0].text)
