def single_root_words(root_word,*other_words):
    same_words=[]
    other_words_lower = [item.lower() for item in other_words]
    j = 0
    for i in other_words_lower or other_words:
        if root_word.lower() in i or i in root_word.lower():
            same_words.append(other_words[j])
        j += 1
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)