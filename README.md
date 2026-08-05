# Widget Service , CircleCI Demo

A tiny Flask API used to demo a CircleCI pipeline live.

- `GET /health` , returns ok
- `GET /widgets/count` , returns the number of widgets in stock

## The pipeline
`.circleci/config.yml` runs one job: install dependencies, then run the tests.
If a change breaks a test, the build goes red and nothing ships.

## The demo
1. Show the repo and the last green build.
2. Push a change that breaks `test_widget_count` (add a 4th widget so count returns 4, not 3).
3. Watch the build go red in CircleCI, live.
4. Push the fix (remove the 4th widget). Build goes green.
5. That red build is the bug that never reached production.

## Python Notes
the venv creation was silently failing in the container (the python -m venv venv step).
Removing it was both the fix and the more correct approach , in an ephemeral CI container you don't need a venv, the container is already isolated.
Cleaner config, and it matches how real CircleCI Python pipelines usually look.
