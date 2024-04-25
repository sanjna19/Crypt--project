class RelayServer:
    def __init__(self):
        self.public_keys = {}
        self.last_message = None  # Add this line to initialize last_message
    
    def register_public_key(self, identifier, public_key):
        self.public_keys[identifier] = public_key
    
    def get_public_key(self, identifier):
        return self.public_keys.get(identifier)
    
    def relay_message(self, receiver, iv, ciphertext, tag):
        # Store the message details so it can be retrieved later
        self.last_message = (iv, ciphertext, tag)  # Add this line to store the message

        # In a real application, you'd relay the message to the receiver, not just print it
        print(f"Message relayed to {receiver}: {ciphertext}")
