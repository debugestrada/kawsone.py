import requests
import time
from random import getrandbits

def main():
	try:
		for i in range(1,1000):
			#Use gmail for the + trick to work
			email = 'moneycats323+{}@gmail.com'.format(getrandbits(40))
			payload = {"mailinglist_email": email}
			response = requests.post('http://kawsone.com/', data=payload)
			print('{}/1000: Registered. Good luck fam! '.format(i))

			time.sleep(10)


	except Exception as e:
		raise e

if __name__ == "__main__":
    main()
