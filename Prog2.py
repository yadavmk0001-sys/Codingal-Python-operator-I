Amount = int(input("Enter the amount for withdrawal : "))

n1 = Amount//100
n2 = (Amount%100)//50
n3 = ((Amount%100)%50)//10

print("Notes of 100 rupee : ", n1)
print("Notes of 50 rupee : ", n2)
print("Notes of 10 rupee : ", n3)