"""
def cidr_to_bin_dec(a, b, c):  # CIDR to binary/decimal function
    cidr_block = ""
    output_bin = ""
    output_dec = ""
    network_address_bin = "10101010.10101010.10101010.10101010"
    i = a
    i2 = 0

    while i != 0:
        cidr_block += "1"
        i2 += 1
        i -= 1
        if i2 == 8:
            output_bin += cidr_block
            output_bin += "."
            output_dec += str((int(cidr_block, 2)))
            output_dec += "."
            cidr_block = ""
            i2 = 0

    i = 32 - a

    while i != 0:
        cidr_block += "0"
        i2 += 1
        i -= 1
        if i2 == 8:
            output_bin += cidr_block
            output_bin += "."
            output_dec += str((int(cidr_block, 2)))
            output_dec += "."
            cidr_block = ""
            i2 = 0

    output_dec = output_dec[:-1]
    output_bin = output_bin[:-1]
    if c == 1:  # Full output (for UI)
        print('')
        print('The binary notation is:')
        print(output_bin)
        print('The decimal notation is:')
        print(output_dec)
        print("")
        print("The maximum number of hosts for the network/host address", network_address, "is :")
        print("")
        maximum_hosts(cidr)
        output_dec = output_dec[:cidr + 2] + '|' + output_dec[cidr + 2:]
        print(output_dec)
        print(network_address_bin)
        print("")
    elif c == 2:  # Binary output (for others functions)
            print(output_bin)
"""


def cidr_to_bin(mask_cidr):
    i = mask_cidr
    mask_bin = []
    block = ""
    i2 = 0
    while i != 0:
        if i2 == 8:
            mask_bin.append(block)
            block = ""
            i2 = 0
        block += "1"
        i2 += 1
        i -= 1
    i = 32 - mask_cidr
    while i != -1:
        if i2 == 8:
            mask_bin.append(block)
            block = ""
            i2 = 0
        block += "0"
        i2 += 1
        i -= 1
    return mask_bin


def dec_to_cidr(dec_input):
    bin_output = []
    dec_input = dec_input.split('.')
    for i, item in enumerate(dec_input):
        bin_output.append(bin(int(dec_input[i])))

    return bin_output


def maximum_hosts(cidr_input):
    return (2 ** (32 - cidr_input)) - 2


dec_to_cidr("255.255.255.0")

choice = 0
while not 1 <= choice <= 3:
    print("")
    print("To convert a CIDR mask to decimal notation, type 1:")
    print("To convert network mask with decimal notation to CIDR, type 2:")
    print("Type 3 for exit")
    choice = input()
    choice = int(choice)
if choice == 3:
    exit()
else:
    if choice == 1:
        print("")
        print("Please type your a CIDR number :")
        cidr = input()
        cidr = int(cidr)
        print("")
        while cidr > 32:
            print("Please enter CIDR between 1 & 32 :")
            cidr = input()
            cidr = int(cidr)
        mask = ""
        for i, item in enumerate(cidr_to_bin(cidr)):
            mask += str(int(cidr_to_bin(cidr)[i], 2)) + "."
        mask = mask[:-1]
        print("The decimal notation is:")
        print(mask)
        print("")
        print("You can have a maximum of", maximum_hosts(cidr), "hosts.")
    elif choice == 2:
        dec_to_cidr("255.255.255.0")


# A1: Depends if the function is call for an UI output (1) or a function output (2).
#     The last parameter tells what to do.
