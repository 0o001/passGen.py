#!/usr/bin/env python
import random
import string


__author__ = 'mustafauzun0'

'''                                  
 _ __   __ _ ___ ___  __ _  ___ _ __  
| '_ \ / _` / __/ __|/ _` |/ _ \ '_ \ 
| |_) | (_| \__ \__ \ (_| |  __/ | | |
| .__/ \__,_|___/___/\__, |\___|_| |_|
| |                   __/ |           
|_|                  |___/            

'''

def main():
    password = ''

    for _ in range(random.randint(8, 18)):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    print('Generated Password: ' + password)
    

    
if __name__ == '__main__':
	main()
