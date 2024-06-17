import os

from dotenv import load_dotenv



load_dotenv()

IS_PRODUCTION = os.getenv('IS_PRODUCTION')

if IS_PRODUCTION:
    print("Ambiente de Production")
    from .conf.production.settings import *
else:
    print("Ambiente de Develoment")
    from .conf.development.settings import *
