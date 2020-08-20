from starlette.applications import Starlette

import settings
from urls import routes


app = Starlette(routes=routes,
                **settings.BACKEND_SETTINGS)
