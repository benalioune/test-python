from classes.restaurant_reviews import RestaurantReviews

def test_update_existing_review():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Add a review for the restaurant "Sushi Spot" with an initial rating of 4
    rr.add_review("Sushi Spot", "Fresh and tasty sushi.", 4)
    # Call update_review to modify the existing review for "Sushi Spot"
    update_result = rr.update_review("Sushi Spot", "Exceptional sushi and service.", 5)
    # Check if the update_result matches the expected output
    assert update_result == "Review added for Sushi Spot."
    # Call get_review to retrieve the modified review for "Sushi Spot"
    get_result = rr.get_review("Sushi Spot")
    # Check if the get_result matches the updated review details
    assert get_result == {'review_text': "Exceptional sushi and service.", 'rating': 5}

def test_update_non_existent_review():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Call update_review for a restaurant ("Grill House") that doesn't have an existing review
    result = rr.update_review("Grill House", "Best steaks in town.", 5)
    # Check if the result indicates that the review is not found
    assert result == "Review not found."