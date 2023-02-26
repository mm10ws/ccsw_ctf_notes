from Crypto.Cipher import AES

def unscramble(byte_string):
    result = bytearray(byte_string)

    # Do the reverse of what the binary did: bytes[i+1] = bytes[i+1] ^ bytes[i])
    for i in reversed(range(1,16)):
        result[i] = result[i] ^ result[i - 1]
    return result

if __name__ == "__main__":
    # Taken from pcap
    key = b"Prestidigitation"
    payload_bytes1 = bytes.fromhex("e1dbfd6826a14f279fafe76982333070")
    payload_bytes2 = bytes.fromhex("a0595e10eec5ffd64cf3569eac102451")

    # Init cypher as ECB mode to match what openssl will use for AES_encrypt
    decipher = AES.new(key, AES.MODE_ECB)

    # Decrypt using key
    msg1 = decipher.decrypt(payload_bytes1)
    msg2 = decipher.decrypt(payload_bytes2)

    # Print what we got so far, should still be scrambled at this point
    print(msg1 + msg2)

    # Unscramble both messages
    result1 = unscramble(bytearray(msg1))
    result2 = unscramble(bytearray(msg2))
    
    # At this point we should have the decrypted and decoded messages
    print(result1 + result2)
