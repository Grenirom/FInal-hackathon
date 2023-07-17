import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

print(stripe.Product.create(name="Gold Special"))

# stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
#
# stripe.Price.create(
#   currency="usd",
#   unit_amount=1000,
#   product='{{PRODUCT_ID}}',
# )