# sensible-rentals
A cronjob that finds sensible rentals in Ireland.

# Dev setup

## 1. Setup up virtual environment

```zsh
python3 -m venv my-venv
source my-venv/bin/activate
```

## 2. Install requirements

```zsh
python3 -m pip install -r requirements.txt
```

## 3. Make an `.env` with the following vars
```env
GOOGLE_API_KEY=...
POINT_OF_INTEREST=...           (stuff you'd like to be close to)
DAFT_DEFAULT_USER_AGENT=...
DAFT_CF_CLEARANCE=...
```

## 4. Load 'em up and run it!
```zsh
source .env && py -m src.main
```