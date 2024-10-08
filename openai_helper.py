from openai import OpenAI
import config

class OpenAiHelper:
    BASE_PROMPT = ("Generate a valid SQL query for the following restaurant-related question. "
                   "Do not include explanations, just return the SQL statement.")
    
    _helper_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._helper_instance:
            cls._helper_instance = super(OpenAiHelper, cls).__new__(cls)
        return cls._helper_instance

    def __init__(self):
        if not hasattr(self, 'client'):
            self.client = OpenAI(api_key=config.OPENAI_API_KEY)

    def create_query(self, messages, max_tokens=150, temperature=0):
        response = self.client.chat.create(
            model="gpt-4",
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content

    def formulate_response(self, prompt, chat_history=None, max_tokens=150, temperature=0):
        initial_setup = ""
        with open('sql/setup.sql', 'r') as file:
            initial_setup = file.read()

        messages = [{"role": "system", "content": initial_setup}, {"role": "system", "content": self.BASE_PROMPT}]
        if chat_history:
            for pair in chat_history:
                messages.append({"role": "user", "content": pair[0]})
                messages.append({"role": "assistant", "content": pair[1]})
        messages.append({"role": "user", "content": prompt})

        return self.create_query(messages, max_tokens, temperature)

    def generate_friendly_response(self, question, db_output):
        prompt = f"The question: '{question}' was answered by the database: {db_output}. Provide the answer only, no extra explanation."
        messages = [{"role": "user", "content": prompt}]
        return self.create_query(messages, 50, 0.6)

    def zero_shot_query(self, question):
        return self.formulate_response(question)

    def contextual_query(self, question):
        example_pairs = [("Which dish is the most expensive?", 
                          "SELECT Name FROM Dish ORDER BY Price DESC LIMIT 1;")]
        return self.formulate_response(question, example_pairs)
