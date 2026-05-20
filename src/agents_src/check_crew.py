from pprint import pprint

from agents_src.crew import qa_crew

input_data={
    "user_query":"Explain about electric fields for dipole",
    "chat_history":{}
}

result=qa_crew.kickoff(input_data)

result_dict=result.to_dict()

pprint(result_dict)