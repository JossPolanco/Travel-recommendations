# Travel Recommendations API

This project is a tourist place recommendation API based on user preferences. Developed as a school project, it combines front-end and back-end technologies to provide an interactive destination search experience.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask
- **Database**: SQL
- **Maps**: Mapbox Integration

## Project Structure
```
josspolanco-travel-recommendations/
├── app.py                         # Main application entry point
├── requirements.txt               # Project dependencies
├── config/                        # Configurations
│   └── db.py                      # Database configuration
├── data/                          # Initial data
│   └── travel_recommendations.sql # SQL script for database
├── database/                      # Database access layer
│   └── init.py
├── models/                        # Data models
│   ├── init.py
│   └── places_model.py            # Model for tourist places
├── routes/                        # Route definitions
│   ├── init.py
│   ├── api.py                     # API routes
│   └── views.py                   # Web view routes
├── services/                      # Business logic
│   ├── init.py
│   ├── get_form_info.py           # Form processing
│   └── pycache/
├── static/                        # Static files
│   ├── css/
│   │   └── styles.css             # CSS styles
│   └── js/
│       ├── index.js               # Main JavaScript
│       ├── javascript.js          # Additional JavaScript functions
│       ├── mapbox-gl.js           # Mapbox GL library
│       ├── mapbox.js              # Mapbox configuration
│       └── mapkick.js             # Utilities for Mapbox
├── templates/                     # HTML templates
│   ├── index.html                 # Main page
│   ├── place.html                 # Place details page
│   └── layouts/
│       └── base.html              # Base template
├── test/                          # Tests
│   └── place_searching_testing.py # Place search tests
└── utils/                         # Utilities
├── init.py
└── db_utils.py                # Database utilities
```

## How to Run
1. Clone this repository:
   ```
   https://github.com/JossPolanco/Travel-recommendations.git
   ```
2. Create a virtual environment and install dependencies::
   ```
    python -m venv env
    env\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt   
   ```
4. Set up the database:
   ```
   # Import the SQL script
   # Adjust the configuration in config/db.py according to your environment
   ```
5. Run the application:
   ```
   python app.py
   ```

## Usage
- Access the web application at http://localhost:5000

- Use the form to enter your travel preferences
- Explore the personalized recommendations on the interactive map
- View specific details for each recommended place


##  Author

- **Josué Ángel Pérez Polanco**