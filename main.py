# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class TestApp:
    def __init__(self):
        self.name = "Fedor"
        self.surname = "Maziev"
        self.thirdname = "Sergeevich"

    def print_name(self) -> None:
        print(self.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = TestApp()
    app.print_name()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
