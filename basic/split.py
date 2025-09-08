# задача - сделай функцию split() туда передается строка
# она возвращает список слов в ней
# split("   ира      ест  кашу")
# [ "ира", "ест", "кашу" ]


def split(s):
    text = []
    word = "" # variable for word building
    # letter = l

    for l in s:
        if l != " ": # if there are no spaces we add char to the word
            word += l
            # but if there are spaces and 
            if word != "": # if this word not empty
                text.append(word)  # we finished the word

            # how to finish and check if there are all done 
        

def main():
    test = split("   ира      ест  кашу")
    return(s)

main()