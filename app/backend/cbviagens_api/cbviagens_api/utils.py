def getResponse(ok: bool, code: int, data: dict):
    return {
        "status": "success" if ok else "error",
        "code": code,
        "data": data
    }

        

