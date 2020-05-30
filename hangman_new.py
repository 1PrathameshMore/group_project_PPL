import random
#import random library to get a random number corresponding to a word

line_number = random.randint(0, 365)
#get the random number

picked_word = "" #string defined to store the word selected

from words import word_list
#wordlist imported

#Hangman Game Graphics
stages = [  #extra try
                """
                   --------
                   |      |
                   |    DEAD
                   |
                   |      
                   |     
                   -
                """,
                
                #head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   
                   BONUS LAST TRY 
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    
for i, line in enumerate(word_list):
    #word corresponding to the random number is picked    
    if i == line_number:
        picked_word = line.upper() #picked word is captilasied for uniformity
        break

picked_word
user_word = '_' * (len(picked_word)) #create the word to store guessed by user of same lenght as picked word

length = len(picked_word) #no of unguessed words displayed
game_over = False
tries = 7
guessed_word = '' 
# to store all the words guessed so that you don't waste your tries 
guessed_letter = ''
#to store the letters that are guessed
print("Let's play Hangman!")
print(stages[tries])
print(user_word)
print(f"Number of letters unguessed {length}")
print("\n")

while not game_over and tries > 0:
    
    guess = input("Please guess a letter or word: ").upper()
    
    if len(guess) == 1 and guess.isalpha():
        #check whether entered character is a single alphabet
        
        if guess in guessed_letter:
            #repeated letter
            print(f"You already guessed the letter {guess}.")
         
        elif guess not in picked_word:
            #wrong guess
            print(f"{guess} not in the word.")
            tries = tries - 1
            guessed_letter += guess
            
        else:
            #correct guess
            print(f"Good Job! {guess} is in the word.")
            guessed_letter += guess
            #added to guessed letters

            word_as_list = list(user_word)
            #Initial word with blanks is converted to list to place the guessed words at correct point
            indices = [i for i, letter in enumerate(picked_word) if letter == guess]
            #list of indices in the picked word string where guessed word is present
            length = length - len(indices)
            #number of letters not guessed is recalculated
            for index in indices:
                #replace the letters
                word_as_list[index] = guess
            user_word = "".join(word_as_list)
            #list is converted back to string and stored in user_word
            
            if "_" not in user_word:
                #when there is no blank in the guessed word
                game_over = True
                
    elif len(guess) == len(picked_word) and guess.isalpha():
        #when word of length equal to word to be guessed is eneterd
        if guess in guessed_word:
            #already guessed word
            print(f"You already guessed the word {guess}.")
            
        elif guess != picked_word:
            #when wrong word is guessed
            print(f"{guess} is not the word.")
            tries = tries - 1
            guessed_word += guess
            
        else:
            #when corret word is guessed
            game_over = True
            user_word = guess
            
    else:
        #when the entered character is not a alphabet or
        #when the entered word is not of same length as the word to be guessed or
        #when the entered word contains non-alphabetic character/s
        print(f"{guess} is out of bound guess")
        
    print(stages[tries])
    #print the number of tries remaining in form of hangman stage
    print(user_word)
    #print the word containing all the correct guesses made till that point
    print(f"Number of letters unguessed:- {length}")
    print("\n")
    
if game_over:
    #game_over is true when the word is correctly guessed
    print(f"COngratulations!!!!!You Guessed The Word!!!!!! You Win\n")
else:
    #all the tries are used and unable to guess the word
    print(f"Sorry!You ran out of tries.{picked_word} was the word. Better luck next time!!")

  
