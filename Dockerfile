ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

COPY [ "requirements.txt", "."]

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

ENV HOME=/usr/src/code

RUN set -ex && apk update

RUN apk add --update --no-cache \
      bash=5.0.11-r1

COPY --from=install-env [ "/root/.local", "/usr/local" ]

WORKDIR ${HOME}

COPY [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

ENTRYPOINT []

CMD [ "python", "main.py" ]
