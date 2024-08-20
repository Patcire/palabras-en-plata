# frontend/Dockerfile
FROM node:18

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto en el contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN npm install

# Comando por defecto para ejecutar
CMD ["npm", "run", "dev"]
