hashes = [
    "931672ef8007efadcb5edabc82ccf760b4ad1e29",
    "249cec6cc0daeb14e340af88f39a8d2b56799fe7",
    "c60266a8adad2f8ee67d793b4fd3fd0ffd73cc61",
    "d3bd1eb71f1f14f75f7e71cdad5fe0f5ade07f52",
    "fdddbaa4a5451f116b1dd3dd1289a04e50e968bc",
    "edcaef342de393ea82accad611d1c1b4242d2b36",
    "e97ba6aed5561a3d7fa95bc8f799387219d9c1e7",
    "e660ef2f99888ce5e7e2884d4193540d2b1fd0b4",
    "5ae8db5b72c7e3536f259a005b63117cbbca0505",
    "47265105ec5517e46aec2ed5310c177e1e811af8",
    "680254bad1d7ca0d65ec46aaa315d363abf6a50a",
    "f3ac5f0709efe8be7fccedc4955eb354dce78d24",
    "fb10549407078744164d6102c809ccd50cc87de8",
    "e85e7aea15b160d4c482e06f253752bd77d8ef8e",
    "7d65c1633ac5383c94fb21b067fdf30aa10bc1fe",
    "31216940d23924a5761bff2a101893cfccfc625d",
    "7994ebae30a63934992a16deca856d50596bc1a9",
    "4504274f6214a3c420396e17ce5edf044344baf1",
    "4fb2f4c43c90a51b4cafec65661c7274e45b770c",
    "1b8cb242f7e28133bae0adefa873aa170486cb42",
]


def get_strcmp_rval():
    result = ""
    for i in range(20):
        result += hashes[i][2 * i : 2 * i + 2]
    print(result)


if __name__ == "__main__":
    get_strcmp_rval()
