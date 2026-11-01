from pathlib import Path
import os
<<<<<<< HEAD
import sys
import shutil
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

# Detect packaged EXE
IS_FROZEN = getattr(sys, "frozen", False)

if IS_FROZEN:
    RESOURCE_DIR = Path(sys._MEIPASS)

    LOCAL_APP_DATA = Path(
        os.environ.get(
            "LOCALAPPDATA",
            Path.home() / "AppData" / "Local"
        )
    )

    APP_DATA_DIR = LOCAL_APP_DATA / "BrewCo"
    DATA_DIR = APP_DATA_DIR / "data"
    ENV_PATH = APP_DATA_DIR / ".env"

else:
    RESOURCE_DIR = ROOT
    APP_DATA_DIR = ROOT
    DATA_DIR = ROOT / "data"
    ENV_PATH = ROOT / ".env"

# Database and menu paths
DB_PATH = DATA_DIR / "orders.sqlite3"
MENU_PATH = DATA_DIR / "menu.json"

# Default menu included with the EXE
DEFAULT_MENU_PATH = RESOURCE_DIR / "data" / "menu.json"

# Create writable data folder
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Copy menu only on first installation
if IS_FROZEN and not MENU_PATH.exists():
    if DEFAULT_MENU_PATH.exists():
        shutil.copy2(DEFAULT_MENU_PATH, MENU_PATH)

# Load environment variables
load_dotenv(ENV_PATH)
=======
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "orders.sqlite3"
MENU_PATH = DATA_DIR / "menu.json"
load_dotenv(ROOT / ".env")
>>>>>>> origin/Develop
GESTURE_HOLD_SECONDS = 1.25
FIST_CANCEL_HOLD_SECONDS = 0.65
GESTURE_COOLDOWN_SECONDS = 0.28
# Ratio of thumb/index tip distance to palm width, so pinches behave similarly
# whether the hand is near or far from the webcam.
PINCH_DISTANCE_THRESHOLD = 0.38
FINGER_EXTENSION_MARGIN = 0.025
OPEN_PALM_HOLD_SECONDS = 0.45
THUMBS_UP_HOLD_SECONDS = 0.55
SWIPE_X_THRESHOLD = 0.12
SWIPE_Y_THRESHOLD = 0.12
SWIPE_MIN_DURATION = 0.12
SWIPE_RELEASE_THRESHOLD = 0.04
HAND_DETECTION_CONFIDENCE = 0.65
HAND_TRACKING_CONFIDENCE = 0.55
