#!/usr/bin/env python3.12

'''
This script is used to create a completion using the OpenAI API.
'''
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")
create = OpenAI(api_key=api_key)

# Create a completion
response = create.completions.create(
  model="gpt-4o-mini",
  prompt="Who created AI?"
)

print(response.choices[0].message.content)