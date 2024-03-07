from RAG.config_data import entity_types, relation_types, client, graph
from RAG.pre import define_query
import json

system_prompt_query = f'''
    You are a useful agent designed to create precise queries to retrieve information from a graph database. 
    
    The graph database links games to the following entity types:
    {json.dumps(entity_types)}
    Each link has one of the following relationships:
    {json.dumps(relation_types)}

    Depending on the user prompt, determine if it possible to answer with the graph database.
        
    The graph database can match games with multiple relationships to several entities.
    
    The input is a json databag of type including the game name and information about that game

    Example user input:
    "Can you introduce me to the top backers of Axie Infinity?"
    Relationships to analyse: Mentioning top backers means finding "top backers" that belong to that game
    
    Example user input:
    {{
        "game name": "axie-infinity",
        "information for the game": ["play mode"]
    }}
    Answer: MATCH (game:GAMES {{name: "axie-infinity"}}) RETURN game.play_mode
    
    Orther example user input:
    {{
        "game name": "gods-unchained",
        "information for the game": ["team profile", "staffs"]
    }}
    Answer: MATCH (game:GAMES {{"name": "gods-unchained"}})-[:HAVE_TEAM]->(teamprofile:TEAMPROFILE)-[:HAVE_STAFF]->(staffs:STAFFS) RETURN teamprofile, staffs
    Orther example user input:
    {{
        "game name": "axie-infinity",
        "information for the game": ["top backers"]
    }}
    Answer: MATCH (g:GAMES {{"name": 'axie-infinity'}})-[:HAVE_TOP_BACKERS]->(topbackers:TOPBACKERS) RETURN topbackers
    If no information is provided in the "information for the game" section, a query about about for that game is returned
    Do not response with any explanation or any other information except the Cypher query.
    If can not generate a Cypher query, then say "NOT_A_CYPHER"
'''
def create_query(prompt, model="gpt-3.5-turbo-0125"):
    completion = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
        {
            "role": "system",
            "content": system_prompt_query
        },
        {
            "role": "user",
            "content": prompt
        }
        ]
    )
    return completion.choices[0].message.content
# data = define_query("Hi")
# print(data)
# message = create_query(data)
# print(message)
# print(graph.query(message))
def process(question, conversation):
    data = define_query(question,conversation)
    print(data)
    message = create_query(data)
    print(message)
    if(message == "NOT_A_CYPHER"):
        return []
    return graph.query(message)
