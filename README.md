# ScholarSearch

ScholarSearch is a web application that helps you find the most relevant information for your research paper. Simply type in your question and ScholarSearch will use the Google Search API to find relevant webpages and then use OpenAI's language model to extract and summarize the most relevant information from those webpages. The summarized information is then used to construct a final answer to the query.

![Screenshot 2023-01-01 at 6 36 36 PM](https://user-images.githubusercontent.com/102765426/210194754-90e72e0d-de8e-47ed-b056-cd847b31fc28.png)
![Screenshot 2023-01-01 at 6 40 14 PM](https://user-images.githubusercontent.com/102765426/210194798-9daecc84-abb4-43f4-80e1-98ebe66e2654.png)


## How to use ScholarSearch
Type your question into the search bar.
Press the Enter key or click the search icon to send your request.
ScholarSearch will return a summary of the most relevant information and a list of relevant sources with brief summaries of their content.

## Technical Details
ScholarSearch is a web application built using the Svelte framework and a Flask backend server. The frontend of the application is responsible for displaying the user interface and handling user input, while the backend server is responsible for making API calls to Google Scholar and OpenAI to retrieve and summarize information.

To set up the application, you will need to install the necessary dependencies and configure the API keys. First, you will need to install Node.js, which is required to run the Svelte application. You can download the latest version of Node.js from the official website (https://nodejs.org/). Once Node.js is installed, you can install the Svelte CLI by running the following command:
```
npm install -g svelte-cli
```
Next, you will need to install the necessary Python dependencies for the Flask server. You will need to have Python 3 installed on your system. You can check if you already have Python installed by running the following command:
```
python --version
```
If Python is not installed, you can download the latest version from the official website (https://www.python.org/). Once Python is installed, you can create a virtual environment and install the necessary dependencies by running the following commands:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Finally, you will need to obtain API keys for the Google Search API, OpenAI API and the browserless API. You can sign up for these services on their respective websites and obtain your API keys. Once you have your keys, you will need to create a file called .env in the root directory of the project, and add the following lines, replacing YOUR_API_KEY with your actual API key:
```
openai_api_key = 'YOUR_API_KEY'
browserless_api_key = 'YOUR_API_KEY'
serpapi_api_key = 'YOUR_API_KEY'
```
With the dependencies installed and the API keys configured, you can start the application by running the following commands:
```
cd ScholarSearch
npm install
npm run build
cd ..
flask run
```
This will start the Svelte application and the Flask server, allowing you to access the application in your web browser at http://localhost:5173.

Svelte was chosen for the frontend of ScholarSearch because it is a lightweight and easy-to-use framework for building web applications. Svelte allows us to build interactive user interfaces with minimal code, and it is also very fast, which is important for providing a good user experience. I chose to use Flask for the backend of ScholarSearch because it is a lightweight and easy-to-use framework for building web applications in Python. Flask allowed for the set up of a backend server quickly and easily, and it also has good support for making HTTP requests to external APIs.

I chose to use the Google Search API to find relevant webpages for a given query because it is a reliable and well-documented API that provides access to the vast resources of the Google search engine. The Google Search API allowed for search in webpages that are relevant to a given query, and it returns the results in a structured format that is easy to work with. I chose to use the OpenAI API to extract and summarize information from webpages because it is a powerful and state-of-the-art language model that has been trained on a large corpus of webpages. The OpenAI API allowed me to extract and summarize information from webpages quickly and as accurately as possible, and it returns the results in a structured format that is easy to work with.

## A Note on WebGPT
OpenAI's [WebGPT paper](https://openai.com/blog/webgpt/) describes a language model called WebGPT that is trained on a large corpus of webpages and is able to generate human-like text. The paper explains how the model was trained using a variant of the Transformer architecture, and how it was able to achieve state-of-the-art results on a variety of language generation tasks.

In ScholarSearch, we use the OpenAI API to access the WebGPT language model and use it to extract and summarize information from webpages. The API allows us to send a webpage to the model and receive a summary of the most relevant information in the page. This summary is then used to construct a final answer to the user's query.

One of the key benefits of using the WebGPT language model in ScholarSearch is that it is able to generate coherent and human-like text, which makes it easier for users to understand the information that is being presented to them. Additionally, because the model is trained on a large corpus of webpages, it is able to understand the structure and content of webpages in a way that is similar to a human reader. This allows it to identify and extract the most relevant information from a webpage, which is important for providing users with the information they are looking for.


## FAQ

### What is ScholarSearch?

ScholarSearch is a tool that helps you find the most relevant information for your research paper. It uses the Google Search API to find relevant webpages and then uses OpenAI's language model to extract and summarize the most relevant information from those webpages.

### How does ScholarSearch work?

ScholarSearch uses the Google Search API to find relevant webpages for a given query, and then uses OpenAI's language model to extract and summarize the most relevant information from those webpages. The summarized information is then used to construct a final answer to the query.

### What does the output mean?

The output is a summary of the most relevant information found for your query. The summary is generated using OpenAI's WebGPT language model, which is trained on a large corpus of webpages. The summary is not guaranteed to be 100% accurate, but it should be a good starting point for your research. The summary is also accompanied by a list of relevant sources that you can use to find more information, as well as brief summaries of the content of each source.

#### References:
- Inspired by the original WebGPT search scraping script from [rahul](https://github.com/asaprahul)
- OpenAI WebGPT Paper (https://openai.com/blog/webgpt/)
