# dempsy-worksession

## /.streamlit
- Contains two primary files:
1. secrets.toml
--- Copied over to streamlit when deployed
--- ensure that this is in .gitignore

2. config.toml
--- streamlit configuration items such as theme, server, logging, etc.

## /.gitignore
- Any file listed in .gitignore will not be pushed or committed when a build is created
- Important because secrets we do not want to push - but we still want to have them here to run locally


## /requirements.txt
- Contains any python packages used in the application
- The core are provided
- Automatically installed when the app is deployed
- Packages can be added and the app just needs to be rebooted via streamlit
- Use pip install -r requirements.txt to install initially so it can be used locally

## /app.py
- Streamlit requires a main python file that will run always when the app is launched
- Must be in the root folder
- Can be any name you want
- To run locally - python -m streamlit run app.py

## /pages
- Any pages outside of the main streamlit page (app.py) must be contained in the pages directory
- The names of the python files iwll be the names of the pages in streamlit

## /config
- Directory we use to hold any global or additoinal configuration items in our app
- Examples: Page title functions, styles, etc. that are used across the app
- NOTE: WE REUSE THIS IN EVERY APP

## /assets
- Holds any site assets such as logos, images, terms, etc.