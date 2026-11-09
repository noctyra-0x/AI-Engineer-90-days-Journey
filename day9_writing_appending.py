log_file_path= "ai_response_log.txt"
with open(log_file_path, "w") as f:
    f.write("===AI conversion Log===\n")
    f.write(" Session: Initialized Session\n")

user_prompt=input("Enter the test prompt for the AI: ")
ai_response=f" Simulated AI response to {user_prompt}"
with open(log_file_path, "a") as f:
    f.write(f"User: {user_prompt}\n")
    f.write(f"AI: {ai_response}\n")
print("\n New conversion entry append successfully")
print("-----Current file content on disk-----")
with open(log_file_path, "r") as f:
    print(f.read())
