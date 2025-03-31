from module import client

prompt = '''
Help me plan a beach vacation.
Step 1 - Specify four potential locations for beach vacations
Step 2 - State some accommodation options in each
Step 3 - State activities that could be done in each
Step 4 - Evaluate the pros and cons for each destination
'''

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a travel agent."},
        {"role": "user", "content": prompt}
    ]
    )

print(response.choices[0].message['content'])