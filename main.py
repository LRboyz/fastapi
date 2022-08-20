from apps import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1', port=9080, debug=False, reload=True, access_log=False,workers=1, use_colors=True)