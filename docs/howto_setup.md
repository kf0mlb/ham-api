# Project Setup

## Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate # linux
# or
.\.venv\Scripts\Activate.ps1 # windows powershell

pip install -r requirements.txt
```

## Environment Variables

The API is looking for the `.env` file in the root directory. Variables to define are:

- `PROJ_URL` : This URL is sent out in the notification emails, it should match your local or public DNS name, including URI and port if needed. This will also be used on the FastAPI docs page.
- `PROJ_EMAIL` : This email is used with the notification emails, it should be a valid email in the event you get a reply. This will also be used on the FastAPI docs page.
- `PROJ_TEAM_NAME` : The Team Name will be used as the sender on the notification emails. This will also be used on the FastAPI docs page.
- `PROJ_SITE_NAME` : The Site Name will be used on the email body of the notification emails. This will also be used on the FastAPI docs page.
- `ANALYTICS_APIKEY` : API Key from APIAnalytics.dev

## Generate API Analytics API Key

1. Go to [apianalytics.com/generate](https://apianalytics.com/generate)
2. Click Generate
3. Copy secret to .env file
