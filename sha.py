import hashlib

# Define the string to be encrypted
message = "Hello, World!"

# Encode the message into bytes using UTF-8 encoding
message_bytes = message.encode('utf-8')

# Use SHA-256 algorithm to create a hash object
hash_object = hashlib.sha256()

# Update the hash object with the message bytes
hash_object.update(message_bytes)

# Get the hex digest of the hash object
hash_hex = hash_object.hexdigest()

print("Original message: ", message)
print("Encrypted message: ", hash_hex)