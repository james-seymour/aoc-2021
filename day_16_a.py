from re import A
from utils import read_aoc_input, flatten


def get_version(s):
    return int(s[:3], 2)

def get_type(s):
    return int(s[3:6], 2)

def get_length_type_id(s):
    return s[6]

def is_operator_packet(s):
    return get_type(s) != 4

def hex_to_bin(s):
    t = bin(int(s, 16))[2:]
    return (len(t) % 4) * "0" + t

version_sum = 0

def parse_literal_packet(s):
    global version_sum
    version = get_version(s)
    version_sum += version

def parse_zero_op(sub, len):
    if is_operator_packet(sub):
        pass
    else:
        parse_literal_packet(sub[:11])

def parse_one_op(s):
    num_sub_packets = int(s[7:18], 2)
    indicies = [i * 11 + 18 for i in range(num_sub_packets + 1)]
    for i, j in zip(indicies, indicies[1:]):
        sub_packet = s[i:j]
        if is_operator_packet(sub_packet):
            parse_operator_packet(sub_packet)
        else:
            parse_literal_packet(sub_packet)

def parse_operator_packet(s):
    global version_sum
    len_type_id = get_length_type_id(s)
    version_sum += get_version(s)

    if len_type_id == "0":
        total_len = int(s[7:22], 2)
        parse_zero_op(s[22:], total_len)

    if len_type_id == "1":
        print(s)
        parse_one_op(s)

def main():
    # print(hex_to_bin())
    parse_operator_packet(hex_to_bin("8A004A801A8002F478"))
    # print(version_sum)

    

main()


