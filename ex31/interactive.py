print "You enter an enchanted castle with two hallways.  Do you go through door #1 or door #2?"

hallway = raw_input("> ")

if hallway == "1":
    print "There's a jester picking his toenails.  What do you do?"
    print "1. Stand there and get hit by toenail lint."
    print "2. Run away."

    toenail = raw_input("> ")

    if toenail == "1":
        print "The toenail goes into your eye.  Good job!"
    elif toenail == "2":
        print "You run into a wall.  Good job!"
    else:
        print "Well, doing %s is probably better.  Jester runs away." % bear

elif hallway == "2":
    print "You walk into a punk rock concert."
    print "1. Faint."
    print "2. Crowd surf."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
