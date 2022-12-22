import uvicorn      

# if __name__ == "__main__":
#     uvicorn.run("server.api:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    uvicorn.run("server.api:app", host="192.168.0.2", port=8000, reload=True)   