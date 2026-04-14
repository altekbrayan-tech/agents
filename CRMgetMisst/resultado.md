 Aquí tienes el código fuente base para el Sistema de Gestión de Clientes (CRM) "Soluciones Hidráulicas PH" siguiendo la arquitectura y diseño descritos en tu contexto:

### 3.2 Módulo de Ventas - Node.js con API RESTful

#### Dockerfile para el módulo de ventas
```dockerfile
# Utiliza una imagen base de Node.js
FROM node:14

# Crea y establece el directorio de trabajo
WORKDIR /app

# Copia los paquetes de la aplicación
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de la aplicación
COPY . .

# Expone el puerto en el que correrá la API
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]
```

#### `docker-compose.yml` para el módulo de ventas
```yaml
version: '3'
services:
  sales:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - ./app:/app
    environment:
      - NODE_ENV=production
    depends_on:
      - db

  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: crm_db
      POSTGRES_USER: crm_user
      POSTGRES_PASSWORD: password
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
```

#### `package.json` para la aplicación Node.js
```json
{
  "name": "crm-sales",
  "version": "1.0.0",
  "description": "Módulo de ventas del CRM Soluciones Hidráulicas PH",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "pg": "^8.5.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.6"
  }
}
```

### 3.1 Módulo de Clientes - Base de datos relacional (PostgreSQL)

#### `schema.sql` para la base de datos PostgreSQL
```sql
CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  phone VARCHAR(15),
  address TEXT
);

CREATE TABLE sales_opportunities (
  id SERIAL PRIMARY KEY,
  client_id INT REFERENCES clients(id),
  status VARCHAR(50),
  opportunity_value NUMERIC(10, 2)
);
```

### 3.3 Módulo de Marketing - Python/Flask

#### Dockerfile para el módulo de marketing
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

#### `requirements.txt` para el módulo de marketing
```
Flask==2.0.1
requests==2.25.1
```

### 3.4 Módulo de Servicio al Cliente - CMS con integración directa a la base de datos PostgreSQL

#### `config.yaml` para el CMS
```yaml
database:
  driver: postgres
  host: db
  port: 5432
  database: crm_db
  user: crm_user
  password: password
```

### Integración y Comunicación - API RESTful

#### Autenticación OAuth 2.0
Configuración de autenticación en el servidor (Node.js) y clientes externos utilizando tokens JWT.

#### `oauth_config.json`
```json
{
  "token_endpoint": "http://localhost:3000/oauth/token",
  "client_id": "your_client_id",
  "client_secret": "your_client_secret"
}
```

### Documentación técnica detallada en los archivos de código fuente y documentación adicional.