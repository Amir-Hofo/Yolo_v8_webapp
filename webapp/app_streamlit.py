from predict import *

background_color= "#E6E6FA"

def webapp_fn():
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: {background_color} !important;
            }}
        </style>
    """, unsafe_allow_html= True)


    st.title("Yolo v8 Web App")
    st.markdown("[Visit my portfolio](https://amir-hofo.github.io/Portfolio/)")

    task_selection= st.selectbox("Choose your task", ["object detection", "segmentation",
                                                      "oriented bounding box", "classify",
                                                      "body position"])
    data_selection= st.selectbox("Choose your data type", ["image", "video"])

    if data_selection== "video":
        uploaded_file= st.file_uploader("Choose an video...", type= ["mp4", "mkv"])
    else:
        uploaded_file= st.file_uploader("Choose an image...", type= ["jpg", "jpeg", "png"])
    
    task_map= {"segmentation": 'segment',
                "object detection": 'detect',
                "oriented bounding box": 'obb', 
                "classify": 'classify',
                "body position": 'pose'}
    
    model_map= {"segmentation": '-seg',
                "object detection": '',
                "oriented bounding box": '-obb', 
                "classify": '-cls', 
                "body position": '-pose'}
    
    task= task_map[task_selection]
    model= f'assets/model/yolov8n{model_map[task_selection]}.pt'
    # task= 'segment' if task_selection== "segmentation" else "detect"
    # model= 'assets/model/yolov8n-seg.pt' if task_selection== "segmentation" else 'assets/model/yolov8n.pt'


    if uploaded_file:
        if os.path.exists('runs'): shutil.rmtree('runs')
        if os.path.exists('assets/uploads'): shutil.rmtree('assets/uploads')
        os.makedirs('assets/uploads', exist_ok= True)
        with open(f"assets/uploads/{uploaded_file.name}", "wb") as f: f.write(uploaded_file.getbuffer())
        data_format= 'png' if data_selection== 'image' else 'mp4'
        model_fn(task, f"assets/uploads/{uploaded_file.name}", model)

        if data_selection== 'image':
            image= Image.open(f'runs/{task}/predict/{uploaded_file.name}')
            st.image(image, caption= "Done.") #, use_container_width= True)
            buf= io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            
            st.download_button(
                label= f"Download {data_selection}",
                data=buf,
                file_name= f"{task}_{data_selection}.{data_format}",
                mime="{data_selection}/{data_format}")

        elif data_selection== 'video':
            video= f'runs/{task}/predict/{uploaded_file.name}'
            st.video(video) #, caption= "Done.", use_container_width= True)
            with open(video, "rb") as f:
                video_bytes = f.read()
            st.download_button("Download Video", video_bytes, file_name=f"{uploaded_file.name}", mime="video/mp4")

        
        shutil.rmtree('assets/uploads')
        shutil.rmtree('runs')