# Accounting Ledger

A web-based double-entry accounting system built with Django and React. This application allows users to record transactions and view their financial position using double-entry accounting principles.

## Tech Stack

- **Backend**: Django
- **Frontend**: React
- **Database**: PostgreSQL
- **Development Tools**: Docker

## Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Getting Started

#### Clone the repository
```bash
git clone https://github.com/eulloa10/accounting-ledger.git
cd accounting-ledger
```

#### Start the Docker containers
```bash
docker-compose up --build
```

#### Access the application
```bash
  Django Backend: http://localhost:8000
  pgAdmin: http://localhost:5050
      Email: admin@admin.com
      Password: admin
```

## Development
#### Running Migrations
```bash
docker-compose exec web python manage.py migrate
```

#### Creating a Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

#### Running Tests
```bash
docker-compose exec web python manage.py test
```

## Features
- Double-entry accounting system
- Account management
- Transaction management
- Financial position tracking
- User authentication
- RESTful API
- PostgreSQL database integration
- pgAdmin for database management

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/eulloa10/accounting-ledger/blob/main/LICENSE) file for details.
