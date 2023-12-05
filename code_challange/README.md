Restaurant Review System
Overview

This Python script implements a simple restaurant review system using three main classes: Customer, Restaurant, and Review. It allows you to create customers, restaurants, and reviews, and provides basic functionality for retrieving information about customers, restaurants, and reviews.
Table of Contents

   - Installation
   - Usage
   - Classes
       . Customer
       . Restaurant
       . Review

Installation

 1. Clone the repository:

    bash

git clone https://github.com/kevinkamadi/Restaurant-Review-System
cd restaurant-review-system

2. Run the script:

bash

    python main.py

Usage

The main.py script serves as an example of how to use the implemented classes. It demonstrates creating customers, restaurants, and reviews, and using various methods to obtain information.

python

python main.py

Classes
Customer

The Customer class represents a customer and has the following methods:

    full_name(): Returns the full name of the customer.
    restaurants(): Returns a list of restaurants reviewed by the customer.
    add_review(restaurant, rating): Adds a new review for a restaurant.
    num_reviews(): Returns the number of reviews submitted by the customer.
    find_by_name(name): Finds a customer by their full name.
    find_all_by_given_name(name): Finds all customers with a given first name.

Restaurant

The Restaurant class represents a restaurant and has the following methods:

    average_star_rating(): Calculates and returns the average star rating based on reviews.
    customers(): Returns a list of customers who reviewed the restaurant.

Review

The Review class represents a customer's review for a restaurant and has the following methods:

    customer(): Returns the customer associated with the review.
    restaurant(): Returns the restaurant associated with the review.
    rating(): Returns the rating given in the review.