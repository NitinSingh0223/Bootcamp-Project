#PROGRAM TO GENERATE HASH OF STRING USING 3 ALGORITHMS
import hashlib

# encode it to bytes
message = "PYTHON IS FUN".encode()


# hash with MD5 
print("MD5:", hashlib.md5(message).hexdigest(),"\n")


# hash with SHA-1
print("SHA-1:", hashlib.sha1(message).hexdigest(),"\n")


# hash with SHA-2 (SHA-256 & SHA-512)
print("SHA-256:", hashlib.sha256(message).hexdigest(),"\n")

print("SHA-512:", hashlib.sha512(message).hexdigest(),"\n")


#SOME OTHERVALGORITHMS ARE GIVEN BELOW
# hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest(),"\n")

print("SHA-3-512:", hashlib.sha3_512(message),"\n")


# hash with BLAKE2
# 256-bit BLAKE2 (or BLAKE2s)
print("BLAKE2c:", hashlib.blake2s(message).hexdigest(),"\n")

# 512-bit BLAKE2 (or BLAKE2b)
print("BLAKE2b:", hashlib.blake2b(message).hexdigest(),"\n")

print("\n\n************PROGRAM IS COMPLETE************\n")