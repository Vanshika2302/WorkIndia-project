# Cricbuzz Clone

A Flask application for a cricket-related platform, inspired by Cricbuzz.

## Description

This project aims to replicate the core functionalities of Cricbuzz, providing users with the ability to view cricket match schedules, details, player statistics, and more. It also includes authentication and authorization mechanisms for admin and guest users.

## Features

- User registration and login for admins
- Admin dashboard for managing matches and teams
- Guest view for browsing match schedules and details
- APIs for creating matches, fetching schedules, and accessing player statistics

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Vanshika2302/WorkIndia-project/tree/main
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the database URI in `config.py`.

4. Run the application:

    ```bash
    python run.py
    ```

## Usage

- Access the admin dashboard at `/admin` after logging in with admin credentials.
- View match schedules and details at `/matches` as a guest user.
- Use the provided APIs for programmatic access to various functionalities.

## Endpoints

- POST `/aplication/register`: Register an admin user.
- POST `/aplication/login`: Login an admin user.
- POST `/aplication/creatematches`: Create a new match.
- GET `/application/getmatcheschedule`: Get all match schedules.
- GET `/aplication/getmatchedetails/{match_id}`: Get details of a specific match.
- POST `/application/addteam/{team_id}/squad`: Add a player to a team's squad.
- GET `/aplication/getplayerstatics/{player_id}`: Get player statistics.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, improvements, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
