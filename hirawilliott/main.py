from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from hypermedia import Element
from hypermedia.fastapi import full, htmx

from hirawilliott.hiragana.router import router as hiragana_router
from hirawilliott.speak.router import router as speak_router

from hirawilliott.views.index import render_index, render_index_partial

app = FastAPI(
    title="Hirawilliott.",
    description="Hirawilliott. Hiragana practice for kids",
)


@app.middleware("http")
async def add_vary_accept_header(  # type: ignore
    request: Request,
    call_next,
) -> Response:
    """Add the vary accept header.

    This allows the browser to cache the responses based on caller,
    which should prevent the browser from caching htmx responses as a full page
    """
    response: Response = await call_next(request)
    response.headers["Vary"] = "Accept"
    return response


@app.get("/", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass


app.include_router(hiragana_router)
app.include_router(speak_router)


app.mount("/static", StaticFiles(directory="hirawilliott/static/"), name="static")
app.mount(
    "/hiragana/static",
    StaticFiles(directory="hirawilliott/hiragana/static/"),
    name="static",
)
