def cidr_to_bin_dec(a, b):
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
            output_dec += cidr_block
            output_dec += "."
            output_bin += str((int(cidr_block, 2)))
            output_bin += "."
            cidr_block = ""
            i2 = 0

    i = 32 - a

    while i != 0:
        cidr_block += "0"
        i2 += 1
        i -= 1
        if i2 == 8:
            output_dec += cidr_block
            output_dec += "."
            output_bin += str((int(cidr_block, 2)))
            output_bin += "."
            cidr_block = ""
            i2 = 0

    output_dec = output_dec[:-1]
    output_bin = output_bin[:-1]
    print('')
    print('La notation décimale est :')
    print(output_bin)
    print('La notation binaire est:')
    print(output_dec)
    print("")
    print("The maximum number of machines for the network/machine address", network_address, "is :")
    maximum_hosts(cidr)
    output_dec = output_dec[:cidr + 2] + '|' + output_dec[cidr + 2:]
    print(output_dec)
    print(network_address_bin)
    print("")


def dec_to_cidr(a):
    print("")


def maximum_hosts(a):
    print((2 ** (32 - a)) - 2)


choice = 0
while not 1 <= choice <= 3:
    print("")
    print("To convert CIDR to DEC/BIN, type 1 :")
    print("To convert Network Address to CIDR, type 2 :")
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
        cidr_to_bin_dec(cidr, network_address)
    else:
        print("TO DO")
