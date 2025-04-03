from utils import *

def model_fn(task, data, model= 'yolov8n.pt', conf= 0.5):
    subprocess.run([
        "yolo", 
        f"task={task}", 
        "mode=predict", 
        f"model={model}", 
        f"conf={conf}", 
        f'source={data}', 
        "save=True"
    ], check= True)