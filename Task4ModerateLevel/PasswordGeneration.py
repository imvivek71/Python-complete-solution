"""""
Password Generation for below specs
*must contains 8 letters
*One upper case & One lower case
*At least one special character
*One numeric

"""

import string
from random import *
characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation  + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))
print(password)
