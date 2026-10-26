# Smart Coffee Ordering

**Computer Vision • Hand Gesture • Touchless Ordering**

A touchless coffee ordering kiosk. Customers browse the menu, add drinks to a cart and place an order using **hand gestures** captured by a webcam, with no mouse or touch screen required. Built by **Group 14** as a university project.

<!-- TODO: add screenshots -->
<!-- ![Home page](docs/images/home.png) -->

---

## Features

- Touchless navigation with hand gestures (webcam + MediaPipe hand tracking)
- Browsable coffee menu loaded from `data/menu.json`
- Shopping cart: add, remove and review items
- Order placement, with orders stored in a local database (`data/orders.sqlite3`)
- Customer accounts and login
- Admin login and order management
- Contact page / messages
- Responsive web interface (HTML, CSS, JavaScript)

> TODO: list the exact gestures supported (for example: point to hover, pinch to select, open palm to go back).

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| Computer vision | OpenCV, MediaPipe Hands |
| Database | SQLite (`data/orders.sqlite3`) |
| Frontend | HTML5, CSS3, vanilla JavaScript |

---

## Project Structure

```
smart-coffee-ordering-by-group-14/
├── backend/
│   ├── main.py              # FastAPI app and API routes
│   ├── config.py            # Settings
│   ├── database.py          # Database connection and setup
│   ├── camera.py            # Webcam capture
│   ├── hand_tracker.py      # MediaPipe hand tracking
│   ├── gesture_engine.py    # Converts hand landmarks into gestures
│   ├── menu_manager.py      # Menu loading
│   ├── cart_manager.py      # Cart logic
│   ├── order_manager.py     # Order creation and queue
│   ├── customer_manager.py  # Customer data
│   ├── customer_auth.py     # Customer authentication
│   ├── admin_auth.py        # Admin authentication
│   ├── contact_manager.py   # Contact messages
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html
│   ├── menu-fallback.json
│   ├── css/                 # style.css, responsive.css
│   ├── img/                 # Product images
│   └── js/                  # app, cart, orders, touchless, admin, ...
├── data/
│   ├── menu.json            # Coffee menu
│   └── orders.sqlite3       # Orders database
└── docs/
    └── architecture.md
```

---

## Requirements

- **Python 3.11 or newer** (tested on 3.13)
- A **webcam**
- **Google Chrome** (or another modern browser)
- Windows, macOS or Linux (the commands below are for Windows PowerShell)

---

## Installation

**1. Clone the repository**

```powershell
git clone <your-repository-url>
cd smart-coffee-ordering-by-group-14
```

**2. Create a virtual environment**

```powershell
python -m venv .venv
```

**3. Activate it**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

You should now see `(.venv)` at the start of your prompt.

**4. Install dependencies**

```powershell
python -m pip install -r backend/requirements.txt
```

> If you see `No module named 'cv2'` or `'mediapipe'` when starting the server, install them manually:
> `python -m pip install opencv-python mediapipe numpy`

---

## Running the Project

With the virtual environment activated, from the project root folder:

```powershell
python -m uvicorn backend.main:app --reload
```

Then open Chrome and go to:

```
http://127.0.0.1:8000
```

When Chrome asks for camera permission, click **Allow**. Keep the terminal open while using the site; press `Ctrl + C` to stop the server.

> **Do not open `index.html` by double-clicking it.** The site needs the backend running, and browsers only allow camera access on `localhost` / `127.0.0.1`.

---

## How to Use

1. Start the server and open the site in Chrome.
2. Allow camera access and keep your hand visible to the webcam.
3. Use hand gestures to browse the menu, add items to your cart and place your order.

> TODO: add a table of gestures and what each one does.

---

## API Overview

> TODO: fill in from `backend/main.py`.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/menu` | Get the menu |
| POST | `/api/orders` | Place an order |

---

## Troubleshooting

**PowerShell says "running scripts is disabled on this system"**
Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate the venv again. This only affects the current terminal.

**`Fatal error in launcher: Unable to create process using ...python.exe`**
The project folder was moved after the virtual environment was created. Virtual environments cannot be moved. Delete `.venv` and recreate it (steps 2-4 above).

**`No module named 'backend'`**
Run the server from the project root folder (the one that contains `backend/` and `frontend/`), not from inside `backend/`.

**`No module named 'cv2'` / `'mediapipe'`**
Run `python -m pip install opencv-python mediapipe numpy`. If MediaPipe does not install on your Python version, use Python 3.11 or 3.12.

**Camera does not start**
Make sure no other app (Zoom, Teams, another browser tab) is using the webcam, and that you clicked **Allow** in Chrome. Use `http://127.0.0.1:8000`, not a `file://` path.

**"This site can't be reached"**
The server is not running. Start it again with the command in *Running the Project*.

---

## Team

**Group 14**

| Name | Role |
|---|---|
| TODO | TODO |

---

## License

> TODO: choose a license, or write "For educational use only."
