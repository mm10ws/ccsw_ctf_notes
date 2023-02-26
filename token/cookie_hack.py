import base64


if __name__ == "__main__":
    a = [123, 34, 117, 115, 101, 114, 34, 58, 34, 104, 101, 108, 108, 111, 34, 44, 34, 114, 111, 108, 101, 34, 58, 34, 117, 115, 101, 114, 115, 34, 125]
    orig_plaintext = "a"
    orig_cookie = "wceQP3q5xkINqAheu67oxNkiCpOgkF8X9Bh3I0NV8JhMUUu63jeYkXCqEuWNsQL+YxKCRDzXLZC60Wx7ae+/nQ=="

    base64_decode_cookie_bytes = base64.b64decode(orig_cookie)
    print(len(base64_decode_cookie_bytes))
    print(bytes(a))