from prettytable import PrettyTable

beer_chart = PrettyTable()

beer_chart.field_names = ["Beer Name", "Calories", "ABV", "6pack/12pack", "Price", "Score", "Store", "Beer Type"]
beer_chart.add_row(["Modelo", "144", "4.4%", "12pack", "$15.99", "", "Smart&Final", "Mexican Lager"])

print(beer_chart)