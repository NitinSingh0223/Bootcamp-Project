#Program to generate MD5 hash of a string
import hashlib

def hashing(string):
	hash = hashlib.md5(string.encode())
	#encode() : Converts the string into bytes to be acceptable by hash function.
	
	print("Byte equivalent of hash is : ", end ="") 
	print(hash.digest())
	#digest() : Returns the encoded data in byte format.
	
	print("The hexadecimal equivalent of hash is : ", end ="") 

	print(hash.hexdigest())
	#hexdigest() : Returns the encoded data in hexadecimal format.

string = input("ENTER STRING TO GENERATE MD5 ============>\n")
hashing(string)
print("\n\n************PROGRAM IS COMPLETE************\n")
	