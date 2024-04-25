import utils

class Receiver:
    def __init__(self, relay_server, identifier):
        self.relay_server = relay_server
        self.identifier = identifier
        self.relay_server = relay_server
        self.private_key, self.public_key = utils.generate_key_pair()
        self.relay_server.register_public_key('receiver', self.public_key)
    
    def receive_message(self, sender_id, iv, ciphertext, tag):
        sender_public_key_bytes = self.relay_server.get_public_key(sender_id)
        sender_public_key = utils.deserialize_public_key(sender_public_key_bytes)
        shared_secret = self.private_key.exchange(sender_public_key)
        key = utils.derive_key(shared_secret)
        plaintext = utils.decrypt_message(key, iv, ciphertext, tag)
        print(f"Received message: {plaintext.decode('utf-8')}")
