#Demonstrate the working of MD5 (byte-byte)  
  
import hashlib  
  
#encoding TYCSSTUDENTS using md5 hash fucntion  
  
result = hashlib.md5(b'TYCSSTUDENTS')  
  
#print the equivalent byte value.  
  
print("The byte equivalent of hash is :",end="")  
  
print(result.digest())  
  
str2hash = "TYCSSTUDENTS"  
  
#Encoding TYCSSTUDENTS using encode()  
  
#then sending to md5()  
  
result = hashlib.md5(str2hash.encode())  
  
#printing the equivalent hexadecdimal value  
  
print("The hexadecimal equivalent of hash is :",end = "")  
  
print(result.hexdigest()) 
