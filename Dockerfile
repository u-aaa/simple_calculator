FROM python:3.8.0-slim

# Make a directory for our application
WORKDIR /app

# Copy our source code
RUN pip install simple-calculator-u-aaa==0.0.3

# Run the application
CMD ["python"]