from pydantic import BaseModel, HttpUrl, validator

class IngestRequest(BaseModel):
    file_name: str
    s3_url: HttpUrl  # ensures valid URL

    @validator("s3_url")
    def must_be_pdf(cls, v: HttpUrl):
        url_str = str(v)  # convert HttpUrl object to string
        if not url_str.lower().endswith(".pdf"):
            raise ValueError("url must be extension of PDF file")
        return v
        
class ChatRequest(BaseModel):
    q: str