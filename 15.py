def reverse_sentence():
    juzi = input("Just write some sentence, please: ")
    juzi_split = juzi.split()
    result = []

    for i,e in enumerate(juzi_split):
        result.append(juzi_split[len(juzi_split)-1-i])

    return result

print reverse_sentence()
