def xor_bytes(arr1, arr2):
    return bytearray([_a ^ _b for _a, _b in zip(arr1, arr2)])


if __name__ == "__main__":
    encoded_flag = [
        0xAF,
        0x85,
        0xDE,
        0xBA,
        0x7E,
        0x78,
        0x47,
        0x5C,
        0x97,
        0xE2,
        0xA0,
        0xC5,
        0x62,
        0x1C,
        0x3A,
        0x30,
        0x9C,
        0xFE,
        0xA3,
        0xC5,
        0x71,
        0x67,
        0x47,
        0x36,
        0x84,
        0x9F,
        0xDE,
        0xCA,
        0x1E,
        0x79,
        0x21,
        0x34,
        0x85,
        0xE3,
        0xC5,
        0xE3,
    ]

    # key = bytearray(b"k#\x1cI")

    # for i in range(9):
    #     part_bytes = bytearray(encoded_flag[i:i+4])
    #     print(f"part: {part_bytes.hex()}")


    #     print(xor_bytes(xor_bytes(key, part_bytes[::-1]), bytearray([0xAA, 0xAA, 0xAA, 0xAA])))

    #     key = part_bytes

    const1 = int.from_bytes(bytearray([0xAA, 0xAA, 0xAA, 0xAA]), "big")
    result = int.from_bytes(bytearray(b"{W3L"), "big")
    part = int.from_bytes(bytearray(encoded_flag[0:4]), "big")

    key = const1 ^ result ^ part
    print(key)
