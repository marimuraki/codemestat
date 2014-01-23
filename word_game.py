
print "Enter a word to create a sentence. Enter ! or . to end it."

while True:
    x_new = raw_input("What's your word? ")
    if x_new != "!" and x_new != ".":
        print x_new
    else:
        break
        
    