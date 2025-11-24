import uvicorn
import os

if __name__ == "__main__":
   
    if not os.path.exists("data"):
        os.makedirs("data")
        
    
    uvicorn.run("server.app:app", host="127.0.0.1", port=8000, reload=True)