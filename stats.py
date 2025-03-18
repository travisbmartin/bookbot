def word_count(file):
    f = file.split()
    count = len(f)
    return count

def char_count(file):
    char_dic = {}
    f = file.lower()
    s = list(f)
    for chars in range(0,len(s)):
        x = s[chars]
        if x in char_dic:
            char_dic[x] += 1
        else:
            char_dic[x] = 1
    return char_dic

def char_sort(chars):
    dlist = []
    for letter, count in chars.items():
        dlist.append({"char": letter, "count": count})
    print(dlist)
    dlist.sort(key=lambda item: item["count"], reverse=True)
    return dlist
