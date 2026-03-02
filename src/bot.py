import builtins

def restricted_exec(code):
    FORBIDDEN = ["import", "os", "sys", "subprocess", "open", "__"]

    for word in FORBIDDEN:
        if word in code:
            raise ValueError(f"{word} is not allowed.")

    local_vars = {}
    builtins.exec(code, ALLOWED_GLOBALS, local_vars)
    return local_vars

    # bot_fixed.py
import pydoc
from pyexpat.errors import messages
import requests
import os

api_key = os.getenv("GroqAPI")
endpoint = "https://api.groq.com/openai/v1/chat/completions"
data= r'C:\Users\acer\Downloads\heart.csv'


# module-level globals (contract expects these)
conversation_history = []
project_context = []
summary_memory = ''

class Bot:
    def __init__(self, api_key, endpoint, dataset_path, system_context= word_file_string):
        self.api_key = api_key
        self.endpoint = endpoint
        self.dataset_path = dataset_path
        self.system_context = system_context
    def build_context(self):
        context= [
        {"role": "system", "content": self.system_context},
        {
            "role": "system",
            "content": f"Project Context:\n{globals().get('project_context')}"
        },
        {
            "role": "system",
            "content": f"Summary Memory:\n{globals().get('summary_memory')}"
        },
            ] + globals().get("conversation_history")
        return context
        
    
    
    def send_message(self, message, max_tokens=1500, temperature=0.2):

        conversation_history.append({"role": "user", "content": message})

        avanish = self.build_context()
        print(avanish)

        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": avanish,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)
        print("API response status:", response.status_code)

        if response.status_code == 200:
            response_data = response.json()
            bot_reply = response_data['choices'][0]['message']['content']

            # append assistant reply to conversation history
            conversation_history.append({"role": "assistant", "content": bot_reply})

            # try to extract & execute code block from bot reply
            self.execute_code_with_delimiters(bot_reply)

        else:
            return {"error": f"Error: {response.status_code} - {response.text}"}

    def execute_code_with_delimiters(self, text):
        """
        Extract the first fenced ```python``` block from `text`, execute it in module globals,
        and return a dict describing the result.
        """
        try:
            start_marker = "```python"
            end_marker = "```"

            start_index = text.find(start_marker)
            if start_index == -1:
                return {"status": "no_code_block_found"}

            start_index += len(start_marker)
            end_index = text.find(end_marker, start_index)
            if end_index == -1:
                return {"status": "no_closing_fence"}

            code_str = text[start_index:end_index].strip()

            # Execute in module globals so the executed code can update project_context/summary_memory
            exec(code_str, globals())

            return {"status": "executed", "code": code_str}
        except Exception as e:
            # return the error (do not recursively call send_message)
            return {"status": "error", "error": str(e)}


from docx import Document

file_path = r"C:\Users\acer\Downloads\bot_code_instructions.docx"  # apna actual path daal dena

doc = Document(file_path)

print(word_file_string)

