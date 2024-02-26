FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY ./ ./

RUN apt-get update && apt-get install -y wait-for-it

# Grant execute permissions to the script
RUN chmod +x entrypoint.sh

# Run the entrypoint script
CMD ["./entrypoint.sh"]

# CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"] 