"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

ways = 1 

for one_pound in range(3): #0-2
	first_total = one_pound * 100
	for fifty_p in range(5): #0-4
		second_total = first_total + fifty_p * 50
		for twenty_p in range(11): #0-10
			third_total = second_total + twenty_p * 20
			for ten_p in range(21): #0-20
				fourth_total = third_total + ten_p * 10
				for five_p in range(41): 
					fifth_total = fourth_total + five_p * 5
					for one_p in range(201):
						sixth_total = fifth_total + one_p
						if sixth_total == 200:
							ways += 1
							break
print(ways)


#Attempt 2

for i in range(200, 0, -200):
	print(i)
