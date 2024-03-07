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

client = OpenAI()

entity_types = {
    "GAMES": "It is information about GameFi games, for example 'Axie Infinity', 'Befitter', 'Superpower Squad', 'Gods Unchained','Pegaxy','Gunstar Metaverse, include information as about, play mode, play to earn model,...'",
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
    "HAVE_STAFF": "the team profile of the game has staffs",
 }

