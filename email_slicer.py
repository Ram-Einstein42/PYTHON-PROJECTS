# Email Slicer Project

# Step 1: Get email from user
email = input("Enter your email address: ")

# Step 2: Split email into parts
try:
    username, domain = email.split("@")

    # Step 3: Display results
    print("\n--- Email Details ---")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
except ValueError:
    print("Invalid email format. Please include an '@' symbol.")

