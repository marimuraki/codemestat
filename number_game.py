
x = 0
max_tries = 10
count = 0

print "The game begins! Enter an integer ... if it's > or <, I'll tell you and if not, I'll quit (I'll give you 10 trys!)."

try:
    while True:
        x_new = int(raw_input("What's your number? "))
        if count == 0:
            print "Your first number!"
        else:
            if x_new > x:
                print " -> it's bigger than the last!"
            elif x_new < x:
                print " ->  it's smaller than the last!"
            else:
                print " -> no change! I'll exit now."
                break
            
        x = x_new
        count += 1
        if count > max_tries:
            print "too many tries ..."
            break
except ValueError:
    print "Not an integer!"