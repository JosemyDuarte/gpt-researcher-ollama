# 🔎 GPT Researcher
This is a fork from https://github.com/assafelovic/gpt-researcher with some modifications to make it work with
local [Ollama](https://ollama.com/library) models.

## How to use

1. Clone this repository
2. Install the requirements
3. Copy the .env.example file to .env and fill in the fields accordingly
   - Make sure to have the Ollama model already downloaded with ollama server running
   - The example is using `mixtral:8x7b-instruct-v0.1-q6_K`
4. For embbedings I'm using [llama3](https://ollama.com/library/llama3), so unless you change `gpt_researcher/memory/embeddings.py` to use something else you will need to run:
    ```bash
    ollama pull llama3
    ```
5. Modify the `query` variable in the `main.py` file with the prompt you want to use for your research
6. Run the `main.py` file