function_definition = [{
    'type': 'function',
    'function': {
        'name': 'extract_job_info',
        'description': 'Extract job information from a job posting.',
        'parameters': {
            'type': 'object',
            'properties': {
                'job_title': {
                    'type': 'string',
                    'description': 'The title of the job.'
                },
                'location': {
                    'type': 'string',
                    'description': 'The location of the job.'
                }
            },
        }

    }
}]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            'role': 'user',
            'content': 'Extract job information from the following job posting.'
        },
        {
            'role': 'assistant',
            'content': 'Sure! Please provide the job posting.'
        }
    ],
    tools=function_definition,
)

print(response.choices[0].message.tool_calls[0].function.arguments)