from openai import OpenAI
from api_keys.api_keys import openai_api_key
from prompt.prompt import prompt_consulta
from helpers.helpers import formatear_conversacion, formatear_historial_conversaciones, formatear_horarios_disponibles
import pytz
from datetime import datetime

class OpenAIManager:
    def __init__(self):
        self.client = OpenAI(api_key=openai_api_key)

    def consulta(self, cliente,conversation_actual, conversation_history):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt_consulta(cliente) + formatear_conversacion(conversation_actual)},
            ],
            max_tokens=250,
        )
        return response.choices[0].message.content.strip()
