from cvOPEN import open_image

class Main():
    def __init__(self):
        img = open_image("images/1.jpg",is_show=True)

    def run(self):
        while True:
            pass

if __name__ == '__main__':
    app = Main()
    app.run()