from BLZW_encoder import Encoding
from BLZW_decoder import Decoding
from Importance_class import Importance_calculations

from nltk.corpus import gutenberg

def main():
    macbeth = gutenberg.raw('shakespeare-macbeth.txt')
    #text = macbeth.replace('\n', '')

    file = open('no_rel/data.txt', 'r')
    #text = file.readlines()[0]
    text = "aababbabbaababba"
    #text = "aababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababbaaababbabbaababba"
    imp = Importance_calculations(text)
    rectified = imp.filter(text)
    z,occ = imp.importance_sorting()
    encode_order = imp.encode_rank()


    enc = Encoding(rectified, encode_order)
    code = enc.encoded()
    clear_code = enc.ambiguity_solver()
    print("The Encoded version is: ", code)
    print("The inambiguous version is: ", clear_code)

def decode(clean_code):
    decoder = Decoding(clean_code)
    decoded = decoder.decoder()
    print(decoded)

if __name__ == "__main__":
    main()