# ScholarSearch

ScholarSearch is a web application that helps you find the most relevant information for your research paper. Simply type in your question and ScholarSearch will use the Google Search API to find relevant webpages and then use OpenAI's language model to extract and summarize the most relevant information from those webpages. The summarized information is then used to construct a final answer to the query.

## How to use ScholarSearch
Type your question into the search bar.
Press the Enter key or click the search icon to send your request.
ScholarSearch will return a summary of the most relevant information and a list of relevant sources with brief summaries of their content.

## Technical Details
ScholarSearch is a web application built using the Svelte framework and a Flask backend server. The frontend of the application is responsible for displaying the user interface and handling user input, while the backend server is responsible for making API calls to Google Scholar and OpenAI to retrieve and summarize information.

To set up ScholarSearch on your local machine, you will need to install the following dependencies:

- Node.js
- npm (comes with Node.js)
- Python 3
- Flask
- axios
- serpapi 
- openai

To install these dependencies, follow the instructions below:

1. Download and install Node.js from the official website. This will also install npm, which is the package manager for Node.js.
2. Download and install Python 3 from the official website.
3. Open a terminal and run the following command to install Flask: `pip install flask google-search-results openai dotenv` .
4. In the same terminal, run the following command to install axios: `npm install`.

Once you have all the dependencies installed, you can set up the ScholarSearch application by following these steps:

1. Clone the ScholarSearch repository to your local machine.
2. Navigate to the root directory of the repository in your terminal.
3. Run the following command to start the Flask server: python app.py.
4. In a new terminal window, navigate to the public directory within the repository.
5. Run the following command to start the Svelte application: npm run dev.

The Svelte application will now be running on your local machine, and you can access it by visiting http://localhost:5000 in your web browser.

I chose to use Svelte for the frontend of ScholarSearch because it is a lightweight and easy-to-use framework for building web applications. Svelte allows us to build interactive user interfaces with minimal code, and it is also very fast, which is important for providing a good user experience. I chose to use Flask for the backend of ScholarSearch because it is a lightweight and easy-to-use framework for building web applications in Python. Flask allowed for the set up of a backend server quickly and easily, and it also has good support for making HTTP requests to external APIs.

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