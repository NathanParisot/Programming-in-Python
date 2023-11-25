menu_item = "Menu item: pizza"
guests = 20
number_of_guest = "Number of guests"
print(menu_item)
print(number_of_guest)
print(guests)
menu_item = "biryani and "
menu_item2 = "cookies" 
print("Updated menu item is: " + menu_item + menu_item2)
cookies_per_person = 3
cookies_needed = cookies_per_person * guests
cookies_bought = 45
enough_cookies = cookies_per_person == cookies_bought
cookies_per_guest = cookies_bought / guests
biryani_per_person = 1
biryani_needed = biryani_per_person * guests
biryani_prepared = 10
enough_biryani = biryani_prepared == biryani_needed
biryani_per_guest = biryani_prepared / guests
print("Biryani per guest")
print(biryani_per_guest)
print("Cookies per guest")
print(cookies_per_guest)