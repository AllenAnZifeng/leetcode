"""

"""
def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val
#
# def flippedBits(num1, num2):
#     # Write your code here
#     flag = 0
#     if (num1 < 0 and num2 >=0) or (num1 >= 0 and num2 < 0):
#         flag = 1
#
#
#     # turn num1 into binary
#     num1 = bin(num1)[2:]
#     # turn num2 into binary
#     num2 = bin(num2)[2:]
#
#     print(num1)
#     print(num2)
#
#     if len(num1) > len(num2):
#         num2 = '0' * (len(num1) - len(num2)) + num2
#     # if num2 is longer than num1, add 0s to the front of num1
#     elif len(num2) > len(num1):
#         num1 = '0' * (len(num2) - len(num1)) + num1
#     # if num1 and num2 are the same length, do nothing
#     else:
#         pass
#
#
#
#
#     c = 0
#     for i in range(len(num1)):
#         if num1[i] == num2[i]:
#             pass
#         else:
#             c +=1
#
#     return c + flag


def flippedBits(num1, num2):

    if num1 == num2:
        return 0

    # Define the width of the binary representation
    width = max(num1.bit_length(), num2.bit_length()) + 1  # add 1 for sign bit

    # If number is negative, compute two's complement, else just convert to binary
    num1_bin = format(num1 & ((1 << width) - 1), f'0{width}b') if num1 < 0 else format(num1, f'0{width}b')
    num2_bin = format(num2 & ((1 << width) - 1), f'0{width}b') if num2 < 0 else format(num2, f'0{width}b')

    # print(num1_bin)
    # print(num2_bin)

    # Count the differing bits
    count = sum(el1 != el2 for el1, el2 in zip(num1_bin, num2_bin))

    return count
def main():
    # input for num1
    # num1 = int(input())
    num1 = 8
    # input for num2
    # num2 = int(input())
    num2 = -1
    result = flippedBits(num1, num2)
    print(result)
    # print(bin(twos_complement(-7, 32)))
    # print(bin(twos_complement(7, 32)))


if __name__ == "__main__":
    main()