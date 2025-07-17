# from fastapi import FastAPI, Query
from transliterate import translit

# app = FastAPI()

# @app.get("/transliterate/")
# def transliterate_name(name: str = Query(..., example="Алексей")):
#     try:
#         result = translit(name, 'ru')
#         return {"original": name, "transliterated": result}
#     except Exception as e:
#         return {"error": str(e)}

