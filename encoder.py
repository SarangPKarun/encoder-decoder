def encode_string(s):
    # Convert the string to its hexadecimal representation
    encoded = [f"0x{len(s):02x}"]
    encoded.extend([hex(ord(char)) for char in s])
    return encoded

def encode_bytes(b):
    encoded = [f"0x{len(b):02x}"]
    encoded.extend([f"0x{byte:02x}" for byte in b])

    return encoded

def encode_list(l):
    encoded = [f"0x{len(l):02x}"]
    encoded.extend([f"0x{i:02x}" for i in l])
    return encoded

def encode_integer(i):
    num_bytes = (i.bit_length() + 7) // 8  # This ensures the right byte length
    little_endian = i.to_bytes(num_bytes, byteorder='little')
    encoded = [f"0x{byte:02x}" for byte in little_endian]
    return encoded

def encode_dictionary(d):
    encoded = []
    encoded.extend([f"0x{len(d):02x}"])
    for key, value in d.items():
            # Encode the key
            if key is None:
                encoded.extend(f"0x{0:02x}")  # Empty sequence for None
            elif isinstance(key, bytes):
                encoded.extend(encode_bytes(key))
            elif isinstance(key, int):
                encoded.extend(encode_integer(key))
            elif isinstance(key, str):
                encoded.extend(encode_string(key))
            elif isinstance(key, dict):
                encoded.extend(encode_dictionary(key))
            elif isinstance(key, list):
                encoded.extend(encode_list(key))
            
            # Encode the value based on its type
            if value is None:
                encoded.extend(f"0x{0:02x}")  # Empty sequence for None
            elif isinstance(value, bytes):
                encoded.extend(encode_bytes(value))
            elif isinstance(value, int):
                encoded.extend(encode_integer(value))
            elif isinstance(value, str):
                encoded.extend(encode_string(value))
            elif isinstance(value, dict):
                encoded.extend(encode_dictionary(value))
            elif isinstance(value, list):
                encoded.extend(encode_list(value))
    return encoded

def encode_data(input_data):
    encoded = []

    # Check if the input is a dictionary
    if isinstance(input_data, dict):
        encoded.extend(encode_dictionary(input_data))
    elif input_data is None:
        encoded.append(f"0x{0:02x}")  # Empty sequence for None
    elif isinstance(input_data, bytes):
        encoded.extend(encode_bytes(input_data))
    elif isinstance(input_data, int):
        encoded.extend(encode_integer(input_data))
    elif isinstance(input_data, str):
        encoded.extend(encode_string(input_data))
    elif isinstance(input_data, list):
        encoded.extend(encode_list(input_data))

    return encoded


INPUT_2 = {
    "outer": {
        "inner": [1, 2, 3],
        "value": 42
    }
}

INPUT_3 = 18446744073709551615

print(type(encode_data(INPUT_3)[0]))