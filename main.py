#annoying tv gatekeeper program

tvShow = input("What is your favorite tv show? ")
if tvShow == "mandalorian":
    print("oh really? we'll see about that!")
    actualName = input("What is baby Yodas actual name? ")
    if actualName == "grogu":
        print("Hmmm... You got that right...")
        actualName = input(
            "Alright then, what's the Mandalorians first name? ")
        if actualName == "din" or actualName == "djarin" or actualName == "din djarin":
            print(
                "I guess you do know your stuff, Din is right, Din Djarin. Looks like you are an actual fan!"
            )
        else:
            print(
                "You almost showed how much of a true fan you were, but the actual answer is Din! Din Djarin"
            )
    else:
        print("Hah! it's Grogu! Obviously you're not a true fan")
else:
    print("Yeah, that's cool and all… but the Mandalorian is where it's at!")
