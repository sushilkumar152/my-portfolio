Install python, node
npm install -g @angular/cli
create ui & api folders
inside api folder
    python -m venv venv
    pip install fastapi uvicorn pydantic
    mkdir controllers services dao models
    type nul > __init__.py
    type nul > main.py

For UI
Generate the Angular workspace:
    npx @angular/cli new portfolio-ui --directory . --style=css --routing=true
    npm install -D tailwindcss postcss autoprefixer
    npx tailwindcss init

The Next Step (Setting up the FastAPI Backend) in main.py file
Verify and run fast api code: uvicorn main:app --reload
Run the command in browser: http://127.0.0.1:8000/docs