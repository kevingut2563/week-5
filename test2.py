newphrase = "rainstorm"
            #012345678
            #123456789 -- in collegeboard
#create a variable called shortphrase
# abd assign it a value by slicing 
#the newphrase variab;e by removing the first 3 letters 
#and the last three characters 
#substring(string,start, end)

shortphrase = newphrase[3:len(newphrase)]

#collage board version [4:len(newphrase)-6]

print(shortphrase)
#explain len(newphrase)-3 = 9-3=6
#why does it end with 6 
#because the last index is not included