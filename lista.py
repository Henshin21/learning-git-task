shopping_list = {
    "Lidl": ["pierogi","spaghetti","sos boloński","mięso mielone","ser"],
    "Intermarche": ["drogi chleb","drogi papier","drogie chipsy"],
    "Chińczyk": ["tanie spodnie","tani gadżet"],
    "Rossman": ["drogie nie moje kosmetyki","tani szampon 3 w 1"]
}
item_count = 0
for shop, products in shopping_list.items():
    print(F"Idę do {shop.capitalize()} i kupuję {[food.capitalize() for food in products]}")
    item_count += len(products)
print(f"W sumie kupuję {item_count} rzeczy")