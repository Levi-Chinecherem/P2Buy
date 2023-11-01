# recommendations/recommendations.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommendation:
    def __init__(self, products):
        self.products = products
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(products['description'])

    def get_recommendations(self, product_id, num_recommendations=5):
        cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        product_idx = self.products[self.products['id'] == product_id].index[0]
        similar_products = list(enumerate(cosine_sim[product_idx]))
        similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)
        similar_products = similar_products[1:num_recommendations + 1]
        recommended_product_ids = [x[0] for x in similar_products]
        return self.products.iloc[recommended_product_ids]
