class Imp:

    def __init__(self, file):
        self.data = self.filter(file)

    def filter(self, str):
        str = str.lower()
        i = [x for x in range(97)] 
        j = [x for x in range(123,256)]
        k = i + j
        for c in [chr(i) for i in k]:
            str = str.replace(c, '')
        return str
    #successfully filtered the sample
    def code_book(self):
        dictionary = []
        accum = ''
        for i in self.data:
            pat = accum + i
            if pat in dictionary:
                accum = pat
            else:
                dictionary.append(pat)
                accum = ''
        book = {dictionary[i]:i+1 for i in range(len(dictionary))}
        return book
    
class LZW_generic:

    def __init__(self, string, codebook):
        self.data = string 
        self.encode_order = codebook

    def encoder(self):
        accum = ''
        encoded = ''
        appeared_before = []
        for s in self.data:
            pattern = accum+s
            if pattern in appeared_before:
                accum = pattern 
            else:
                appeared_before.append(pattern)
                if len(pattern) == 1:
                    encoded += '#'+pattern 
                else:
                    encoded = encoded + str(self.encode_order[accum]) + s
                accum = ''
        return encoded, appeared_before

#text = macbeth.replace('\n', '')   
text = "aababbabbaababba"
test = Imp(text)
rect = test.filter(text)
code_book = test.code_book()
coded = LZW_generic(rect, code_book)
code,_ = coded.encoder()
print(len(code))
print(len(text))