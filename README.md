# 🔎 GPT Researcher
This is a fork from https://github.com/assafelovic/gpt-researcher with some modifications to make it work with
local [Ollama](https://ollama.com/library) models.

## How to use

1. Clone this repository
2. Install the requirements
3. Copy the .env.example file to .env and fill in the fields accordingly
   - Make sure to have the Ollama model already downloaded with ollama server running
4. Modify the `query` variable in the `main.py` file with the prompt you want to use for your research
5. Run the `main.py` file