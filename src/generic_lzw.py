from collections import defaultdict

def lzw(data):
        dictionary = []
        counter = defaultdict(int)
        phrase = ""
        for char in data:
            new_phrase = phrase + char
            
            if new_phrase in dictionary:
                phrase = new_phrase
            else:
                counter[phrase] += 1
                dictionary.append(new_phrase)
                phrase = ''
        #print('importance dictionary:', dictionary)
        encode = ''
        lzw_dict = {}
        for char in dictionary:
            if len(char) == 1:
                encode += '#' + char
                lzw_dict[char] = dictionary.index(char)+1 
            else:
                prev = lzw_dict[char[:-1]]
                lzw_dict[char] = dictionary.index(char)+1
                encode += str(prev)+char[-1]
        return encode