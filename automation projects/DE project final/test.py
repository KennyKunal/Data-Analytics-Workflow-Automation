data = ['Amul Taaza Homogenised Toned Milk 1 L Carton', '1 l', '₹77.00', 'Amul Taaza Homogenized toned Milk, 200 ml', '200 ml', '₹17.00', 'Amul Moti Homogenized Toned Milk, 450 Ml Pouch', '450 ml', '₹32.00', 'Amul Gold Milk Homogenized Standardized, 1 Litre Carton', '1 l', '₹83.00', 'Amul Lactose Free Milk, 250 Ml', '250 ml', '₹26.00', 'Amul Milk - Gold,1 L Pouch', '1 l', '₹72.00', 'Amul Fresh Cream, 250ml Tetra Pack', '250 ml', '₹75.00', 'Dabur Hommade Coconut Milk- Goodness of 2 Creamy Coconuts-200 ml', '200 ml', '₹80.00', "Amul Slim 'N' Trim Skimmed Milk, 1 Litre", '1 l', '₹85.00', "D'lecta Dairy Cream - 200ml", '200 ml', '₹61.75', 'Heritage FARM FRESH TONED UHT MILK 1LTR TETRA', '1 l', '₹72.00', 'Mother Dairy Uht Milk Carton, 1 Liter', '1 l', '₹77.00', 'A+ Toned Milk, 1L, Tetra Pack., Liquid', '1 l', '₹107.00', 'A+ Slim Skimmed Milk, 1L, Tetra Pack., Liquid', '1 l', '₹94.00', 'Heritage LITE FIT UHT MILK 1LTR TETRA', '1 l', '₹70.00', "D'Lecta milke-Condensed-Partly-skimmed-Milk 20 Pcs Carton", '200 ml', '₹110.00', 'Amul Whipping Cream, 250 ml', '250 ml', '₹100.00', 'Milky Mist Sweetend Condensed Milk, 200GM', '200 g', '₹50.00', 'Bagrrys Plant Based Almond Drink, Unsweetned 1l | Vegan | Gluten Free| Dairy free | No Added Sugar| Plant based milk | No Preservatives', '1 l', '₹229.00', 'Milky Mist Uht Milk Cream, 250 g Tetra Pack', '250 g', '₹80.00', "D'lecta Dairy-Free Whipping Cream 1 Kg", '1 kg', '₹189.00', 'Akshayakalpa Organic Slim Milk (UHT), Pure antibiotic-free milk, low calorie, low fat, long shelf life, No chemical residues, convenient and ready-to-use, nutritious by nature, 1 Ltr', '1 l', '₹145.00', 'Mother Dairy Cream, 200ml', '200 ml', '₹63.00', "D'lecta Dairy Cream - 1 LTR", '1 l', '₹290.00', 'Mother Dairy UHT Fit Lite ESL Milk, 450ml', '450 ml', '₹32.00', 'Akshayakalpa Organic Cow Milk (Uht), Pure Antibiotic- Free Milk, Long Shelf Life, No Chemical Residues, Convenient And Ready-To-Use, Nutritious By Nature, 200Ml.', '200 ml', '₹31.00', 'Amul Fresh Cream, 1 Litre', '1 l', '₹250.00', 'Akshayakalpa Organic Slim Milk (Uht), Pure Antibiotic-Free Milk, Low Calorie, Low Fat, Long Shelf Life, No Chemical Residues, Convenient And Ready-To-Use, Nutritious By Nature, 200Ml', '200 ml', '₹36.00', 'Milky Mist Sweetend Condensed Milk, 395gm', '400 g', '₹95.00', 'Mooz Sour Cream-Mooz, 150 g', '150 g', '₹210.00', 'Milky Mist UHT Milk Cream Pouch, 1 L', '₹305.00', 'Milky Mist Toned Milk (UHT) Pouch, 1 L', '1 l', '₹90.00', 'Amul Taaza Homogenized Toned Milk, 500 Ml', '500 ml', '₹40.00']
# products = [
#     {
#         "name": data[i],
#         "quantity": data[i + 1],
#         "price": data[i + 2]
#     }
#     for i in range(0, len(data), 3)
# ]
products = []
i = 0

while i < len(data):
    # Product name
    name = data[i]
    i += 1

    # Quantity
    if i < len(data) and not data[i].startswith("₹"):
        quantity = data[i]
        i += 1
    else:
        quantity = "N/A"

    # Price
    if i < len(data) and data[i].startswith("₹"):
        price = data[i]
        i += 1
    else:
        price = "N/A"

    products.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })

# for p in products:
#     print(p)
print(products)
print(len(data))
# print(len(fixed))
