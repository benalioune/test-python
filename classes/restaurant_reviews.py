class RestaurantReviews:
    def __init__(self):
        self.reviews = {}

    def add_review(self, restaurant, review_text, rating):
        # Check if the rating is within the valid range
        if rating < 1 or rating > 5:
            return "Invalid rating. It must be between 1 and 5."
        # Add the review to the dictionary
        self.reviews[restaurant] = {'review_text': review_text, 'rating': rating}
        return f"Review added for {restaurant}."

    def get_review(self, restaurant):
        # Retrieve the review for the specified restaurant, or return a default message if not found
        return self.reviews.get(restaurant, "Review not found.")

    def update_review(self, restaurant, new_review_text, new_rating):
        # Check if the restaurant exists in the reviews
        if restaurant not in self.reviews:
            return "Review not found."
        # Call add_review to update the existing review with new information
        return self.add_review(restaurant, new_review_text, new_rating)

    def delete_review(self, restaurant):
        # Check if the restaurant exists in the reviews
        if restaurant not in self.reviews:
            raise ValueError("Review not found to delete.")
        # Delete the review for the specified restaurant
        del self.reviews[restaurant]
        return "Review deleted for {}.".format(restaurant)