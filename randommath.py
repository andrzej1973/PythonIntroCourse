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

print('\n\n')

for index in range(loopMax):
    number1=random.randint(-99,99)
    number2=random.randint(-99,99)
    operator=operations[random.randint(0,len(operations)-1)]
    result=calculator.ExecuteOperation(operator, number1, number2,1)
    print("iteration:",index,"number1=", number1, "number2=", number2, "operator=", operator, "result=", result)
    print('\n')

dictionaryOfThinks={};

shadesOfBlue=["lightblue","blue","darkblue"]

dictionaryOfThinks['Apple']="Tasty fruit, which is nice to eat"
dictionaryOfThinks['Banana']="Yellow fruit"
dictionaryOfThinks[3]="Number bigger then 2 and smaller then 4"
dictionaryOfThinks['Blue']=shadesOfBlue

for idx in dictionaryOfThinks:
    print("idx:",idx,'\n',"Dictionary Item:",dictionaryOfThinks[idx],'\n')
