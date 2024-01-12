import pytest
from classes.restaurant_reviews import RestaurantReviews

def test_delete_existing():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Add a review for testing
    rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
    # Call delete_review for an existing restaurant
    result = rr.delete_review("Pasta Palace")
    # Check if the result matches the expected output
    assert (result == "Review deleted for Pasta Palace.")
    
    # Additional functional part to the test:
    # Test the implications of the review deletion
    result2 = rr.get_review("Pasta Palace") 
    # Check if the result2 indicates that the review is not found
    assert(result2 == "Review not found.")

# Check the non-functioning case with an exception
def test_delete_non_existing():
    # Create an instance of RestaurantReviews
    rr = RestaurantReviews()
    # Use pytest.raises to check if a ValueError is raised during the delete_review call
    with pytest.raises(ValueError) as e:
        rr.delete_review('Unkown Restaurant')
    # Check if the exception message matches the expected output
    assert str(e.value) == "Review not found to delete."