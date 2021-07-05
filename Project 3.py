#PROGRAM TO ADD SALTING AND ITERATION TO HASH

import hashlib

user_entered_password = input("ENTER STRING \n")
salt = "5gz"

#ADD SALTING
db_password = user_entered_password+salt
print("STRING TO BE SALT IS ===============>\n",db_password,"\n")
h = hashlib.md5(db_password.encode())
hash = h.hexdigest()
print("SALTED STRING HASHING IS===============> \n",hash,"\n")


#ADDING ITERATION
a= int(input("ENTER NO. OF ITERATION YOU WANT "))
for i in range(a):
	h = hashlib.md5(hash.encode())
	hash = h.hexdigest()

print("ITERATED STRING HASHING IS =========>\n")
print(hash,"\n\n\n")

print("**************PROGRAM IS COMPLETE***************")
