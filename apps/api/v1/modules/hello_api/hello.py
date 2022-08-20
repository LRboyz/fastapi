from typing import Any
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/')
def hello() -> Any:
    html_content = """
        <html>
            <style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: 
    pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: 
    "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; 
    margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }</style><div style="padding: 24px 48px;"><p> 
    Hello 🎉 <br/><span style="font-size:30px">WelCome, this API is built by FastAPI 🔥 </span></p>
    <span>Author: 🧑🏻 LRboy</span>
    </div>
        </html>
    """
    return HTMLResponse(content=html_content)
