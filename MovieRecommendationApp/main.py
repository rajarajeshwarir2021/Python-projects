import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from surprise import Dataset, Reader, SVD, model_selection

"""
###################### POPULARITY BASED FILTERING ######################

movies = pandas.read_csv("dataset/movies_metadata.csv", low_memory=False)
credits = pandas.read_csv("dataset/credits.csv")
ratings = pandas.read_csv("dataset/ratings.csv")

#print(movies.head())
#print(credits.head())
#print(ratings.head())

m = movies["vote_count"].quantile(0.9)
print(m)

C = movies["vote_average"].mean()
print(C)

movies_filtered = movies.copy().loc[movies["vote_count"] >= m]


def weighted_rating(df, m=m, C=C):
    R = df["vote_average"]
    v = df["vote_count"]
    wr = (v / v+m) * R + (m / (v+m) * C)
    return wr


movies_filtered["weighted_rating"] = movies_filtered.apply(weighted_rating, axis=1)
print(movies_filtered)

movies_filtered.sort_values("weighted_rating", ascending=False).head(10).to_dict()
"""

"""
###################### CONTENT BASED FILTERING ######################

movies_content = pandas.read_csv("dataset/movies_metadata.csv")
print(movies_content)

tfidf = TfidfVectorizer(stop_words="english")
movies_content["overview"] = movies_content["overview"].fillna("")
print(movies_content["overview"])

tfidf_matrix = tfidf.fit_transform(movies_content["overview"])
print(tfidf_matrix)

pandas.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print(tfidf_matrix.shape)

similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
print(similarity_matrix)


def similar_movies(movie_title, nr_movies):
    idx = movies_content.loc[movies_content["title"] == movie_title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    movies_indices = [tpl[0] for tpl in scores[1:nr_movies+1]]
    similar_titles = list(movies_content["title"].iloc[movies_indices])

    return similar_titles


print(similar_movies("Kung Fu Panda 3", 3))
"""

###################### COLLABORATIVE BASED FILTERING ######################

ratings = pandas.read_csv("dataset/ratings.csv")[["userId", "movieId", "rating"]]
reader = Reader(rating_scale(1, 5))
dataset = Dataset.load_from_df(ratings, reader)
print(dataset)

trainset = dataset.build_full_trainset()

list(trainset.all_ratings())

# Train the model
svd = SVD()
svd.fit(trainset)
svd.predict(15, 1956)

# Validation
model_selection.cross_validate(svd, dataset, measures=["RMSE", "MAE"])






