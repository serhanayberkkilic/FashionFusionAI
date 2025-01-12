FROM python:3.11.2-alpine3.17

LABEL Maintainer="PEA"
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY ./App /code/App

EXPOSE 8000
CMD ["uvicorn", "App.Main:App", "--host=0.0.0.0" , "--reload" , "--port", "8000"]