#!/bin/sh
set -eu

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v ON_ERROR_STOP=1 \
  -c "CREATE DATABASE targeting_db"

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v ON_ERROR_STOP=1 -f /scripts/flags-init.sql
psql --username "$POSTGRES_USER" --dbname targeting_db \
  -v ON_ERROR_STOP=1 -f /scripts/targeting-init.sql
