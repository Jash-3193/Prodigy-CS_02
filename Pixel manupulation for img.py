from PIL import Image
import random

# Function to encrypt the image
def encrypt_image(image_path, encryption_key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get the image dimensions
    width, height = img.size

    # Create a new encrypted image
    encrypted_img = Image.new('RGB', (width, height))
    encrypted_pixels = encrypted_img.load()

    for i in range(width):
        for j in range(height):
            # Get the original pixel value
            r, g, b = pixels[i, j]

            # Apply encryption by manipulating pixel values using the encryption key
            # Swap values and add/subtract random value based on encryption key
            encrypted_r = (r + encryption_key) % 256
            encrypted_g = (g + encryption_key) % 256
            encrypted_b = (b + encryption_key) % 256

            # Place the encrypted pixel into the new image
            encrypted_pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

# Function to decrypt the image
def decrypt_image(image_path, encryption_key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()

    # Get the image dimensions
    width, height = img.size

    # Create a new decrypted image
    decrypted_img = Image.new('RGB', (width, height))
    decrypted_pixels = decrypted_img.load()

    for i in range(width):
        for j in range(height):
            # Get the encrypted pixel value
            r, g, b = pixels[i, j]

            # Apply decryption by reversing the encryption operation
            decrypted_r = (r - encryption_key) % 256
            decrypted_g = (g - encryption_key) % 256
            decrypted_b = (b - encryption_key) % 256

            # Place the decrypted pixel into the new image
            decrypted_pixels[i, j] = (decrypted_r, decrypted_g, decrypted_b)

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

# Main function to test encryption and decryption
def main():
    # Input image path
    image_path = input("Enter the path of the image to encrypt: ")
    
    # Choose an encryption key (this can be any integer)
    encryption_key = random.randint(1, 50)  # Can be any number for a simple encryption
    
    print(f"Encryption key: {encryption_key}")

    # Encrypt the image
    encrypt_image(image_path, encryption_key)

    # Decrypt the image
    decrypt_image("encrypted_image.png", encryption_key)

if __name__ == "__main__":
    main()
