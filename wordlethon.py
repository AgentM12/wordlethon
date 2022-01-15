import random
import colorama

LANG_CODE = 'en'
ROUNDS = 6
RECYCLE_WORDS = False

def init():
	colorama.init(autoreset=False)
	print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.WHITE, end='')

	letters = 0
	while letters < 5 or letters > 10:
		letters = input('How many letters do you want to play with? (5-10): ')
		try: letters = int(letters)
		except: letters = 0

	dictionary_location = f"dictionary_{LANG_CODE}_{letters}_test.txt"
	words_location = dictionary_location #f"words_{LANG_CODE}_{letters}_test.txt"

	words = get_words(words_location)
	dictionary = get_dictionary(dictionary_location)
	return words, dictionary, letters

def check_correct(guessed_word, word_to_guess, i):
	return guessed_word[i] == word_to_guess[i]

def check_semicorrect(guessed_word, remaining_correct_letters, i):
	return guessed_word[i] in remaining_correct_letters

def play():
	words, dictionary, letters = init()
	
	checks = [check_correct, check_semicorrect]

	play_words = list(words)
	while len(play_words) > 0:
		word_to_guess = random.sample(play_words, 1)[0]
		if not RECYCLE_WORDS:
			play_words.remove(word_to_guess)

		board = []
		for r in range(ROUNDS):
			board.append(f'{r+1}: ' + colorama.Back.WHITE + '   ' * letters + colorama.Back.BLACK)

		game_round = 0
		print(f"\n === Guess this {letters} letter word === \n")
		[print(line) for line in board]
		while game_round < ROUNDS:
			game_round += 1
			guessed_word = input(f"\n === Guess {game_round} === \n").lower()
			while len(guessed_word) != letters or (guessed_word not in dictionary):
				if len(guessed_word) < letters:
					print(f"{guessed_word} is not a valid word (too short). Try again!")
				elif len(guessed_word) > letters:
					print(f"{guessed_word} is not a valid word (too long). Try again!")
				else:
					print(f"{guessed_word} is not a valid word. Try again!")

				[print(line) for line in board]
				guessed_word = input(f"\n === Guess {game_round} === \n").lower()
			
			# Prioritize correct letters before semi correct letters by checking them in order.
			remaining_correct_letters = list(word_to_guess)
			check_priority = [2] * letters
			for t in range(len(checks)):
				for i in range(letters):
					if check_priority[i] == 2 and checks[t](guessed_word, word_to_guess if t == 0 else remaining_correct_letters, i):
						check_priority[i] = t
						remaining_correct_letters.remove(guessed_word[i])

			# Construct the guess-coloring based on the prioritized checked guess.
			colored_word = ""
			correct_letters = 0
			for i in range(letters):
				let = guessed_word[i]
				if check_priority[i] == 0: # GREEN
					colored_char = colorama.Back.GREEN
					correct_letters += 1
				elif check_priority[i] == 1: # YELLOW
					colored_char = colorama.Back.YELLOW
				else: # GRAY
					colored_char = colorama.Back.RED
				
				colored_char += f" {let} "
				colored_word += colored_char

			colored_word += colorama.Back.BLACK
			board[game_round - 1] = f'{game_round}: ' + colored_word
			[print(line) for line in board]
			if (correct_letters == letters):
				break
		if (correct_letters == letters):
			print(f"Congratulations! You guessed the word in {game_round} guess{'es' if game_round != 1 else ''}.")
		else:
			print(f"Too bad. The word was: {word_to_guess}")
		if (input("\nPlay another game? (y/n): ").lower().startswith('n')):
			break


def get_dictionary(dictionary_location):
	with open(dictionary_location, 'r') as f:
		return [line.strip() for line in f]

def get_words(words_location):
	with open(words_location, 'r') as f:
		return [line.strip() for line in f]

def main():
	play()


if __name__ == '__main__':
	main()