from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[:5])


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()

    # Add the customer preference to the list
    customer_preferences.append(preference.lower())

    response = input("Do you want to add another preference? (Y/N): ").upper()


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        matches = count_matches(product["tags"], customer_tags)

        if matches > 0:
            recommendations.append({
                "name": product["name"],
                "matches": matches
            })

    recommendations.sort(
        key=lambda product: product["matches"],
        reverse=True
    )

    return recommendations


# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(
    converted_products,
    customer_preferences
)

print("\nRecommended Products:")

for product in recommendations:
    print(f"- {product['name']} ({product['matches']} match(es))")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

# I designed the recommendation tool using lists and sets to organize and
# compare customer preferences with product tags. The main operations I used
# were loops, list append operations, set conversion, set intersection, and
# sorting. A list is useful for storing the collection of products because it
# allows the program to loop through each product. I converted the customer
# preferences and product tags into sets because sets make it easy to find
# shared values. The intersection operation identifies tags that appear in
# both the customer preferences and a product's tags. I then use the length
# of the intersection to calculate the product's match score.
#
# The recommendation function loops through the product catalog and calls
# the count_matches function for each product. Products with at least one
# matching preference are added to the recommendation list. Finally, the list
# is sorted by the number of matching tags so that products with stronger
# matches appear first.
#
# If the catalog grew to 1,000 or more products, the basic approach could
# still work, but I would consider improving how products are searched and
# organized. For a much larger catalog, I could use a dictionary that maps
# each tag to the products containing that tag. This would reduce the amount
# of data that needs to be checked for every customer. I could also consider
# storing the catalog in a database rather than keeping everything in memory.
# The current solution is intentionally simple because the goal is to practice
# core Python data structures and operations.
