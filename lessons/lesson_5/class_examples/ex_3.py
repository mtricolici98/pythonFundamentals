# Changing the key of an object in a dict

my_dict = {
    "brand": "Audi",
    "Year": 1991,
    "Price": 2000,
    "Currency": "EUR"
}
# Removes key "Price" from the dict and sets it's value into tmp_price
tmp_price = my_dict.pop("Price")
my_dict["Cost"] = tmp_price
print(my_dict)
