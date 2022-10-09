class Pycharm:
    def execute(self):
        print("compiling and running")

class MyEditor:
    def execute(self):
        print("compiling and running and many things")

class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()

lap1.code(ide)


