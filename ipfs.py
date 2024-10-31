import requests

def upload_image_to_ipfs(image_path):
    # URL of the local IPFS node API
    url = "http://localhost:5001/api/v0/add"

    # Read the image file as binary
    with open(image_path, "rb") as file:
        # Prepare the file for uploading
        files = {"file": file}

        # Post the request to add the image to IPFS
        response = requests.post(url, files=files)
        
        # Check if the request was successful
        if response.status_code == 200:
            ipfs_hash = response.json()["Hash"]
            print(f"Image uploaded to IPFS with hash: {ipfs_hash}")
            print(f"Access the image at: https://ipfs.io/ipfs/{ipfs_hash}")
            return ipfs_hash
        else:
            print("Failed to upload image to IPFS:", response.text)
            return None

image_path = "WhatsApp Image 2024-10-21 at 11.42.55_0503b66f.jpg"
upload_image_to_ipfs(image_path)
