def cidr_to_bin_dec(a, b, c): # CIDR to binary/decimal function
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


def dec_to_cidr(decimal_input):
    i = 0
    block = ""




def dec_to_bin(dec_input):
    i = 1
    blocks = dec_input.split(".")
    bin_output = ""
    for i, elem in enumerate(blocks):
        elem = int(elem)
        bin_output += bin(elem)
        #"{0:#b}".format(blocks)
        #bin_ouput =+ "{0:b}".format(elem)
        i += 1
    bin_output = bin_output[:-1]
    print(bin_ouput)

def maximum_hosts(a):
    print((2 ** (32 - a)) - 2)


dec_to_bin('192.168.1.0')

choice = 0
while not 1 <= choice <= 3:
    print("")
    print("To convert CIDR to DEC/BIN, type 1 :")
    print("To convert Network Mask to CIDR, type 2 :")
    print("Type 3 for exit")
    choice = input()
    choice = int(choice)
if choice == 3:
    exit()
else:
    if choice == 1:
        print("")
        print("Please type your CIDR number :")
        cidr = input()
        cidr = int(cidr)
        print("")
        print("Please type your Network address or machine address (or leave it empty)")
        print("Ex. : 192.168.1.0 / 172.16.3.254 :")
        network_address = input()
        network_address = str(network_address)
        while cidr > 32:
            print("Please enter CIDR between 1 & 32 :")
            cidr = input()
            cidr = int(cidr)
        cidr_to_bin_dec(cidr, network_address, 1)  # The last parameter, tells what kind of output we want (cf. A1).
    else:
        print("TO DO")

# A1: Depends if the function is call for an UI output (1) or a function output (2).
#     The last parameter tells what to do.

