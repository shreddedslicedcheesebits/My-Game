from opening import interaction
def interact(current,inventory):
	if current == (0, 0, 0):
		if "Broken Bottle" not in inventory:
			inventory.append("Broken Bottle")
			print("\"Broken Bottle\" added to inventory")
			interaction()
	elif current == (1,0,0):
		if "Shiny Coin" not in inventory:
			inventory.append("Shiny Coin")
			print("\"Shiny Coin\" added to inventory")
			interaction()
	return inventory
