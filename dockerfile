FROM python:3.8


WORKDIR /app
COPY . /app
ENV FLASK_ENV=production
RUN pip --no-cache-dir install -r requirements -i https://mirrors.aliyun.com/pypi/simple
EXPOSE 5000
CMD gunicorn -w 4 -b 0.0.0.0:5000 app:app >> app.log