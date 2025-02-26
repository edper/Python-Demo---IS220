import random

hedges = ("Please tell me more.",
          "Many of my patients says the same thing.",
          "Please continue.")
qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")
replacements = {"i":"you","me":"you","my":"your", 
                "we":"you", "us":"you", "mine":"yours"}

def reply(sentence):
    probability = random.randint(1,4)

    if probability == 1:
       response = random.choice(hedges)
       return response
    else:
       response = random.choice(qualifiers) + changePerson(sentence)
       return response

def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(str(word).lower(),word))
    return " ".join(replyWords)


def main():
    # Output greeting to the patient
    print("Good morning. I hope you are well today.")
    print("What can I do for you? ")

    while True:
        sentence = input("\n>>")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break  
        print(reply(sentence))

if __name__ == "__main__":
    main()
