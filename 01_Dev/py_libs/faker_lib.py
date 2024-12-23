from faker import Faker

fake = Faker()

print(fake.name())           # Output: A random name (e.g., John Smith)
print(fake.address())        # Output: A random address
print(fake.text())          # Output: Random lorem ipsum text
print(fake.email())         # Output: A random email address
print(fake.date_of_birth())# Output: A random birthdate
print(fake.credit_card_number()) #for testing purposes ONLY. Never use this for illicit purposes
fake_fr = Faker('fr_FR')
print(fake_fr.name()) #Output a French name
