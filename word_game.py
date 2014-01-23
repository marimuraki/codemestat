
print "Enter a word to create a sentence. Enter ! or . to end it."
sentence = []
while True:
    word = raw_input("What's your word? ")
    if word != "!" and word != ".":
        print word
        sentence.append(word)
    else:
        print ' '.join(sentence) + word
        break
        
    