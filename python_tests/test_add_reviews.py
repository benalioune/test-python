
from classes.restaurant_reviews import RestaurantReviews


def test_add_valid_review():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Call add_review with valid parameters
    result = rr.add_review("Cafe Mocha", "Great coffee and pastries.", 4)
    # Check if the result matches the expected output
    assert result == "Review added for Cafe Mocha."
    # Uncomment the line below to check the stored review details
    # assert rr.get_review("Cafe Mocha") == {'review_text': "Great coffee and pastries.", 'rating': 4}

def test_add_invalid_rating_above_5():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Call add_review with an invalid rating above 5
    result = rr.add_review("Cafe Mocha", "Good ambiance.", 6)
    # Check if the result matches the expected output
    assert result == "Invalid rating. It must be between 1 and 5."

def test_add_invalid_rating_below_1():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Call add_review with an invalid rating below 1
    result = rr.add_review("Cafe Mocha", "Good ambiance.", 0)
    # Check if the result matches the expected output
    assert result == "Invalid rating. It must be between 1 and 5."