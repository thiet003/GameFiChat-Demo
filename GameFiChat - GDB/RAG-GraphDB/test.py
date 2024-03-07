from langchain.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
import json
from openai import OpenAI
# DB credentials
url = "bolt://localhost:7687"
username ="neo4j"
password = "thietdong264"

# Tạo một đối tượng graph
graph = Neo4jGraph(
    url = url,
    username = username,
    password = password
)
# Tạo query
# query = "CREATE (n:Person {name: 'Alice', age: 24})"
# results = graph.query(query)
# for record in results:
#     print(record)

# tạo truy vấn đối với cơ sở dữ liệu bằng Ngôn ngữ tự nhiên.
# chain = GraphCypherQAChain.from_llm(
#     ChatOpenAI(temperature=0), graph=graph, verbose=True,
# )
# chain.run("game axie infinity?")
# -> Không hiệu quả

# Trích xuất các thực thể từ lời nhắc
entity_types = {
    "GAMES": "It is information about GameFi games, for example 'Axie Infinity', 'Befitter', 'Superpower Squad', 'Gods Unchained','Pegaxy','Gunstar Metaverse'",
    "TOPBACKERS": "It is information about the top backers of a game, for example 'Animoca Brands', 'Binance', 'Coinbase'",
    "COUNTSRATING": "It is information about the rating of a game, for example '4.5', '5.0'",
    "COMMUNITYPERFORMANCE": "It is information about the community performance of a game, for example 'active', 'inactive'", 
    "SOCIALSCORE": "It is information about the social score of a game, for example '100', '200'",
    "COUNTSLIKES": "It is information about the number of likes, dislikes of a game, for example '1000', '2000'",
    "TEAMPROFILE": "It is information about the team profile of a game as name , including the members, also known as staffs",
    "STAFFS": "It is information about the staffs of a game, have information as name, position, description",
    "TEAMPROFILELIKE": "Information about number of likes and dislikes of team profile"
}
relation_types = {
    "HAVE_TOP_BACKERS": "the game has top backers",
    "HAVE_TEAM": "the game has a team profile",
    "HAVE_NUMBER_RATES": "the game has parameters about number of rates",
    "HAVE_COMMUNITY_PERFORMANCE": "the game has parameters about community performance",
    "HAVE_SOCIAL_SCORE": "the game has parameters about social score", 
    "HAVE_NUMBER_LIKES": "the game has parameters about number of likes",
    "HAVE_TEAM_PROFILE_LIKES": "the team profile of the game has parameters about number of likes",
    "BELONGTO": "the staffs belong to the team profile"
 }
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
    If the input only gives the game name without providing anything else, the default information will be "about"
    If you cannot determine the game name, do not query the graph database.
    If there are no relevant entities in the user prompt, return an empty json object.
'''

client = OpenAI()

def define_query(prompt, model="gpt-3.5-turbo-0125"):
    completion = client.chat.completions.create(
        model=model,
        temperature=0,
        response_format= {
            "type": "json_object"
        },
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
        ]
    )
    return completion.choices[0].message.content
example_queries = [
    # "Introduce me to the top backers of Axie Infinity.",
    # "Can you tell me about the play mode of Axie Infinity?",
    # "Talk to me about the team profile of SUPERPOWER SQUAD.",
    # "Let me know about the rating star of Axie Infinity.",
    "Introduce to me the superpower squad game.",
]
    

# schema = """
#     This schema is about the information and relationship between the game and the entities.
#     The entities included below: {json.dumps(entity_types)}
#     The relationships included below: {json.dumps(relation_types)}
# """

# CYPHER_GENERATION_TEMPLATE = """You are an expert Neo4j Cypher translator who understands the question in english and convert to Cypher strictly based on the Neo4j Schema provided and following the instructions below:
# <instructions>
# * Use aliases to refer the node or relationship in the generated Cypher query
# * Do not use EXISTS, SIZE keywords in the cypher. Use alias when using the WITH keyword
# * Use only Nodes and relationships mentioned in the schema
# * Always enclose the Cypher output inside 3 backticks (```)
# * Always do a case-insensitive and fuzzy search for any properties related search. Eg: to search for a Company name use `toLower(c.name) contains 'neo4j'`
# * Cypher is NOT SQL. So, do not mix and match the syntaxes
# </instructions>

# Strictly use this Schema for Cypher generation:
# <schema>
# {schema}
# </schema>

# The samples below follow the instructions and the schema mentioned above. So, please follow the same when you generate the cypher:
# <samples>
# Human: Introduce the top backers of Axie Infinity?
# Assistant: ```MATCH (g:GAMES {name: 'axie-infinity'})-[:HAVE_TOP_BACKERS]->(t:TOPBACKERS) RETURN t```
# Human: Can you tell me about the play mode of Axie Infinity?
# Assistant: ```MATCH (g:GAMES {name: "axie-infinity"}) RETURN g.play_mode```
# Human: Talk to me about the team profile of SUPERPOWER SQUAD.
# Assistant: ```MATCH (g:GAMES {name: "superpower-squad"})-[:HAVE_TEAM]->(t:TEAMPROFILE)-[:HAVE_STAFF]->(s:STAFFS)
# RETURN t, s```
# </samples>
# Human: {question}
# Assistant: 
# """
s = """
Human: Introduce the top backers of Axie Infinity?
Assistant: ```MATCH (g:GAMES {name: 'axie-infinity'})-[:HAVE_TOP_BACKERS]->(t:TOPBACKERS) RETURN t```

Human: Can you tell me about the play mode of Axie Infinity?
Assistant: ```MATCH (g:GAMES {name: "axie-infinity"}) RETURN g.play_mode```



Human: Let me know about the rating star of Axie Infinity?.
Assistant: ```MATCH (g:GAMES {name: "axie-infinity"}) RETURN g.rating_star```

"""
CYPHER_GENERATION_TEMPLATE = """You are an expert Neo4j Cypher translator who understands the question in english and convert to Cypher strictly based on the Neo4j Schema provided and following the instructions below:
<instructions>
* Use aliases to refer the node or relationship in the generated Cypher query
* Use only Nodes and relationships mentioned in the schema
* Always enclose the Cypher output inside 3 backticks (```)
* Always do a case-insensitive and fuzzy search for any properties related search. Eg: to search for a Company name use `toLower(c.name) contains 'neo4j'`
* Cypher is NOT SQL. So, do not mix and match the syntaxes
</instructions>

Strictly use this Schema for Cypher generation:
<schema>
{schema}
</schema>

The samples below follow the instructions and the schema mentioned above. So, please follow the same when you generate the cypher:
<samples>
Human: Tell me about community performance of Pegaxy?
Assistant: ```MATCH (g:GAMES)-[:HAVE_COMMUNITY_PERFORMANCE]->(cp:COMMUNITYPERFORMANCE) WHERE toLower(g.name) CONTAINS 'pegaxy' RETURN cp ```

</samples>

Human: {question}
Assistant: 
"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=['schema','question'], validate_template=True, template=CYPHER_GENERATION_TEMPLATE
)
chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), graph=graph, verbose=True
)
message = """"Let's talk about the team profile of Gods Unchained."""
print(define_query(message))
# print(chain.get_prompts())
print(chain.run(define_query(message)))   