with open("CAM_table.txt") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, type, interface = words
            print(f"{vlan:9}{mac:20}{interface}")