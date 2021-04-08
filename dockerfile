FROM python:3
WORKDIR /omnilytics
COPY . .
CMD ["challenge_a.py"]
CMD ["generator.txt"]
CMD ["challenge_b.py"]
EXPOSE 5000
ENTRYPOINT ["python3"]