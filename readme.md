# oryx

Oryx is a platform for:
- ingesting share market data and storing in a relational database
- backtesting trading strategies (currenlty under development)

Oryx is currenlty integrated with the following data sources:
- Sharadar Core US Fundamentals (SF1)
- Sharadar Core US Insiders Data (SF2)
- Sharadar Core US Institutional Investors Data (SF3)
- Sharadar Fund Prices (SFP)

## Database Instructions

### Windows

- Download and install Docker Desktop
- Run docker/docker_create.bat to create a container running the oryx database
- Run src/database/create.py to generate the database schema
- Run src/database/ingest/sharadar/load_from_tables.py to ingest Sharadar data from tables

## Backtester Instructions

Currently under development.