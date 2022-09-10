Los ejercicios se ejecutan con la versión 10.22 sin instalación

# Windows
C:\Users\Iagovar\Desktop\postgreSQL

# Linux


# Cómo ejecutarlo sin las rutas en el PATH

## Windows

	https://stackoverflow.com/questions/26441873/starting-postgresql-and-pgadmin-in-windows-without-installation

	.\initdb.exe -D ..\pgdata -U postgres -W -E UTF8 -A scram-sha-256

	.\pg_ctl.exe -D ..\pgdata -l logfile start

	Con pgAdmin se puede administrar, simplemente doble click en el exe.


## Evitar que vaya tan lento pgadmin

Hay que cambiar las ``listen_addresses`` a ``127.0.0.1,::1`` en pgdata/postgresql.conf