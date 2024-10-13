def suggest_completions(search_history, query):
    suggestions = []
    for word in search_history:
        if word.startswith(query.lower()):
            suggestions.append(word)        
    return suggestions

search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

query = input("Enter your partial search query: ").strip().lower()
suggestions = suggest_completions(search_history, query)
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
