# Crear un directorio llamado "practica-git"
mkdir practica-git

# Moverse al directorio "practica-git"
cd practica-git

# Inicializar un repositorio git en el directorio "practica-git"
git init

# Crear un archivo llamado "archivo-de-texto.txt" en el directorio "practica-git"
touch archivo-de-texto.txt

# Realizar 10 commits sobre el archivo "archivo-de-texto.txt" en la rama "master"
for ((i=0; i<10; i++)); do
  # Modificar el archivo "archivo-de-texto.txt"
  echo "Commit en MASTER número $i" >> archivo-de-texto.txt

  # Añadir el archivo al staging area
  git add archivo-de-texto.txt

  # Realizar el commit
  git commit -m "Commit en MASTER número $i"
done

# Crear una rama llamada "feature" a partir del segundo commit de la rama "master"
git branch feature HEAD~8

# Cambiar a la rama "feature"
git checkout feature

# Crear un archivo llamado "feature.txt" en el directorio "practica-git"
touch feature.txt

# Realizar 10 commits sobre el archivo "feature.txt" en la rama "feature"
for ((i=0; i<10; i++)); do
  # Modificar el archivo "feature.txt"
  echo "Commit en FEATURE número $i" >> feature.txt

  # Añadir el archivo al staging area
  git add feature.txt

  # Realizar el commit
  git commit -m "Commit en FEATURE número $i"
done

# Volvemos a la rama main
git checkout master