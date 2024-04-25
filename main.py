from relay_server import RelayServer
from sender import Sender
from receiver import Receiver

if __name__ == "__main__":
    relay_server = RelayServer()
    sender = Sender(relay_server)
    receiver = Receiver(relay_server, 'receiver')

    # Sender sends a message
    plaintext = "Hello, secure world!"
    print(f"Sender is sending: {plaintext}")
    sender.send_message('receiver', plaintext)

    # Simulate receiver receiving the last relayed message
    if relay_server.last_message is not None:
        iv, ciphertext, tag = relay_server.last_message
        receiver.receive_message('sender', iv, ciphertext, tag)
    else:
        print("No message has been relayed.")

      