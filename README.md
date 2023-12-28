# Project Poker planning

This project is a website created to implement web poker planning.
Using Python we implemented a Poker planning that would allow multiple users to connect online using Flask and Python tools.
In this project, Flask is used to make the connection between the database and the view, the database will be Firebase and finally the application is deployed using Gunicorn on Heroku.

## Game modes
Following Game modes will be possible be selected.

- Majority
- Average
- Median
- Unanimity

### Note
For unanimity, task will be changed only in case all players selected same score for a task

## How to run locally
Project was created for Python `3.10` and all dependencyes. \
Create a env variable with the value of the service account of firebase database, format is like following one.

```
export SERVICE_ACCOUNT_KEY='{"type": "service_account","project_id": "planning-poker-4352d","private_key_id": "65d...}'
```

The data base basic data is located in `data` folder with a format of `collection_document.json` for example `dicts` is the first base and `cards` is the name of all collection that will contains all register

## Build docs using pydoc
Run following command before upload project
```
pydoctor \
    --project-name=poker-planning \
    --project-version=1.0.0 \
    --project-url=https://github.com/jdalfons/ProjectAgileLyon/ \
    --html-viewsource-base=https://github.com/jdalfons/ProjectAgileLyon/tree/main \
    --make-html \
    --html-output=docs/ \
    --project-base-dir="." \
    --docformat=epytext \
    --intersphinx=https://docs.python.org/3/objects.inv \
    ./package ./tools ./api_routes
```
