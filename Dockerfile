# Use an official Python runtime as a parent image
FROM python:3.12.2

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Poetry with a specific version and clean up cache
RUN pip install poetry==1.8.1 && rm -rf /root/.cache/pip

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && rm -rf /root/.cache/pypoetry

# Command to run the bot
CMD ["poetry", "run", "python", "app/main.py"]
