from encoder import encode 

# Test Vector 1
INPUT_1 = {
    "null": None,
    "octets": bytes([1, 2, 3]),
    "integer": 12345
}

EXPECTED_1 = [
    0x03,                   # Dictionary with 3 items
    0x04, 0x6E, 0x75, 0x6C, 0x6C,         # "null"
    0x00,                   # Empty sequence
    0x06, 0x6F, 0x63, 0x74, 0x65, 0x74, 0x73,  # "octets"
    0x03, 0x01, 0x02, 0x03, # Byte sequence length 3
    0x07, 0x69, 0x6E, 0x74, 0x65, 0x67, 0x65, 0x72,  # "integer"
    0x39, 0x30             # 12345 in little-endian
]

output_1 = encode(INPUT_1)
assert output_1 == EXPECTED_1, f"Test Vector 1 failed! {output_1}"

# Test Vector 2
INPUT_2 = {
    "outer": {
        "inner": [1, 2, 3],
        "value": 42
    }
}

EXPECTED_2 = [
    0x01,                   # Dictionary with 1 item
    0x05, 0x6F, 0x75, 0x74, 0x65,   # "outer"
    0x02,                   # Dictionary with 2 items
    0x05, 0x69, 0x6E, 0x6E, 0x65,   # "inner"
    0x03, 0x01, 0x02, 0x03, # Array [1, 2, 3]
    0x05, 0x76, 0x61, 0x6C, 0x75, 0x65,   # "value"
    0x2A                    # 42
]

output_2 = encode(INPUT_2)
assert output_2 == EXPECTED_2, f"Test Vector 2 failed! {output_2}"
