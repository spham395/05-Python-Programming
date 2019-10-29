nouns = []
adjectives = []
verbs = []
adverbs = []
noun = ""
adjective = ""
verb = ""
adverb = ""
count = 1

def is_input_valid(string_input):
    if string_input.isalnum():
        return string_input
    else:
        return "Invalid Input"

def display_words(*argv):
    print("Here are your words")
    count = 0
    for arg in argv:
        for item in arg:
            print("{}. {}".format(count, item))
            count += 1

def get_input(arg_type, arg_word, arg_list):
    while True:
        arg_word = input("Add {}: ".format(arg_type))
        if arg_word == "quit" or arg_word == 'q':
            break
        if is_input_valid(arg_word) != arg_word:
            break
        arg_list.append(arg_word)

def word_in_list(word):
    if word in nouns:
        return word
    if word in adjectives:
        return word
    if word in verbs:
        return word
    if word in adverbs:
        return word
    return "Invalid Input"

def check_all(selected_word):
    if selected_word == "quit" or selected_word == 'q':
        return False
    if is_input_valid(selected_word) != selected_word:
        return False
    if word_in_list(selected_word) != selected_word:
        return False

get_input('nouns', noun, nouns)
get_input('adjectives', adjective, adjectives)
get_input('verbs', verb, verbs)
get_input('adverbs', adverb, adverbs)

display_words(nouns, adjectives, verbs, adverbs)

message = "This {adj} {nou} can {ver} {adv}."
selected_noun = ""
selected_adjective = ""
selected_verb = ""
selected_adverb = ""


    selected_noun = input("Enter noun to select")
    selected_adjective = input("Enter adjective to select")
    selected_verb = input("Enter verb to select")
    selected_adverb = input("Enter adverb to select")

    check_all(selected_noun)
    check_all(selected_adjective)
    check_all(selected_verb)
    check_all(selected_adverb)

print(message.format(adj=selected_adjective, 
                    nou=selected_noun, 
                    ver=selected_verb, 
                    adv=selected_adverb))
