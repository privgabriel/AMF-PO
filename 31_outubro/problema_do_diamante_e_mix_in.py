class A:
    def m1(self):
        print("Método de A")

class B(A):

    def m1(self):
        super().m1()

    def m2(self):
        print("Método de B")

class C(A):

    def m1(self):
        super().m1()

    def m2(self):
        print("Método de C")

class D(B, C):

    def m1(self):
        super().m1()

    def m2(self):
        super().m2()

if __name__ == "__main__":
    d = D()
    print("Saida:\n")
    d.m1()
    d.m2()