import rumps

class applejobs(object):
    def __init__(self):
        self.app = rumps.App("Apple Jobs", " Jobs")

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = applejobs()
    app.run()
