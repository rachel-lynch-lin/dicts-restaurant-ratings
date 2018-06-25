import sys
"""Restaurant rating lister."""


def gets_restaurant_ratings(text_file):
    """reads restaurant ratings in a file and prints in alphabetical order"""
    file = open(text_file)
    restaurant_ratings_dictionary = {}

    for line in file:
        line = line.rstrip().split(":")
        restaurant_name, rating = line
        restaurant_ratings_dictionary[restaurant_name] = rating

    file.close()

    return restaurant_ratings_dictionary


def alphabetized_restaurant_ratings(restaurant_ratings_dictionary):
    """Alphabetizes restaurant ratings dictionary"""
    for name, rating in sorted(restaurant_ratings_dictionary.items()):
        print(f"{name} is rated at {rating}.")


file_name = sys.argv[0]
text_file = sys.argv[1]

restaurant_ratings_dictionary = gets_restaurant_ratings('scores.txt')
alphabetized_restaurant_ratings(restaurant_ratings_dictionary)
