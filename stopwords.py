#Open cmd Type the following commands 
#   pip install regex  
#   pip install --user -U nltk


#need one text file with 3-4 line text = test.txt




import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


f = open('test.txt', 'r').read()

tok = word_tokenize(f)

print("Enter a choice to process your text:\n1: Convert to lowercase\n2: Convert to uppercase\n3: Tokenize\n4: Remove numbers\n5: Remove punctuation\n6: Remove spaces\n7: Remove stopwords")

while True:
    c = int(input())
    if c == 1:
        print(f.lower())
    elif c == 2:
        print(f.upper())
    elif c == 3:
        print(tok)
    elif c == 4:
        print(re.sub(r'[0-9]', '', f))
    elif c == 5:
        print(f.translate(str.maketrans('', '', string.punctuation)))
    elif c == 6:
        print(f.replace(" ", ""))
    elif c == 7:
        print([i for i in tok if not i in set(stopwords.words('english'))])
    else:
        print("Please enter a choice between 1-7")
