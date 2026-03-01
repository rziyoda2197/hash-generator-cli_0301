import hashlib

text = input("Enter text to hash: ").strip()

print("\nChoose algorithm:")
print("1. MD5")
print("2. SHA256")

choice = input("Enter choice (1/2): ")

if choice == "1":
    hashed = hashlib.md5(text.encode()).hexdigest()
    print("MD5:", hashed)
elif choice == "2":
    hashed = hashlib.sha256(text.encode()).hexdigest()
    print("SHA256:", hashed)
else:
    print("Invalid choice.")
