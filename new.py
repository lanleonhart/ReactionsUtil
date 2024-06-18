import requests

# Data Model:
# "Item": [ID, Graphene, Methanofullerene, PPD, Fullerene, C3-FTM]

'''
Fullerite-C32	352	Harvestable Cloud		1,760 m3	7,373,495.36 ISK
Fullerite-C50	960	Harvestable Cloud			960 m3
Fullerite-C60	2,760	Harvestable Cloud		2,760 m3	11,946,163.20 ISK
'''

items = {
	"Hydrogen Fuel Block": [4246, 0, 5, 5, 5, 0],
	"Nitrogen Fuel Block": [4051, 5, 0, 0, 0, 0],
	"Helium Fuel Block": [4247, 0, 0, 0, 0, 5],
	"Nocxium": [38, 400, 0, 0, 0, 0],
	"Isogen": [37, 0, 300, 0, 0, 0],
	"Pyerite": [35, 0, 0, 800, 0, 0],
	"Mexallon": [36, 0, 0, 0, 600, 0],
	"Megacyte": [40, 0, 0, 0, 0, 80],
	"Fullerite-C28": [30375, 100, 0, 0, 0, 0],
	"Fullerite-C32": [30376, 100, 0, 0, 0, 0],
	"Fullerite-C50": [30370, 0, 0, 300, 0, 0],
	"Fullerite-C60": [30371, 0, 0, 100, 100, 0],
	"Fullerite-C70": [30372, 0, 100, 0, 100, 0],
	"Fullerite-C72": [30373, 0, 100, 0, 0, 0],
	"Fullerite-C84": [30374, 0, 0, 0, 0, 100],
	"Fullerite-C540": [30378, 0, 0, 0, 0, 100],
}

reactions = [
	"Graphene Nanoribbons",
	"Methanofullerene",
	"PPD Fullerene Fibers",
	"Fullerene Intercalated Graphite",
	"C3-FTM Acid",
]

ids = []
for item in items:
	ids.append(str(items[item][0]))

market = requests.get(f"https://market.fuzzwork.co.uk/aggregates/?region=30000142&types={','.join(ids)}").json()

def get_item_total(name, qty):
	if name not in items:
		return 0
	item_id = items[name][0]
	price = float(market[str(item_id)]['sell']['weightedAverage'])
	return price * int(qty.replace(',',''))

input_data = []
print("Paste your inventory from your hangar, hit enter twice to continue...")
while True:
	line = input()
	if line == '':
		break
	input_data.append(line)

stock = {}
for d in input_data:
	item = d.split('\t')
	if item[0] in items:
		stock[item[0]] = item[1]

for s in stock:
	resp = "{0} x {1}: {2:,.2f}".format(stock[s], s, get_item_total(s, stock[s]))
	print(resp)