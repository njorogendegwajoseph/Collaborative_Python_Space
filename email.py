#!/usr/bin/python3

email = input('Enter the email content: ')
if 'emergency' in email:
	print("Do you want to make this email urgent?")
elif 'joke' in email:
	print("Do you want to set this email as non-urgent?") 


"""if email.find('emergency') == True:
	print("Do you want to make this email urgent?")
elif:
	email.find('joke') == True
	print("Do you want to set this email as non-urgent?")"""
