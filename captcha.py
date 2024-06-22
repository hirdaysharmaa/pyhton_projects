import random

# Define the characters allowed in the CAPTCHA
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Length of the CAPTCHA text
captcha_length = 5

# Generate random CAPTCHA text
captcha_text = "".join(random.sample(characters, captcha_length))

# Print the generated CAPTCHA text
print("Your CAPTCHA:", captcha_text)








