from view.preload_predictor_app import App

class Main:
    @staticmethod
    def run():
        try:
            app = App()
            app.mainloop()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()