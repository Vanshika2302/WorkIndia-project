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

- POST `/api/admin/signup`: Register an admin user.
- POST `/api/admin/login`: Login an admin user.
- POST `/api/matches`: Create a new match.
- GET `/api/matches`: Get all match schedules.
- GET `/api/matches/{match_id}`: Get details of a specific match.
- POST `/api/teams/{team_id}/squad`: Add a player to a team's squad.
- GET `/api/players/{player_id}/stats`: Get player statistics.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, improvements, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
