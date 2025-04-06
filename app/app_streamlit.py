from predict import *

light_background= "#E6E6FA"
dark_background= "#483D8B"

def webapp_fn():
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: {light_background} !important;
            }}
            
            @media (prefers-color-scheme: dark) {{
                .stApp {{
                    background-color: {dark_background} !important;
                }}
            }}
        </style>
    """, unsafe_allow_html=True)


    st.title("Yolo v8 Web App")
    st.markdown("[Visit my portfolio](https://amir-hofo.github.io/Portfolio/)")

    with st.expander("ℹ️ How to use"):
        st.markdown("""
            1. Choose your data type (image/video)
            2. Select the task you want to perform:
                - Object Detection: Detects and locates objects
                - Segmentation: Creates pixel-level masks
                - Tracking: Tracks objects in videos
                - Body Position: Detects human poses
            3. Upload your file
            4. Wait for processing
            5. Download the results
        """)

    data_selection= st.selectbox("Choose your data type", ["image", "video"])
    # task_selection= st.selectbox("Choose your task", ["segmentation", "object detection",
    #                                                   "oriented bounding box", "classify",
    #                                                   "body position"])
    

    if data_selection== "video":
        task_selection= st.selectbox("Choose your task", ["tracking", "segmentation",
                                                        #   "oriented bounding box", "classify",
                                                          "body position"])
        uploaded_file= st.file_uploader("Choose an video...", type= ["mp4", "mkv"])
    else:
        task_selection= st.selectbox("Choose your task", ["segmentation", "object detection",
                                                        #   "oriented bounding box", "classify",
                                                          "body position"])
        uploaded_file= st.file_uploader("Choose an image...", type= ["jpg", "jpeg", "png"])
    
    task_map= {"segmentation": 'segment',
                "object detection": 'detect',
                "tracking": 'detect',
                # "oriented bounding box": 'obb', 
                # "classify": 'classify',
                "body position": 'pose'}
    
    model_map= {"segmentation": '-seg',
                "object detection": '',
                "tracking": '',
                # "oriented bounding box": '-obb', 
                # "classify": '-cls', 
                "body position": '-pose'}
    
    task= task_map[task_selection]
    model= f'assets/model/yolov8n{model_map[task_selection]}.pt'
    # task= 'segment' if task_selection== "segmentation" else "detect"
    # model= 'assets/model/yolov8n-seg.pt' if task_selection== "segmentation" else 'assets/model/yolov8n.pt'


    if uploaded_file:
        with st.spinner('Processing... Please wait'):
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