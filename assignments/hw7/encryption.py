def encode_better(message, key):
    length_key = len(key)
    length_message = len(message)
    encoded_message = ""
    for i in range(length_message):
        letter_message = message[i]
        key_number = i % length_key
        letter_key = key[key_number]
        encoded_letter_message = ord(letter_message) - 65
        encoded_letter_key = ord(letter_key) - 65
        combined_encoding = encoded_letter_key + encoded_letter_message
        encode_moved = (combined_encoding % 58) + 65
        decoded_ = chr(encode_moved)
        encoded_message = encoded_message + decoded_
    return encoded_message


def encode(message_, key_):
    length_ = len(message_)
    encoded_message = ""
    for i in range(length_):
        letter = message_[i]
        encode_ = ord(letter) + key_
        decode_ = chr(encode_)
        encoded_message = encoded_message + decode_
    return encoded_message
