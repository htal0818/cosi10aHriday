from random import choice

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def questions():
    """
        simulate a customer service representative who is asking about your iPhone
        this function asks the user questions
        based on the answer to the previous question
    """
    userComment = input("Computer >> What seems to be the problem?\nThe User >> ")

    while userComment not in ["goodbye","bye","quit","exit"]:
        humanResponses.append(userComment)
        response = respond(userComment)
        if response in computerResponses:
            response = "Once again, "+response
        computerResponses.append(response)
        print("Computer >> "+response)
        userComment = input("The User >> ")
    print("bye")

def respond(comment):
    """ generate a computer response to the user's comment"""
    if contains(comment,broken):
        return choice(brokenresponses)
    if contains(comment,newphone):
        return choice(salesresponse)
    if len(comment.split()) <= 2:  # respond to short answers...
        return choice(pleaseanswer)
    return choice(generalResponses)

def contains(sentence,words):
    """ true if one of the words is in the sentence
        where sentence is a string and
        words is a list of strings
    """
    wordsInSentence = [word for word in words if word in sentence]
    return len(wordsInSentence) >= 1

def contains2(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the keywords and responses to phone damage comments
broken = "cracked screen broken software not starting water damage".split()
brokenresponses=[
"how did you damage your phone?",
"Do you have Applecare?",
"Would you like to buy a new phone?",
]


# Here are the mad keywords and response to comments containing a mad keyword
newphone = "new phone product replacement".split()
salesresponse = [
  "Let me see the damage",
  "We have three models",
  "Wait here while I see what we have in stock",
  "Are you experiencing any other issues right now?",

]

# these are the possible responses to short comments
# like "yes" or "no" or "idk"
pleaseanswer = [
    "Could you please elaborate?",
    "Would you mind elaborating?",
    "What else?",
    "Anything more to say?",
    "Tell me more",
    "Please specify your problem",
    "I need a little more information, can I ask you more questions?"
]

# We give these responses if there is nothing else to say!
generalResponses = [
  "Would you like to scheduele an appt with the Genius bar?",
  "Would you like to buy the new iPhone 11?",
  "Tell me about your relationship with your mother?",
  "Let me run a diagnostic test on your phone",
  "is your phone backed up to Icloud?",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]


if __name__=="__main__":
    questions()  # call questions when run as a script
         # but not when imported
