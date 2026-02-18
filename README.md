# sensible-rentals
A notification job that finds sensible rentals in Ireland.

# Dev setup

## 1. Set virtual environment up

```zsh
python3 -m venv my-venv
source my-venv/bin/activate
```

## 2. Install requirements

```zsh
python3 -m pip install -r requirements.txt
```

## 3. Create a `.env`
```env
GOOGLE_API_KEY=...
WORKPLACE_ADDRESS=...           (or any address you'd like to be close to)
DAFT_USER_AGENT=...
DAFT_CF_CLEARANCE=...
```

## 4. Spin it up!
```zsh
source my-venv/bin/activate && source .env && python3 .
```
