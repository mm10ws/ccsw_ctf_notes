from pickletools import bytes1
from PIL import Image


def getbytes(bits):
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte


if __name__ == "__main__":
    print("go")

    ref_img = Image.open("ref.png")
    steg_img = Image.open("ccsw.png")

    ref_px = ref_img.load()
    steg_px = steg_img.load()

    print(f"ref: {ref_img.width}, {ref_img.height}")
    print(f"steg: {steg_img.width}, {steg_img.height}")

    width = ref_img.width
    height = ref_img.height

    bits = []
    max_width = 0

    for i in range(0, width):
        for j in range(0, height):
            r_ref, g_ref, b_ref, a_ref = ref_img.getpixel((i, j))
            r_steg, g_steg, b_steg, a_steg = steg_img.getpixel((i, j))

            if r_steg == 255 and g_steg == 255 and b_steg == 255:
                bits.append(1)
                max_width = i
            elif r_steg == 255 and g_steg == 255 and b_steg == 254:
                bits.append(0)

    byts = getbytes(iter(bits))
    result = bytearray()
    for b in byts:
        result += b.to_bytes(1, "big")
    
    with open("out.bin", "wb") as f:
        f.write(result)
