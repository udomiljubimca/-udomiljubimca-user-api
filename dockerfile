FROM udomiljubimca/base-image:1.0

ENV POSTGRES_URL ${POSTGRES_URL}
ENV POSTGRES_URL ${POSTGRES_URL}
ENV POSTGRES_DB ${POSTGRES_DB}
ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_PASSWORD: ${USER_SERVICE_DB_PASSWORD}

ADD ./server.sh ./requirements.txt . ./app /app/

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    chown -R appuser:root /app && \
    chmod -R g=u /app

WORKDIR /app

USER appuser

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]