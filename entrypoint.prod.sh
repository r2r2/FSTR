#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
	echo "Waiting for postgres..."

	while ! nc -z $FSTR_DB_HOST $FSTR_DB_PORT ; do
		sleep 0.1
	done

	echo "PostgreSQL started"
fi


exec "$@"