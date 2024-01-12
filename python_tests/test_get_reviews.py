from classes.restaurant_reviews import RestaurantReviews

def test_get_existing_review():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Add a review for the restaurant "Pasta Palace" with a rating of 5
    rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
    # Call get_review for an existing restaurant ("Pasta Palace")
    result = rr.get_review("Pasta Palace")
    # Check if the result matches the expected output
    assert result == {'review_text': "Delicious pasta dishes.", 'rating': 5}

def test_get_non_existent_review():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Call get_review for a restaurant ("Burger Bistro") that doesn't have a review
    result = rr.get_review("Burger Bistro")
    # Check if the result indicates that the review is not found
    assert result == "Review not found."