# INPUT
phrase = input("Enter greetings from your state : ")
state = input("From which FSM state : ")
times = int(input("How many times? "))

print("No. Greetings"," "*20,"State")
print("-"*45)
for num in range(times):
    print("%3d" % (num+1),"%-30s" % phrase, "%-10s" % state)