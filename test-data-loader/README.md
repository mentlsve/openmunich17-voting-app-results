# Test data loader

This is a helper to create the `votes` table and insert some data so the result screen can be tested.

## Usage

1. Build the container
```
# Assuming we are currently at the repository root
cd test-data-loader
bash$ docker build -t test-data-loader .
```
2. Start a postgres db (skip if you have a running posgres instance you want to use). Using the default postgres image, documentation is [here](https://hub.docker.com/_/postgres/)
```
bash$ docker run --name results-test-db -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
3. Get the IP/Hostname of the postgres db (skip if you already have an IP/Hostname)
```
bash$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' results-test-db
172.17.0.2
```
4. Load the test data
```
bash$ docker run --rm -e 'PGHOST=172.17.0.2' test-data-loader
Inserted 20 values in table votes (PGDATABASE=postgres, PGHOST=172.17.0.2, PGUSER=postgres)
```

## Notes

I am not using container links because this is [deprecated](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/) and no time for user-defined networks which would make it possible to resolve IPs by container name.