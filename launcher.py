import threading
import time
import webbrowser
from urllib.request import urlopen
from urllib.error import URLError

import uvicorn

from backend.main import app


HOST = "127.0.0.1"
PORT = 8001

APP_URL = f"http://{HOST}:{PORT}"


def open_browser_when_ready():
    """Open the kiosk in the browser after the server is ready."""

    health_url = f"{APP_URL}/api/health"

    for _ in range(60):
        try:
            with urlopen(health_url, timeout=2) as response:
                if response.status == 200:
                    webbrowser.open(APP_URL)
                    return

        except (URLError, TimeoutError, OSError):
            time.sleep(1)

    print("Could not connect to Brew & Co. server.")


if __name__ == "__main__":

    print("Starting Brew & Co. Smart Coffee Ordering...")
    print(f"Application URL: {APP_URL}")

    browser_thread = threading.Thread(
        target=open_browser_when_ready,
        daemon=True
    )

    browser_thread.start()

    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        log_level="info"
    )