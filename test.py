def test(pas):
    for i in range(5,-1,-1):
        print(i,pas)

class test1():

    def __init__(self) -> None:
        test("coucou")


class test2():

    def __init__(self) -> None:
        test("hello")
        self.hello = "hello"

    def hello():
        print("helo")


testpiece = test1()
testpiece = test2()

print(8%2)
print(8//2)


if testpiece or testpiece==0:
    print("yes")
else:
    print("no")

testpiece = 0

if testpiece==0 or testpiece.hello:
    print("yes")
else:
    print("no")



for x,y in [(5,10),(81,555),(58,23)]:
    print(x,y)