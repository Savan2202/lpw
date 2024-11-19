
FROM python:3.9-slim


WORKDIR \

EXPOSE 5000

CMD ["python3", "hms.py"]