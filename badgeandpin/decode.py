if __name__ == "__main__":
    # Encoded flag bytes taken from address 0x0ef8 (36 bytes)
    encoded_flag = (
        "af85deba7e78475c97e2a0c5621c3a309cfea3c571674736849fdeca1e79213485e3c5e3"
    )
    const_xor_factor = 0xAAAAAAAA
    result = b""

    # Key 4 bytes (dont care what it is since it is only used to decode the first 4 bytes)
    key = 0xDEADBEEF

    # Do the same thing the decoding code is doing in the rom
    for i in range(9):
        # Take 4 bytes at a time from the encoded flag and cast as int
        encoded_bytes = bytes.fromhex(encoded_flag[i * 8 : i * 8 + 8])

        # Big endian to match sega saturn processor
        encoded_bytes_as_int = int.from_bytes(encoded_bytes, "big")

        # Decode
        decoded_int = encoded_bytes_as_int ^ key ^ const_xor_factor
        decoded_bytes = decoded_int.to_bytes(4, "big")
        result += decoded_bytes

        # Update the key for next iteration
        key = encoded_bytes_as_int

    print(result)
