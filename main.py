""" import neccessary libs"""
from fastapi import FastAPI
import uvicorn
from mylib import preprocess as prep
from mylib.user_request import PreprocessingRequest

step_name_to_obj = {
    "remove_punkt": prep.RegExRemovePunkt(),
    "replace_number_like": prep.RegExReplaceNumberLike(),
    "replace_phone": prep.RegExReplacePhone(),
    "replace_email": prep.RegExReplaceEMail(),
    "lower": prep.Lowercase(),
}


api = FastAPI()


@api.get("/")
async def root():
    """Root page"""
    return {"message": "Hello, this is a text preposessing api"}


@api.get("/preprocess/")
def preprocess(request: PreprocessingRequest):
    """Do preprocessing"""
    steps = request.steps
    text = str(request.text)
    preprocessed_text = "" + text
    for step in steps:
        preprocessed_text = step_name_to_obj[step].preprocess(preprocessed_text)

    response = {"steps": steps, "text": text, "preprocessed_text": preprocessed_text}
    return response


if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")
