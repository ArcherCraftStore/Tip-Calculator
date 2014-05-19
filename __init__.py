meal = raw_input("Meal")
tax = raw_input("Tax")
tip = raw_input("Tip")

meal = meal + meal * tax

total = meal + meal * tip
print("%.2f" % total)
