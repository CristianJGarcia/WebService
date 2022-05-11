FROM python:3.8
WORKDIR /adv
COPY packages.txt packages.txt
RUN pip install -r packages.txt
COPY . .
EXPOSE 12075
CMD ["python", "web.py"]