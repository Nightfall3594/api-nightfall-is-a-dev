from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def ping():
    return {'ping': 'pong'}  # note: for testing connectivity only

@app.get('/timeline')
async def timeline():
    return {'timeline': []}  # return a timeline. Note: timeline items only


@app.get('/articles/{article_slug}')
async def article(article_slug: str):
    return {'id': ""}  # return an Article object using the slug. Note: Body is included


@app.get('/articles')
async def articles():
    return {'articles': []}  # get all articles, exclude body


@app.get('/thoughts')
async def thoughts():
    return {'thoughts': []}  # get all thought items