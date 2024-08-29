# elif is better to use for write simple code
A = float(input(" Enter Arjun's Age"))
W = float(input(" Enter Wasim's Age"))
R = float(input(" Enter Rihan's Age"))
if A > W and A > R:
    print(" Arjun is Eldest ")
elif W > R and W > A:
    print("Wasim is Eldest")
else:
    print("Rihan is Eldest")