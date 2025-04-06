from webapp import *

subprocess.run(["pip", "install", "./assets/ultralytics"], check= True)

if __name__ == "__main__":
    webapp_fn()