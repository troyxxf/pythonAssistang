shuru = input() 
GDP = {}
while shuru!="ok":
    name , gdp = shuru.split()[0], eval(shuru.split()[1])
    GDP[name] = gdp
    shuru = input()
