FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the script is executable
RUN chmod +x start.sh

CMD ["./start.sh"]