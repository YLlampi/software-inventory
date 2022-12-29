FROM python:3.10.6
ENV PYTHONUNBUFFERED 1

COPY /software-inventory/requirements.txt /tmp/requirements.txt
COPY /software-inventory/requirements_dev.txt /tmp/requirements_dev.txt
COPY /software-inventory /software-inventory
WORKDIR /software-inventory
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements_dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    chown -R django-user:django-user -R /software-inventory/


ENV PATH="/scripts:/py/bin:$PATH"

USER django-user