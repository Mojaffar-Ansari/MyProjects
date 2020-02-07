from sys import argv
script,user_name=argv
promt='>'
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you few questions.")
print(f"Do you like me {user_name} ?")
likes=input(promt)
print(f"Where do you live {user_name}")
lives=input(promt)
print(f"What kind of computer do you have?")
computer=input(promt)
print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where thar is.
And you have a {computer} computer. Nice
''')
