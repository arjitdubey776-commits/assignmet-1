salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))

if salary >= 25000 and credit_score >= 650:
    print("Loan approved")
elif salary >= 25000 or credit_score >= 650:
    print("Loan conditionally approved")
else:
    print("Loan rejected")
