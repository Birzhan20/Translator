import nest_asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import g4f

nest_asyncio.apply()

app = FastAPI()


class Txt(BaseModel):
    text: str | int


@app.post("/vacancy/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� �������� ��������, �������������� �� ������������� ������� Mytrade.kz �� ������ ����� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ������� ������ ������ Mytrade.kz �������� �{text}� � ��������� ������� ����, ������� ���������. ������� ������� �������� �{text}�. ��������� ������ ��������� ������� ����, � ������� �������� ���� ���������� �� ������ �������� � ������� ������ ������ Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/resume/index")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f" ������� ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ������ ���������� ������, �������������� �� ������������� ������� Mytrade.kz �� ������ ����� ������: �{text}�."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/vacancy/resume/seo")
async def generate_meta_description(request_body: Txt):
    text = request_body.text
    print(text)

    if not text:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ������� ������ ������ Mytrade.kz ������ ���������� � ����������� �� ��������� �{text}� � ��������� ������� ����, ������� ���������. ������� ������� ������ �{text}�. ��������� ������ ��������� ������� ����, � ������� ���������� ���� ������ �� ��������� (�������� ���������� �� ��� �� ������������ �������� ���������) � ������� ������ ������ Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������."}],
            stream=False,
        )
        print(response)

        meta_res = response.strip('"')

        return JSONResponse(content={"meta": meta_res})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
