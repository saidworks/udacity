import random
from words import *
noun = random.choice(nouns)
verb = random.choice(verbs)
template = random.choice(templates)
def silly_string(nouns, verbs, templates):
    # Choose a random template.


    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    #for index in range(len(template)):
    while index<len(template):
        if template[index:index+8]=="{{noun}}":
            output.append(noun)
            index+=8
        elif template[index:index+8]=="{{verb}}":
            output.append(verb)
            index+=8
        else:
            output.append(template[index])
            index+=1
    output=''.join(output)
    return output


    # Add a while loop here.

    # After the loop has finished, join the output and return it.

print(silly_string(noun,verb,template))