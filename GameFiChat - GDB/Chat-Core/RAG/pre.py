import json
from RAG.config_data import client
from RAG.config_data import entity_types, relation_types

system_prompt = f'''
    You are a helpful agent designed to fetch information from a graph database. 
    
    The graph database links games to the following entity types:
    {json.dumps(entity_types)}
    
    Each link has one of the following relationships:
    {json.dumps(relation_types)}

    Depending on the user prompt, determine if it possible to answer with the graph database.
        
    The graph database can match games with multiple relationships to several entities.
    
    Example user input:
    "Can you introduce me to the top backers of Axie Infinity?"
    Relationships to analyse: Mentioning top backers means finding "top backers" that belong to that game
    
    Example user input:
    "I want to know the play mode of Axie Infinity."
    Relationships to analyse: Look in the game properties to see if there is that component, here it is "play mode"
    
    Orther example user input:
    "Let's talk about the team profile of Axie Infinity."
    Relationships to analyse: In this input, there is mention of the game's team profile, and the team profile includes staffs, so please respond with information about staffs as well.
    Return a json object following the following rules:
    For each relationship to analyze, add a keyword about the game name, the game's attributes, and the relationships involved.
    
    For the example: "Let's talk about the team profile of Axie Infinity.", the expected output would be:
    {{
        "game name": "axie-infinity",
        "information for the game": ["team profile", "staffs"],
    }}
    For the example: "Introduce to me the play mode befitter game.", the expected output would be:
    {{
        "game name": "befitter",
        "information for the game": ["play mode"],
    }}
    If the input only gives the game name without providing anything else, the default information will be "about", "count rating", "community performance", "social score", "count likes"
    If you cannot determine the game name, do not query the graph database.
    If there are no relevant entities in the user prompt, return an empty json object.
'''

def define_query(prompt,conversation, model="gpt-3.5-turbo-0125"):
    messages = [{"role": "system", "content": system_prompt}] + conversation + [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model=model,
        temperature=0,
        response_format= {
            "type": "json_object"
        },
        messages=messages
    )
    return completion.choices[0].message.content

# print(define_query("Tell me about the play to earn model of Axie Infinity."))