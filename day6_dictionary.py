ai_req={
    "model": "gpt-4o",
    "prompt": "Explain vector database simply",
    "temperature": "0.5",
    "tags": ["education", "python", "ai"]
}
print("===AI REQUEST METADATA CONFI===")
print(f"Target_model: {ai_req.get('model')}")
print(f"Creativity_level(temp): {ai_req.get('temperature')}")
try:
    new_temp=float(input("\n Enter new temperature value (0 to 1.0): "))
    ai_req["temperature"]=new_temp
    print("\n New temp value added successfully")
except ValueError:
    print("Invalid value, keeping default value")
print("\n ===Final request metadata obj===")
for key, value in ai_req.items():
    print(f"{key.upper()}: {value}")