# Results voting app

This is the results app part only from Docker's [example voting app](https://github.com/dockersamples/example-voting-app).

It has been slightly modified
* to use node-postgres 7.4.0 which makes it cleaner by using a configuration object instead of a connection string, see [new Pool([config: object])](https://node-postgres.com/api/pool)
* to allow specifying the postgres connection configuration through environment variables

## Prerequisites

You need a postgres database running, in best case with some data. You can use the test data loader and the standard postgres image as described [here](test-data-loader/README.md) (it is pretty straightforward with 4 steps).

Once you have your postgres database, we need its IP/hostname. In case you were following the [previous steps](test-data-loader/README.md) you can get it like:

```
TEST_DB_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' results-test-db)
```

## Build & Run

1. Build the image

```
# Assuming we are currently at the repository root
bash$ docker build -t result-voting-app .
```

2. Run the container
```
bash$ docker run --name ui -p 80:80 -e "PGHOST=$TEST_DB_HOST" result-voting-app
```

3. Access the app under localhost:80

## Just Run

An automatic build has been created on Docker hub so you can also do a

```
bash$ docker run --name ui -p 80:80 -e "PGHOST=$TEST_DB_HOST" mentlsve/openmunich17-voting-app-results
```