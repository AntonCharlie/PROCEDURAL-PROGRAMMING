
def get_questions():
	
	return [
		["What color is the daytime sky on a clear day? ", "blue"], # [0][0], [0][1]
		["What is the answer to life, the universe and everything? ", "42"], # [1][0], [1][1]
		["What is a three letter word for mouse trap? ", "cat"],	#[2][0], [2][1]
		["What is the color of snow?", "white"],
		["What do we eat everyday?", "rice"],
		["Who is the president of Indonesia?", "joko widodo"],
		["Two plus three equals to", "five"],
		["Thing that we use to sit is", "chair"],
		["What do we use to protect our body?", "clothes"],
		["Where is the place to take a bath?", "bathroom"]
	]

def check_questions(row):
	q = row[0]
	a = row[1]

	user_ans = input(q)
	if a == user_ans:
		print("Correct!")
		return True
	else:
		print("Incorrect")
		return False

def run(questions):
	if len(questions) == 0:
		print("No questions were given")
	else:
		index = 0
		right = 0

		while index < len(questions):
			
			# print(questions[index])

			if check_questions(questions[index]):
				right += 1

			index += 1 
		print(f"Your score is {right/len(questions) * 100}")

run(get_questions())