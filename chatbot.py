
import json
import difflib
import re

# Load FAQs from the JSON file
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


def clean_text(text):
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def get_answer(user_question):
    """Find the closest matching FAQ."""
    question = clean_text(user_question)
    
    if question in ["hello", "hi", "hey", "hii", "good morning", "good evening"]:
        return "Hello! 👋 Welcome to RailBot AI! Ask me anything about railway inspection, crack detection, sensors, or robot safety."


    if not question:
        return "Please enter a question."

    best_match = None
    best_score = 0

    for faq in faqs:
        faq_question = clean_text(faq["question"])

        score = difflib.SequenceMatcher(
            None, question, faq_question
        ).ratio()

        if score > best_score:
            best_score = score
            best_match = faq

    if best_score >= 0.45:
        return best_match["answer"]

    return (
        "Sorry, I could not find a suitable answer. "
        "Please try asking about railway inspection robots."
    )


if __name__ == "__main__":
    print("===================================")
    print("   Railway Inspection FAQ Chatbot")
    print("===================================")
    print("Ask me questions about railway inspection!")
    print("Type 'exit' to close the chatbot.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye! Happy learning!")
            break

        answer = get_answer(user_input)
        print("Chatbot:", answer, "\n")
