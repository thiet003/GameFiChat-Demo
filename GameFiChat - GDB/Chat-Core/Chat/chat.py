import logging
import os
import sys
from typing import Any, Dict, Generator, List, Union
import openai
from openai import OpenAI
import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage
from chromadb.config import Settings
from py2neo import Graph, Node, Relationship


def load_index() -> Any:
    """Load the index from the storage directory."""
    print("Loading index...")

    chroma_client = chromadb.PersistentClient(path="store", settings=Settings(
        anonymized_telemetry=False
    ))
    chroma_collection = chroma_client.get_or_create_collection("gamefi")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store,persist_dir="store/res" ) 
    # load the index
    cur_index = VectorStoreIndex([], storage_context=storage_context)
    retriever = cur_index.as_retriever()
    print("Done.")
    return retriever
    print(response)

def build(question) -> None:
    retriever = load_index()
    extract_res = retriever.retrieve(question)
    return extract_res