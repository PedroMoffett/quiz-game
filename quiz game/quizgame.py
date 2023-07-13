print("Welcome to my quiz game!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Is your girlfriend ever wrong? ")
if answer.lower() == 'no':
    print('Correct!')
    score +=1
else:
    print('Wrong!')

answer = input("Who won 'Succession'? ")
if answer.lower() == 'Tom':
    print('Correct')
    score += 1
else:
    print('Wrong!')

answer = input("What does 'PSU' stand for? ")
if answer.lower() == 'Power Supply Unit':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("Has Capitalism expired? ")
if answer.lower() == 'yes':
    print('Correct!')
    score +=1
else:
    print('Wrong!')

print("You got " + str(score) + "questions correct!")
print("You got " + str((score/4) * 100) + "%.")