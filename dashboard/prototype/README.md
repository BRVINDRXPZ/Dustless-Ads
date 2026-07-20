# Local Dashboard Prototype

> **SYNTHETIC DEMONSTRATION DATA — NOT BUSINESS PERFORMANCE.**

No credentials, APIs, remote databases, trackers, communications, or live services are used.

## Run

From repository root:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/dashboard/prototype/`. Do not deploy it.

## Test

```bash
python3 dashboard/prototype/tests/check_dashboard.py
```

The static Python server is required because browsers commonly block local `fetch()` from `file://`. Reset reloads the in-memory synthetic fixture; export creates only the currently filtered synthetic lead rows.
