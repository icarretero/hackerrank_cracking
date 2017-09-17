def ransom_note(magazine, ransom):
    magazine_dict = {}
    for magazine_item in magazine:
        magazine_dict[magazine_item] = magazine_dict.get(magazine_item, 0) + 1
    for ransom_item in ransom:
        words_available = magazine_dict.get(ransom_item, 0)
        if words_available > 0:
            magazine_dict[ransom_item] -= 1
        else:
            return False
    return True
            

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
