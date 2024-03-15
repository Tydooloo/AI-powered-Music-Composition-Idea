from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a teacher of infinite that knows and be's you are basically a god of wisdom"},
        {"role": "user", "content": "teach me how to juggle 30 oranges at once as a mere human being Format the previous answer given as a daily routine for a whole week that can be repeated until the goal is fulfilled, space each day"},
    ]
)

# Extracting the last message's content
content = completion.choices[0].message[-1].content

print(content)