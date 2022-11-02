#!/usr/bin/python3

total = 13 + 14.02 + 22.35

party = 3

print('Receipt for your meal')
if party >= 8:
	total = total + total * .2
	print('We have added the tip automatically, since your party was eight or larger')
print('Total:', total)
print('Thank your for dining with us today')
