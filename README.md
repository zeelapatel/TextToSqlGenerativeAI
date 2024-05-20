# Text-to-SQL Generative AI with Google Gemini API
## This project demonstrates how to use the Google Gemini API to convert natural language text into SQL queries using Python. The application is designed to take user input in the form of natural language queries and return the corresponding SQL statements, facilitating easier interaction with databases.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- You have Python 3.7 or later installed on your local machine.
- You have a Google Cloud account with access to the Google Gemini API.
- You have set up authentication for Google Cloud and obtained the necessary API credentials.

## Installation
1. Clone the Repository

```

git clone https://github.com/your-username/text-to-sql-gemini.git

```
```

cd text-to-sql-gemini

```
2. Install the Required Packages
```

pip install -r requirements.txt

```
3. Set Up Google Cloud Authentication

Ensure that you have your Google Cloud service account key file. Set the environment variable to point to your service account key file:
```

export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"

```
