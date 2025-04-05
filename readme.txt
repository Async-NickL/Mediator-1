# Mediator Project

A Flask-based web application with separate Frontend and Backend components.

## Project Structure
- Frontend/: Contains templates and static files
- Backend/: Contains backend routes and logic
- app.py: Main application entry point
- requirements.txt: Project dependencies
- .env: Environment variables (not tracked in git)

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a .env file in the root directory
   - Add the following variables:
     ```
     SECRET_KEY=your_secret_key_here
     ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. The application will be available at http://localhost:5000

## Development

- The application uses Flask as the web framework
- Frontend templates are located in Frontend/templates/
- Static files (CSS, JS, images) are in Frontend/static/
- Backend routes are organized in Backend/routes/

## Testing

Run the test suite:
```bash
python testing.py
```

## Notes

- The application runs in debug mode by default
- Make sure to set a secure SECRET_KEY in your .env file
- The application is configured to accept connections from all hosts (0.0.0.0)
