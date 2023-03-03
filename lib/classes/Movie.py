from classes.Review import Review


class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        Movie.add_to_all(self)

    @classmethod
    def add_to_all(cls, review):
        cls.all.append(review)

    def get_title(self):
        return self._title

    def set_title(self, title):
        if (isinstance(title, str)) and (0 < len(title)):
            self._title = title

    title = property(get_title, set_title)

    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return [review.viewer for review in self.reviews()]

    def average_rating(self):
        ratings = [review.rating for review in self.reviews()]
        return (sum(ratings)/len(ratings))

    @classmethod
    def highest_rated(cls):
        all_movies = cls.all
        all_movies.sort(key=lambda x: x.average_rating(), reverse=True)
        return all_movies[0]