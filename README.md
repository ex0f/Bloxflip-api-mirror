# Bloxflip API Mirror

> [!CAUTION]
> Bloxflip (BFlip) has been shutdown so this code no longer works for that site

A Flask-based API mirror that allows you to send requests to Bloxflip's API seamlessly. This project is designed to handle issues like Cloudflare protection, offering a simple way to mirror API requests.It can also be made to mirror any other website API.
This Project was made after the shutdown of https://rest-bf.blox.land.

## Features

- **Cloudflare Bypass:** This code was made to handle Bloxflip's Cloudflare protection so users don't face issues like `cloudscraper.exceptions.cloudflarechallengeerror`.
- **API Mirroring:** Supports all HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) for any Bloxflip API endpoint.
- **Easy to Extend:** The code is structured to easily add more features or customize routes.

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/ex0f/Bloxflip-api-mirror.git
    cd Bloxflip-api-mirror
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Edit the configuration if needed (e.g., update the `API_URL` if Bloxflip changes their API also you can mirror any API with this code).

4. Run the application:
    ```bash
    python main.py
    ```

    The server will be available at `http://127.0.0.1:5000/`.

## Usage

To mirror any Bloxflip API endpoint, make a request to this server with the corresponding method:

```bash
For example: GET http://127.0.0.1:5000/games/crash
```


## Hosting Options

You can host this API mirror on:

- **Replit:** Easy to deploy and run online.[Replit](https://replit.com/).
- **Local Hosting:** Run it locally on your computer or any server that supports Python and Flask.

## Credits

- **Author:** `Ex` (Discord: `03ex | 1142117482979676261`)
- **Inspired by:** https://rest-bf.blox.land RIP.

## License
This project is licensed under the [MIT License](https://mit-license.org/).

> **Note:** This is not a hack or exploit. It simply bypasses Cloudflare protection to allow legitimate API requests and possibly mirror any API.
