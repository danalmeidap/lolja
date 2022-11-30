<h1 align="center">LOLJA</h1>
<p align="center">App for buying and seeling food</p>
<p>This  application uses:</p>
<ul>
    <li><a href="https://www.python.org/downloads/release/python-3810/">Python</a></li>
    <li><a href="https://docs.python.org/3/library/typing.html">Type hints</a></li>
    <li><a href="https://black.readthedocs.io/en/stable/">Black</a></li>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://docs.sqlalchemy.org/en/14/">SQLALCHEMY</a></li>
    <li><a href="https://www.sqlite.org/docs.html">SQLITE3</a></li>
</ul>

# 


# Features

- [x] Add product
- [x] Lists products
- [x] Get product by id
- [x] Update product
- [x] Delete product by id
- [x] Add a Order and relationate with your owner
- [x] Add a user
- [x] List buys and sells by user
- [x] Authenticate and validate user by token

# 


# How to use

### Clone or download repository, activate your virtual environment and install tools running

```pip install -r requirements.txt```

### To run application use, on root of project
 
```uvicorn server:app --reload --reload-dir=src```

