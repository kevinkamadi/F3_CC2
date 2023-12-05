class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name().lower() == name.lower():
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name.lower() == name.lower()]


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list({review.customer for review in self.reviews})

    @classmethod
    def all(cls):
        return cls.all_restaurants
    
    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:         
            return total_ratings / num_reviews
        else:                                                   # Return 0 for no reviews yet
            return 0  


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        restaurant.reviews.append(self)
        customer.reviews.append(self)
        Review.all_reviews.append(self)

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews
    
def main():
    # Instantiate some customers, restaurants, and reviews
    customer1 = Customer("Ronald", "Drew")
    customer2 = Customer("Peterson", "Davis")
    # customer3 = Customer("Jack", "D")
    # customer4 = Customer("Rambo", "Red")
    # customer5 = Customer("Tk", "Travis")
    # customer6 = Customer("ManBoy", "Kev")


    restaurant1 = Restaurant("Club Kiboko")
    restaurant2 = Restaurant("Big Spoon")
    # restaurant3 = Restaurant("Lilian Hotel")
    # restaurant4 = Restaurant("Maggies")
    # restaurant5 = Restaurant("Boma Inn")
    # restaurant6 = Restaurant("KFC")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)
    # review3 = Review(customer2, restaurant2, 3)
    # review4 = Review(customer2, restaurant2, 5)
    # review5 = Review(customer2, restaurant2, 5)
    # review6 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(customer1.full_name())  # Output: Ronald Drew
    print(restaurant2.average_star_rating())  # Output: 5.0
    print(customer2.num_reviews())  # Output: 1

if __name__ == '__main__':
    main()