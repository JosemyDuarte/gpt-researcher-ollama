import os

from colorama import Fore, Style
from langchain_community.llms.ollama import Ollama


class OllamaProvider:

    def __init__(
            self,
            model,
            temperature,
            max_tokens
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.base_url = self.get_base_url()
        self.llm = self.get_llm_model()

    def get_base_url(self):
        """
        Gets the base url
        Returns:

        """
        try:
            base_url = os.environ["LLM_BASE_URL"]
        except:
            raise Exception(
                "Ollama base url not found. Please set the OLLAMA_BASE_URL environment variable.")
        return base_url

    def get_llm_model(self):
        # Initializing the chat model
        llm = Ollama(
            base_url=self.base_url,
            model=self.model,
            temperature=self.temperature,
            num_predict=self.max_tokens,
        )

        return llm

    async def get_chat_response(self, messages, stream, websocket=None):
        if not stream:
            # Getting output from the model chain using ainvoke for asynchronous invoking
            output = await self.llm.ainvoke(messages)

            return output

        else:
            return await self.stream_response(messages, websocket)

    async def stream_response(self, messages, websocket=None):
        paragraph = ""
        response = ""

        # Streaming the response using the chain astream method from langchain
        async for chunk in self.llm.astream(messages):
            content = chunk
            if content is not None:
                response += content
                paragraph += content
                if "\n" in paragraph:
                    if websocket is not None:
                        await websocket.send_json({"type": "report", "output": paragraph})
                    else:
                        print(f"{Fore.GREEN}{paragraph}{Style.RESET_ALL}")
                    paragraph = ""

        return response
