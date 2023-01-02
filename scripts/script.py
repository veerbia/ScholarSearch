from serpapi import GoogleSearch
from dotenv import load_dotenv
import requests
import openai
import logging
import sys, os
from flask import Flask, request
from flask_cors import CORS
import json

load_dotenv()
app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("openai_api_key")
browserless_api_key = os.environ.get("browserless_api_key")
headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
params = {'token': browserless_api_key}

def scarpe_webpage(link):
    json_data = {
        'url': link,
        'elements': [{'selector': 'body'}],
    }
    response = requests.post('https://chrome.browserless.io/scrape', params=params, headers=headers, json=json_data)
    webpage_text = response.json()['data'][0]['results'][0]['text']
    return webpage_text

def summarize_webpage(question, webpage_text):
  prompt = """You are an intelligent summarization engine. Extract and summarize the
  most relevant information from a body of text related to a question.

  Question: {}

  Body of text to extract and summarize information from:
  {}

  Relevant information:""".format(question, webpage_text[0:2500])
  completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.8, max_tokens=800)

  return completion.choices[0].text

def summarize_final_answer(question, summaries):
    prompt = """You are an intelligent summarization engine. Extract and summarize relevant information
    from the four points below to construct an answer to a question.

    Question: {}

    Relevant Information:
    1. {}
    2. {}
    3. {}
    4. {}""".format(question, summaries[0], summaries[1], summaries[2], summaries[3])
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.8, max_tokens=800)

    return completion.choices[0].text

def get_link(r):
    return r['link']

def get_search_results(question):
    serpapi_api_key = os.environ.get("serpapi_api_key")
    search = GoogleSearch({
        "q": question, 
        "api_key": serpapi_api_key,
        "logging": False,
        "engine": "google_scholar"
    })

    result = search.get_dict()
    return list(map(get_link, result['organic_results']))

def print_citations(links, summaries):
    result = []
    i = 0
    while i < 4:
        result.append({"link": links[i], "summary": summaries[i]})
        i += 1
    return result

@app.route('/summarize', methods=['POST'])
def summarize():
    content = request.get_json()
    question = content['question']
    sys.stdout = open(os.devnull, 'w') #disable print
    links = get_search_results(question)
    sys.stdout = sys.__stdout__ #enable print
    webpages = list(map(scarpe_webpage, links[:4]))
    summaries = []
    for x in webpages:
        summaries.append(summarize_webpage(question, x))
    final_summary = summarize_final_answer(question, summaries)
    result = print_citations(links, summaries)
    return json.dumps({'final_summary': final_summary, 'citations': result})

if __name__ == "__main__":
    app.run()

