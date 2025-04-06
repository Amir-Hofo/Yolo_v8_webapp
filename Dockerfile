FROM python:3.10-slim

WORKDIR /app

# install libgl1
RUN apt-get update && apt-get install -y libgl1

# Copy the requirements file first, to leverage Docker cache efficiently
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application files
COPY main.py .
COPY app/ app/
COPY utils/ utils/
COPY predict/ predict/
COPY assets/ assets/

# Ensure necessary directories are created
RUN mkdir -p assets/uploads runs

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1
# ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV PYTHONPATH="/app"

# Run the Streamlit app on container start
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]