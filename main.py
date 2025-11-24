import uvicorn
import os

if __name__ == "__main__":
    # Ensure the data directory exists before starting
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # Run the server
    # "server.app:app" means: look in 'server' folder, 'app.py' file, for the 'app' object
    uvicorn.run("server.app:app", host="127.0.0.1", port=8000, reload=True)