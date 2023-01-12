dic = {
    484 : "Aniket",
    472 : "Neeraj",
    138: "Sourav",
    468: "Daya"
}

print(dic)
print(dic[138]) # Throws error if key is not present in dict
print(dic.get(139))

for keys in dic.keys() :
    print(keys)

for val in dic.values():
    print(val)

for key,value in dic.items():
    print(key, value)

# After 3.7 version onwards dic are ordered