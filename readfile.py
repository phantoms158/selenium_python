r = open("data.txt", "r")
#print(r.read())
for result in r:
    #print(result)
# result = r.read()
# username = 
    result = result.strip()
    arr = result.split(" ")
    username = arr[0]
    password = arr[1]
    print (username, password)