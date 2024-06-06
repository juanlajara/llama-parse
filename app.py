import os
from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

""" document = LlamaParse(result_type="markdown").load_data("FastFoods2020.pdf")

print(document[0].text[:1000])

file_name = "FastFoods2020.md"
with open(file_name, 'w') as file:
    file.write(document[0].text) """


documents_with_instruction = LlamaParse(
    result_type="markdown",
    parsing_instructions=""" This is a Schedule of Property Values 
    for a fast food account, I would like a summary of total insured value by state"""
).load_data("FastFoods2020.pdf")

file_name = "FastFoods2020.md"
with open(file_name, 'w') as file:
    file.write(documents_with_instruction[0].text)
