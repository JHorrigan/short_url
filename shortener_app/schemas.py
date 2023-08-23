# shortener_app/schemas.py

from pydantic import BaseModel

# Inherits from pydantic BaseModel
class URLBase(BaseModel):
    target_url: str

# Inherits pydantic BaseModel with target URL
class URL(URLBase):
    is_active: bool # allows you to deactivate a shortened URL
    clicks: int # how many times a shortened URL has been visited

    class Config: # provide configurations to pydantic
        orm_mode = True # work with a database model

# Enhances URL with additional info
# Subclassed so that it can be used in API, but not in URL for database
class URLInfo(URL):
    url: str
    admin_url: str