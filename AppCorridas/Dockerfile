FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN pip install gunicorn
CMD ["gunicorn","--bind","0.0.0.0:8000","app:app"]