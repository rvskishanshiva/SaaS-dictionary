from user_manager import add_user, display_users
from word_manager import search_word, add_word
from error_manager import log_error
from history_manager import log_history, show_history
from chatbot import chatbot_response
from analytics import top_searched_words
from input_logger import log_input

print("=== SaaS Dictionary Application (Excel Based) ===")

email = input("Email: ")
name = input("Name: ")
log_input(email, name)

if add_user(name, email):
    print("User registered.")
else:
    print("User already exists.")

while True:
    print("\n1. Search Word\n2. Add Word\n3. Show Search History\n4. Chatbot\n5. Top Searched word\n6. Users\n7. Exit\n")
    choice = input("Choice: ")
    log_input(email, choice)

    if choice == "1":
        w = input("Word: ")
        meaning = search_word(w)
        if meaning:
            print("Meaning:", meaning)
            log_history(email, w)
        else:
            print("Word not found.")
            log_error(email, w)

    elif choice == "2":
        add_word(input("Word: "), input("Meaning: "))
        print("Word added.")

    elif choice == "3":
        show_history(email)

    elif choice == "4":
        print(chatbot_response(input("Ask: ")))

    elif choice == "5":
        top_searched_words()

    elif choice == "6":
        display_users()

    elif choice == "7":
        break
