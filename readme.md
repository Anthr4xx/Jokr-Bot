# Discord Joke Bot

## Descripción

Bot de Discord que cuenta chistes en español e inglés utilizando **JokeAPI**. Arroja chistes de una o dos partes, con una pausa entre el set-up y el delivery del chiste.

---

## Características

- Comandos para obtener chistes en español e inglés.
- Manejo de chistes con una o dos partes.
- Implementación con `discord.py` y `requests`.
- Archivo `.env` para manejar el token de Discord.
- Uso de `pipenv` para gestión de dependencias.

---

## Instalación y Ejecución

Este proyecto puede instalarse utilizando Pipenv o pip con venv.

### Opción 1: Usando Pipenv (Recomendado)

1. Instalar Pipenv (si no está instalado):

   ```sh
   pip install pipenv
   ```

2. Instalar las dependencias:

   ```sh
   pipenv install
   ```

3. Activar el entorno virtual:

   ```sh
   pipenv shell
   ```

4. Editar el archivo `.env` y añadir el **TOKEN**:

   ```env
   DISCORD_BOT_TOKEN =  **TOKEN** 
   ```

5. Ejecutar la aplicación:

   ```sh
   python app.py
   ```

---

### Opción 2: Usando pip y venv

1. Crear un entorno virtual:

   ```sh
   python -m venv venv
   ```

2. Activar el entorno virtual:

   ```sh
   venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En Mac/Linux
   ```

3. Instalar las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

4. Editar el archivo `.env` y añadir el **TOKEN**:

   ```env
   DISCORD_BOT_TOKEN =  **TOKEN** 
   ```

5. Ejecutar la aplicación:

   ```sh
   python app.py
   ```

---

## Uso

### **Ejecutar el Bot**
```sh
python app.py
```

### **Comandos Disponibles**
| Comando | Descripción |
|---------|------------|
| `!chiste` | Cuenta un chiste en español. |
| `!joke` | Cuenta un chiste en inglés. |

Si el chiste tiene dos partes (setup y delivery), la segunda parte se enviará después de 3 segundos.

---

## Nota Final
- **El bot funciona de manera local**, se tendrá que ejecutar manualmente para poder usarlo.

