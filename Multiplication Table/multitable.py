print("\t\t\t\tMultiplication Tables\n")

for i in range(1, 11):
    print(i, end="\t")
print()
print("_____________________________________________________________________________\n")
for j in range (1, 11):
    for k in range(1, 11):
        print(j*k, end = "\t")
    print("\n")
