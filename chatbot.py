def chatbot_response(query):
    responses = {
        "help": "Search words, add words, view history or analytics.",
        "search words": "Choose option 1 to search a word.",
        "add words": "Choose option 2 to add a new word.",
        "view history" : "Choose option 3 to add a new word.",
        "analytics" :"Choose option 5 to add a new word."
    }
    return responses.get(query.lower(), "Please try another query.")
