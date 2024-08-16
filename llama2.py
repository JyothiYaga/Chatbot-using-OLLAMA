from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama


def get_model_response(prompt):
    ollama = Ollama(model="Zenith")
    response = ollama(prompt)
    return response