import utils

class Sender:
    def __init__(self, relay_server):
        self.relay_server = relay_server
        self.private_key, self.public_key = utils.generate_key_pair()
        self.relay_server.register_public_key('sender', self.public_key)
    
    def send_message(self, receiver_id, plaintext):
        receiver_public_key_bytes = self.relay_server.get_public_key(receiver_id)
        receiver_public_key = utils.deserialize_public_key(receiver_public_key_bytes)
        shared_secret = self.private_key.exchange(receiver_public_key)
        key = utils.derive_key(shared_secret)
        iv, ciphertext, tag = utils.encrypt_message(key, plaintext.encode('utf-8'))
        self.relay_server.relay_message(receiver_id, iv, ciphertext, tag)
