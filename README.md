# Code Clinic Booking System

A command-line Python application for managing student and volunteer bookings for WeThinkCode_ Code Clinics. The program provides a text menu for creating student bookings, registering volunteer availability, cancelling bookings, and updating stored booking details. A Google Calendar integration is included to read Code Clinic calendar events.

> **Project status:** This is a student project/prototype. Booking records are currently stored in in-memory Python lists, so they are lost when the program exits. The `view` command is unfinished, and some calendar integration functions may need correction before they work reliably with the current Google Calendar API.

## Features

- Interactive command-line menu with help and quit commands.
- Student booking flow with checks for duplicate names/email addresses and WeThinkCode_ student email format.
- Volunteer booking flow.
- Cancellation and update flows for information held in the current process.
- Google Calendar API authentication and event lookup code.
- Unit-test files using Python's built-in `unittest` framework.

## Technology

- Python 3
- Google Calendar API
- Google API Python client and OAuth libraries
- `python-dateutil` for date parsing
- `tabulate` for formatted calendar output
- `unittest` for tests

## Project structure

```text
code-clinic-project-main/
├── booking_system.py                 # CLI entry point and command routing
├── authentication/
│   └── authentication.py             # Google OAuth and calendar access helpers
├── api_services/
│   └── calender_service.py            # Google Calendar API service creation
├── bookings/
│   ├── student_booking.py             # Student booking workflow
│   ├── volunteer_booking.py           # Volunteer booking workflow
│   ├── cancel_booking.py              # Booking cancellation
│   ├── update_information.py          # Update booking information
│   └── calendars/
│       └── calendar.py                # Code Clinic calendar event listing
├── Tests/                             # Feature-level unit tests
└── test_booking_system.py             # Booking-system tests
```

## Requirements

- Python 3.9 or later is recommended.
- Internet access for Google Calendar integration.
- A Google Cloud project with the Google Calendar API enabled if you intend to use calendar features.

Install the third-party dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 python-dateutil tabulate
```

If your environment uses a different Python version, check compatibility before installing packages.

## Setup

### 1. Get the project

Extract the ZIP file and open a terminal in the `code-clinic-project-main` directory.

### 2. Configure Google Calendar credentials (optional)

Calendar-related modules expect a local `credentials.json` OAuth client file and create a local `token.json` after authorization.

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Select or create a project and enable the **Google Calendar API**.
3. Configure the OAuth consent screen as required for your Google account.
4. Create an OAuth client ID for a **Desktop app** and download its JSON file.
5. Save it as `credentials.json` in the project root, next to `booking_system.py`.
6. Run the relevant calendar function; a browser window may open so you can authorize access.

**Security:** Never commit `credentials.json`, `token.json`, access tokens, refresh tokens, or client secrets to Git or share them publicly. If credentials or tokens have already been exposed, revoke the token and rotate the OAuth client secret in Google Cloud Console, then create fresh local files. The project archive originally supplied contained credential/token files; those are intentionally excluded from the cleaned ZIP provided with this README.

The main interactive booking menu does not require Google Calendar authentication for its basic in-memory workflows. Calendar integration is separate and may require fixes described below.

## Run the application

From the project root:

```bash
python booking_system.py
```

The program displays the Code Clinic welcome message and prompts for a command.

### Available commands

| Command | Description |
|---|---|
| `h` or `help` | Display help text |
| `b` or `book` | Start the student booking workflow |
| `v` or `volunteer` | Start the volunteer booking workflow |
| `c` or `cancel` | Cancel a student booking |
| `u` or `update` | Update a booking detail |
| `vc` or `view` | View bookings (currently marked as work in progress) |
| `q` or `quit` | Exit the application |

Use the command names shown by the application. The booking and volunteer flows prompt for further details in the terminal.

## Google Calendar integration

The calendar code is intended to retrieve upcoming events from the Code Clinic calendar and show whether slots appear to be booked. The calendar integration is not fully wired into the main menu and should be tested separately after configuring Google OAuth.

Before relying on it, review and test the following in `api_services/calender_service.py` and `bookings/calendars/calendar.py`:

- The Calendar API `events().list()` parameter should be `timeMin`, not `timein`.
- The OAuth scope should use `https://www.googleapis.com/auth/calendar.readonly` (the supplied code has a malformed scope string in one module).
- The code uses a fixed date from 2022; use the current UTC timestamp for future event searches.
- The event attendee list may be missing; handle absent `attendees` safely.
- Check calendar IDs and permissions for the account authorizing the application.

## Tests

Run the tests from the project root:

```bash
python -m unittest discover -s Tests -v
python -m unittest test_booking_system -v
```

Some existing test methods are placeholders or may need fixes (for example, `test_help_commands` and `test_get_commands` do not currently assert expected behavior). Test imports and module paths may also need adjustment depending on how the project is launched.

## Known limitations and recommended improvements

- **Persistence:** bookings are stored in module-level lists and are not saved to a database or file.
- **Validation:** input handling is inconsistent; some flows may accept invalid or mismatched values.
- **Data consistency:** parallel lists hold related fields, which can become misaligned. Replace them with a booking class/data model and a single collection or database table.
- **Cancellation/update safety:** operations should validate that a matching booking exists before indexing or removing data.
- **Privacy:** the cancellation workflow prints student PIN values; remove this output and avoid storing authentication PINs as plain text.
- **Calendar integration:** API parameter names, scopes, fixed timestamps, and missing attendees need correction.
- **Testing:** add assertions for command routing, booking validation, duplicate handling, cancellation, updates, and calendar failures.
- **Code quality:** consider adding `requirements.txt`, structured logging, type hints, and clearer separation between the CLI, booking logic, and calendar service.

## Troubleshooting

- **Missing Python package:** install the dependencies listed above using the same Python interpreter used to run the application.
- **OAuth file not found:** ensure your own `credentials.json` is in the project root; do not download or reuse someone else's credential file.
- **OAuth authorization errors:** verify that the Calendar API is enabled, the OAuth consent screen is configured, and your Google account is permitted to use the app.
- **Calendar request errors:** check the API parameters, scopes, calendar ID, and current account permissions.
- **Import errors:** run commands from the project root so Python can resolve the `bookings`, `authentication`, and `api_services` packages.

## License

Refer to the license file in the `authentication` directory for the licensing terms of that component. No overall project license was identified in the supplied project root.
