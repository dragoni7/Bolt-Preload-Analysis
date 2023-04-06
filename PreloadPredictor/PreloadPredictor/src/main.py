from view.preload_predictor_app import App
import sys
import setup

class Main:
    @staticmethod
    def run():
        try:
            setup.run()
            root = App()
            root.protocol("WM_DELETE_WINDOW", sys.exit)
            root.mainloop()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()