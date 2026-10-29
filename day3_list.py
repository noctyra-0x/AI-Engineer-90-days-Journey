# ============DAY 3 LIST MANIPULATION AND SLICING===========

ai_topics=["Python", "Variables", "Loops", "Math", "Rag"]
print("Original topic list:", ai_topics)
print("Total Topics:", len(ai_topics))
top_three= ai_topics[0:3]
print("\nTop three topics:",top_three)
ai_topics.remove("Rag")
print("After removing 'rag':", ai_topics)
last_topic=ai_topics.pop()
print(f"Popped topic:", {last_topic})
print("Final topic list:", ai_topics)