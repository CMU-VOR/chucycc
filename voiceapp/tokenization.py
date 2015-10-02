
class Tokenization:
    
    with open("stopwords.txt", "r") as stopWords:
        stoplist = [line.rstrip() for line in stopWords]
    print("here")
    
    @classmethod
    def tokenization(self,text_string):
        words = text_string.split()
        result = []
    
        for word in words:
            if word not in self.stoplist:
                result.append(word)
    
        return result
