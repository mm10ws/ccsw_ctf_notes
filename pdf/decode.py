import sys

# ripped from the rom
encoded_bytes = [
    bytes.fromhex(
        "a4875abf9b24abce6156ea4c9e3d440a762bb7bf9fd52a04b3877adf48fa9027979ebb5296d69220605651fe047b4b2671b494446721c86337bc5a5e04179138b36f7f1ea322da83d4bf4bff6a2540d282caaf53850e9aa07051b4dd879b4ab1a4428c7a6b176a61368ffb415daaa63d89528a5d661a7a06b77fad7db76aca065eab596bc4fa9ac58746b3a99810380bc708437e656b91f01794683d8f8a3b3f272b6a446fc33bd3679e1a42c6c0481f84a58f7f53efbde4040af83e142b453c7759b14761ee529187b678b9c7ce495148a95aa797ca4ac5d75e49a25bca5e26068d5a0e37ffcb4192a51b3f27c85809a6b452ff5ec94ac162585b81041b9a80"
    ),
    bytes.fromhex(
        "605245ae262f9c348a0b581fb61255c3344aa9dfd41f28c0e6cb55cf85c6fbb0c645bf4c713cab8107e87baa951a9de19b81fba89f78bab38aa5bc9f632690615b42802e765b49e46d82b381a42f84c2995e454648c9dbb371b7ad2d8e1a0bc9a48dcb5bb22618cf70a955824100867f5a99a185520fb0197e8e96964d07b0026c8e9880520db0117e8ea39b4a32950540888e8c4c0f852f52a19f9b5909802d529690897e20e7ce65ab4eac9a4a6bf117086b2e9f5b2bce845b38a4e64ae8c28fb46acfd4275750d4478d1d75cb185353aa083d6d28b5c58cb1fbbf563c5ed98642ea0ef78a4ede63188f5bc7de56a39e1b554c5ed3a7816608b3ce6ad641de"
    ),
    bytes.fromhex(
        "9b947b3e79bb8ea18e8db6429a1b59e5d4818da614b82b3398b9dbae6a2eaecd644bbfa89eba388068ebf85185c66be0b7780a6bf4c7afd350185b2fe66847a15d1bbc6f279838f5c67eafa45ec2a65099c8b71d928b7f3f77bb55a35d5aeb27a7ba7a438422280960b93bb08c29fa535c4b4a47618a4480e75287ef5b7aaef1b38aaa0ec7789da3d62a7a1ee61ba8511778bb9a88aba1d3f4a9874f8d2dbb2724a952de6ec1fa21945368476b58443567b1ca4b6b0e48cf6658e8de946a48e356ad7e408cd37b226a8758a28f114ef5f48d0a475bab38e3573a7f7f94106eb17955821e941c840104a5789276ce8e53893a6a1d5625f8cf79ab8cb05b3db527"
    ),
    bytes.fromhex(
        "17b71a6a42283b0987bd3a9873297f33840a8d8b6712ea1f8e2aa552c61a1a91a2dab7ff6129a4cf57b649bea6886b43e4ab5e1d07daebe0a753452d14c3ad392655465eb33578e084456f4b9aa8ebc9639e558ba7dbfa385149497af427460ce4e8fbff6bba4e0c847f54ae683b1bcd95bdf82d8ddeafd868b543928aba4b5326bd574285e847915baf484327bbbcd9797a578b614aeb34753bda7a36fff843b694b1ed75d3840089eb823e82883af16fb7467ac70ea23736b3947f06122b3c75b8ea6e5c1243f357b5aa6e6f6a3a31a20b6f945e0ea4c8687e424f654b7a3d61429e7e99b892dc604bbdce615b572496458a3f857b7b53652bb1afc723a281"
    ),
]

# what we will xor with the sections
check_bytes = bytes.fromhex("262c212745372810")

# each value corresponds with a valid key you can press on the NES. The password must be made up of this charset.
valid_byteset_alt = [201, 58, 164, 177, 33, 43, 109, 161]


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def check_bytes_valid(test_bytes):
    for b in test_bytes:
        if b not in valid_byteset_alt:
            return False
    return True


if __name__ == "__main__":
    for i in range(0, 256 - 8):
        for j, section in enumerate(encoded_bytes):
            slice = section[i : i + 8]
            check_chunk = byte_xor(slice, check_bytes)
            print(f"Checking: {slice.hex()}")
            if check_bytes_valid(check_chunk):
                print(f"Success: {check_chunk.hex()}, slice:{i}, section:{j}")
                sys.exit(0)
