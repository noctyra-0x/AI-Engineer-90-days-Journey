def format_prompt(user_question, context="General Python"):
    clean_prompt=f"[Context: {context},\n Question: {user_question.strip()}]"
    return clean_prompt
def estimate_token_count(text):
    word_count=len(text.split())
    estimate_tokens= int(word_count *1.33)
    return word_count, estimate_tokens
print("===AI PROMPT HELPER===")
question=input("Enter u'r question: ")
prompt=format_prompt(question, context="AI Engineering Day-5 ")
words, tokens=estimate_token_count(prompt)
print("===Processing Prompt===")
print(prompt)
print("--------------")
print(f"Stats: {words} words | {tokens} tokens estimated")