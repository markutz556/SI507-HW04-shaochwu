#!/usr/bin/env python3
question = str(input("What is your question?"))

import random
answer_list = ["It is certain","It is decidedly so", "Without a doubt",
				"Yes definitely, You may rely on it", "As I see it, yes",
				"Most likely", "Outlook good", "Yes", "Signs point to yes",
				"Reply hazy try again", "Ask again later", "Better not tell you now",
				"Cannot predict now", "Concentrate and ask again", "Don't count on it",
				"My reply is no", "My sources say no", "Outlook not so good",
				"Very doubtful"]
random_number = random.randint(0, 20)
answer = answer_list([random_number])

again = True
while again:
	if question.endswith("?"):
		print(answers_list[answers])
	elif question == "quit":
		again = False
	else:
		print("I'm sorry, I can only answer questions.")
