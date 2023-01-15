from student_account import StudentAccount

customer = StudentAccount("Andrew", 1000)

print("initial amount", customer.check_balance())

customer.withdraw_funds(10)
print("amount after funds are withdrawn", customer.check_balance())
