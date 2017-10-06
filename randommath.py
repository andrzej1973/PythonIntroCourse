import datetime
import time
import random
import calculator


print("went to sleep at...",datetime.datetime.now())
time.sleep(1)
print("woken up at...",datetime.datetime.now())


print("random number:",random.randint(1,10))

operations = ["+","-","*"]

operations.append("/")

loopMax=random.randint(1,50)

print("Beginning mathing sequence of", loopMax, "calculations.")

for index in range(loopMax):
    number1=random.randint(-99,99)
    number2=random.randint(-99,99)
    operator=operations[random.randint(0,len(operations)-1)]
    result=calculator.ExecuteOperation(operator, number1, number2)
    print("iteration:",index,"number1=", number1, "number2=", number2, "operator=", operator, "result=", result)

#calculator.main()