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


def dec_to_bin(dec_input):
    bin_output = []
    dec_list = dec_input.split('.')
    for i, item in enumerate(dec_list):
        bin_output.append(bin(int(dec_list[i])))
    return bin_output


def bin_to_cidr(bin_input):
    return str(bin_input).count("1")


def maximum_hosts(cidr_input):
    return (2 ** (32 - cidr_input)) - 2


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
        print("")
        print("Please enter your decimal network mask: (ex.: 255.255.255.0 / 255.255.255.252")
        dec_mask = input()
        print("")
        print("The CIDR notation is:")
        print(bin_to_cidr(dec_to_bin(dec_mask)))
        print("")
        print("You can have a maximum of", maximum_hosts(bin_to_cidr(dec_to_bin(dec_mask))), "hosts.")
