from db_manager import DatabaseManager
from openai_helper import OpenAiHelper

def process_user_queries(output_file, questions, ai_helper: OpenAiHelper, db_manager: DatabaseManager, section_title, query_strategy):
    output_file.write(f'# {section_title}\n\n')
    for idx, question in enumerate(questions):
        sql_query = query_strategy(question)
        db_result = db_manager.execute_query(sql_query)
        response = ai_helper.generate_friendly_response(question, db_result)
        output_file.write(f'Question {idx + 1}\n')
        output_file.write(f'* Prompt: {question}\n')
        output_file.write(f'* SQL Query: \n```sql\n{sql_query}\n```\n')
        output_file.write(f'* Database Result: \n```text\n{str(db_result)}\n```\n')
        output_file.write(f'* AI Friendly Response: {response}\n\n')
        output_file.write('---\n')

def main():
    db_manager = DatabaseManager()
    ai_helper = OpenAiHelper()

    questions = [
        "How much revenue has been generated?",
        "Which customer placed the most orders?",
        "Which is the most ordered dish?",
        "Who spent the most overall?",
        "What was the most recent order?",
        "Which dish has the highest price?"
    ]

    with open('output_queries.md', 'w') as output_file:
        output_file.write('# Restaurant Database Queries\n\n')

        process_user_queries(output_file, questions, ai_helper, db_manager, 'No Context Queries', ai_helper.zero_shot_query)
        process_user_queries(output_file, questions, ai_helper, db_manager, 'Informed Queries', ai_helper.contextual_query)

if __name__ == '__main__':
    main()
