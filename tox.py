[flake8] max-line-length = 120
application_import_names = bot
docstring-convention = all
ignore = P102,B311,W503,E226,S311,
# FastAPI Depends and Header
__B008__,D100,D104,D105,D107,

D203,D212,D214,D215,
"  ", D301,D302,
D400,D401,D402,D404,D405,
D406,D407,D408,D409,D410,
D411,D412,D413,D414,D416,
D417
ANN002,ANN003,ANN101,ANN102,ANN204,ANN206,F722

import-order-style = appnexus
exclude =
__init__.py, config.py, 
tests/*, alembic/*

[pytest] filterwarnings =
ignore::Deprecation::ignore
addopts = 
[-p tests.plugins.env_vars]
