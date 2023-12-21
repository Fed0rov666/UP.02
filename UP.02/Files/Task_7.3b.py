mac_table = []

with open("CAM_table.txt") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, type, interface = words
            mac_table.append([int(vlan), mac, interface])
v = int (input('Enter VLAN number:'))

for vlan, mac, interface in sorted(mac_table):
    if v == vlan:
        print(f"{vlan:9}{mac:20}{interface}")