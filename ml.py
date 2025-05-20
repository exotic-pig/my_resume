from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AI:
    def __clean_sentence(self, sentence):
        return sentence.split("+++$+++")[4].strip(" ").replace("\n", "")

    def __init__(self):
        self.sentences = []
        with open("movie_lines.txt", encoding="utf-8", errors='ignore') as f:
            for line in f.readlines():
                self.sentences.append(self.__clean_sentence(sentence=line))
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.sentences)

    def chatbot_response(self, user_sentence):
        user_vec = self.vectorizer.transform([user_sentence])
        similarities = cosine_similarity(user_vec, self.X)
        best_match = similarities.argmax()
        return self.sentences[best_match]
