from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse



def not_found_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content=dict(detail=exc.message)  # noqa
    )


def logic_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content=dict(detail=exc.message)  # noqa
    )