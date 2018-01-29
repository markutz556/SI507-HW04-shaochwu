#!/usr/bin/env python3
question = str(input("What is your question?"))
while again:
	if question.endswith("?"):
		print(answers_list[answers])
	elif question == "quit":
		again = False
	else:
		print("I'm sorry, I can only answer questions.")
