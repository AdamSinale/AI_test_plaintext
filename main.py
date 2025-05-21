
from api_called import send_api_key

def main():
    # Hardcoded API key (should NEVER be committed to git)
    api_key = "abstract 4f8aeb7c9123d4f5a6b7c8d9e0f1a2b3"
    send_api_key(api_key)

if __name__ == "__main__":
    main()
