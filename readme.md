kami-super-user
kami-testpass123

testuser
testuser@email.com
testpass123

# Airplane Fuel Efficiency API

This project is a RESTful API built with Django and Django REST Framework. It allows users to input airplane data, including a user-defined ID and passenger assumptions. The API calculates and returns the total fuel consumption per minute and the maximum flight minutes for each airplane. It also provides flight details, including departure time, arrival time, origin, destination, and airplane details.

## Starting

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerequisites

You will need to have Python 3.10 or higher and Docker installed. You will also need a copy of the source code, which you can obtain by cloning the GitHub repository.

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/RDSDeveloper/airline-passenger-api.git
    ```
2. Navigate into the directory:
    ```
    cd airline-passenger-api
    ```
3. Copy the `env.sample` file to a new file named `.env`:
    ```
    cp env.sample .env
    ```
4. Open the `.env` file and replace the placeholder values with your actual data.

### Running the Application

1. Build and start the Docker containers:
    ```
    docker-compose up --build
    ```
    This command will install the necessary dependencies as defined in the `requirements.txt` file and start the application.

### API Endpoints

Once the application is running, you can access the following endpoints:

#### Authentication and Registration

- `http://localhost:8000/dj-rest-auth/login/`: Log in.
- `http://localhost:8000/dj-rest-auth/logout/`: Log out.
- `http://localhost:8000/dj-rest-auth/password/reset/`: Reset password.
- `http://localhost:8000/dj-rest-auth/registration/`: Register as a new user.

#### Airplanes

- `http://localhost:8000/api/v1/airplanes/`: List all airplanes or create a new one.
- `http://localhost:8000/api/v1/airplanes/<id>/`: Retrieve, update, or delete a specific airplane.

#### Flights

- `http://localhost:8000/api/v1/flights/`: List all flights or create a new one.
- `http://localhost:8000/api/v1/flights/<id>/`: Retrieve, update, or delete a specific flight.

#### API Documentation

- `http://localhost:8000/api/schema/`: View the API schema.
- `http://localhost:8000/api/schema/redoc`: View the API documentation in Redoc.
- `http://localhost:8000/api/schema/swagger-ui/`: View the API documentation in Swagger UI.

Replace `<id>` with the ID of the airplane or flight you want to retrieve, update, or delete.

### Test User

To test the API, you can create your own user using the registration endpoint:

- `http://localhost:8000/dj-rest-auth/registration/`

After registering, you can log in with your new user credentials at the login endpoint:

- `http://localhost:8000/dj-rest-auth/login/`

Once logged in, you can use this user to test the API endpoints.

### Testing

This project uses Django's built-in testing tools in combination with Coverage.py. To run the tests and generate a coverage report, use the following commands:

1. Run the tests:
    ```
    docker-compose run web coverage run manage.py test
    ```
2. Generate the coverage report:
    ```
    docker-compose run web coverage report
    ```

This will display a report in the terminal showing the coverage of each file.

If you want to generate an HTML report, you can use the following command instead:

1. Generate the coverage report as HTML:
    ```
    docker-compose run web coverage html
    ```

This will generate an HTML report in a new `htmlcov` directory. You can open the `index.html` file in your web browser to view the report.