FROM python:3.6

RUN adduser --system --uid 999 happycity
USER happycity

WORKDIR /app

COPY --chown=999:999 requirements*.txt ./
RUN pip install --no-cache-dir --user -r requirements.txt

COPY --chown=999:999 . .

CMD ["python3", "happycity.py"]