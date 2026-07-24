import uvicorn

# levantar o servidor uvicorn para rodar a aplicação FastAPI
if __name__ == "__main__":
    uvicorn.run(
        "src.main.server.server:app", 
        host="0.0.0.0",
        port=3001,
        reload=True
    )