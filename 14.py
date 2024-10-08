from mrjob.job import MRJob
class MovieSimilarities(MRJob):
    def mapper(self, _, line):
        fields = line.split("::")
        if len(fields) == 3:
            twitter_id, movie_name, genre = fields
            yield genre, movie_name
        else:
            self.increment_counter('warning', 'invalid_line_format', 1)
            print(f"Warning: Skipping invalid line: {line}")

    def reducer(self, genre, movies):
        movie_list = list(movies)
        for i in range(len(movie_list)):
            for j in range(i + 1, len(movie_list)):
                movie1 = movie_list[i].decode('utf-8') if isinstance(movie_list[i], bytes) else movie_list[i]
                movie2 = movie_list[j].decode('utf-8') if isinstance(movie_list[j], bytes) else movie_list[j]
                similarity_score = self.calculate_similarity(movie1, movie2)
                yield (movie1, movie2), similarity_score
    def calculate_similarity(self, movie1, movie2):
        # Convert movie names to lowercase for case-insensitive comparison
        movie1 = movie1.lower()
        movie2 = movie2.lower()
        # Calculate similarity score based on the number of common characters
        common_chars = set(movie1) & set(movie2)
        similarity_score = len(common_chars)
        return similarity_score
if __name__ == '__main__':
    MovieSimilarities.run()
