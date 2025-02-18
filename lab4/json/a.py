import json

json_file = r"C:\Users\sabin\OneDrive\Desktop\PP2\lab4\json\data.json"

with open(json_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)


dn = []
speed = []
mtu = []

for data in json_data['imdata']:
    dn.append(data["l1PhysIf"]["attributes"]["dn"])
    speed.append(data["l1PhysIf"]["attributes"]["speed"])
    mtu.append(data["l1PhysIf"]["attributes"]["mtu"])


print("Interface Status")
print("=" * 100)
print(f"{'DN':<60} {'Description':<15} {'Speed':<10} {'MTU':<10}")
print("-" * 60, "-" * 15, "-" * 10, "-" * 10)


for i in range(len(dn)):
    print(f"{dn[i]:<60}  {speed[i]:<10} {mtu[i]:<10}")