import random # imports the random module
import string # imports the string module

print('Hello!, Welcome to Password generator!') # prints introduction statement

length = int(input('\nEnter the length of password: ')) # input of the user, converts it into a integer after user input

lowercase = string.ascii_lowercase # the lowercase letters
uppercase = string.ascii_uppercase # the UPPERCASE
numbers = string.digits # the numbers
characters = string.punctuation # the characters

all = lowercase + uppercase + numbers + characters # combines all the randomly chosen password into 1 variable

almost_password = random.sample(all,length) # generating the password
password = "".join(almost_password) # the password

all = string.ascii_letters + string.digits + string.punctuation  # just to clear up storage
password = "".join(random.sample(all,length))

print(password) # prints the password
