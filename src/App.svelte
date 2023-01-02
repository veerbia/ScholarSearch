<script>
  import axios from 'axios';
  import Paper from '@smui/paper';
  import { Input } from '@smui/textfield';
  import Fab from '@smui/fab';
  import { Icon } from '@smui/common';

  let question = '';
  let finalSummary = '';
  let citations = [];

  function sendRequest() {
    axios.post('http://127.0.0.1:5000/summarize', {
      question: question
    })
    .then(response => {
      finalSummary = response.data.final_summary;
      citations = response.data.citations;
    });
  }
</script>

<!-- <input type="text" bind:value={question} placeholder="Type your query here" style="vertical-align: top; padding: 20px;" />
<button on:click={sendRequest}>Summarize</button> -->

<h1>📖 ScholarSearch</h1>

<div class="solo-demo-container solo-container">
  <Paper class="solo-paper" elevation={6}>
    <Icon class="material-icons">search</Icon>
    <Input
      bind:value={question}
      placeholder="Seach"
      class="solo-input"
    />
  </Paper>
  <Fab
    on:click={sendRequest}
    disabled={question === ''}
    color="primary"
    mini
    class="solo-fab"
    >
    <Icon class="material-icons">arrow_forward</Icon>
  </Fab>
</div>


{#if finalSummary}
  <h2>Summary:</h2>
  <p>{finalSummary}</p>
  <h2>Sources:</h2>
  {#each citations as citation}
    <p><a href={citation.link}>{citation.link}</a></p>
    <p><strong>Citation Summary:</strong> {citation.summary}</p>
  {/each}
{/if}

<h3>FAQ</h3>
<details>
  <summary>What is ScholarSearch?</summary>
  <p>
    Got an paper due but don't know where to start your research? ScholarSearch is a tool that can help you find the most relevant information for your research paper. Just type in your question and ScholarSearch will find the most relevant information for you using Google Scholar and WebGPT by OpenAI.
  </p>
</details>
<details>
  <summary>How does ScholarSearch work?</summary>
  <p>
    ScholarSearch uses the Google Search API to find relevant webpages for a given query, and then uses OpenAI's language model to extract and summarize the most relevant information from those webpages. The summarized information is then used to construct a final answer to the query.
  </p>
</details>
<details>
  <summary>What does the output mean?</summary>
  <p>
    The output is a summary of the most relevant information found for your query. The summary is generated using OpenAI's WebGPT language model, which is trained on a large corpus of webpages. The summary is not guaranteed to be 100% accurate, but it should be a good starting point for your research. The summary is also accompanied by a list of relevant sources that you can use to find more information. As well as brief summaries of the content of each source.
  </p>
</details>
<style>
  .solo-demo-container {
    padding: 36px 18px;
    border: 1px solid
      var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
  }
 
  .solo-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  * :global(.solo-paper) {
    display: flex;
    align-items: center;
    flex-grow: 1;
    max-width: 600px;
    margin: 0 12px;
    padding: 0 12px;
    height: 50px;
    width: 500px;
  }
  * :global(.solo-paper > *) {
    display: inline-block;
    margin: 0 12px;
  }
  * :global(.solo-input) {
    flex-grow: 1;
    color: var(--mdc-theme-on-surface, #000);
  }
  * :global(.solo-input::placeholder) {
    color: var(--mdc-theme-on-surface, #000);
    opacity: 0.6;
  }
  * :global(.solo-fab) {
    flex-shrink: 0;
  }
</style>
