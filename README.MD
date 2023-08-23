# Short URL
## _Make URLs Easier To Read, Remember & Share_

Short URL is an API-driven web application which creates shortened
URLs that forward to target URLs. 

## Tech

Short URL uses the following technology:

- [Python](https://www.python.org) - A high-level, general purpose programming language
- [FastAPI](https://fastapi.tiangolo.com) - A modern, fast web framework for building APIs
- [Uvicorn](https://www.uvicorn.org) - An ASGI web server for Python
- [SQLite](https://www.sqlite.org) - A small, fast & full featured SQL database engine

## How It Works

This application is supported by an API which creates and manages shortened URLs. THe main
purpose of the API is to receive a full target URL and return a shortened URL.

When you post a target URL to the Short URL application, you get a shortened URL and a secret
key back. The shortened URL contains a random key that forwards to the target URL. You can
use the secret key to see the shortened URLs statistics or delete the forwarding.

## API Overview

Here is a summary of the API endpoints that power Short URL:

| Endpoint | HTTP Method | Request Body | Action |
| ------ | ------ | ------ | ------ |
| / | GET | | Returns a welcome string |
| /url | POST | Your target URL | Shows the created url_key with additional info, including a secret_key |
| /{url_key} | GET | | Forwards to your target URL |
| /admin/{secret_key} | GET | | Shows administrative info about your shortened URL |
| /admin/{secret_key} | DELETE | Your secret key | Deletes your shortened URL |
