# Void Requiem 🚀

## Descripción
Un juego arcade donde controlas una nave espacial y debes derrotar oleadas de enemigos. Desarrollado con Python y Pygame, este juego te pone al mando de una nave espacial en una batalla contra invasores alienígenas.

## Requisitos Previos
- Python 3.x instalado en tu sistema
- pip (gestor de paquetes de Python) *(No necesario si usas la versión ejecutable)*

## Instalación
1. Clona o descarga este repositorio
2. Instala Pygame usando pip:
   ```sh
   pip install pygame
   ```

## Versión Ejecutable  
Si no quieres instalar nada, en la carpeta **`dist/`** encontrarás una versión ejecutable del juego.  
Solo necesitas ejecutar el archivo y ¡disfrutar la batalla espacial sin instalaciones extra! 🚀🎮  

## Estructura del Proyecto
```
void-requiem/
└──
├── main.py # Archivo principal del juego
├── config.py # Configuraciones y constantes
├── player.py # Clase del jugador
├── enemy.py # Clase de enemigos
├── bullet.py # Clase de proyectiles
├── buff.py # Clase de mejoras
│
└── assets/ # Recursos multimedia
├── background.jpg
├── laser.wav
└── explosion.wav
│
└── dist/ # Carpeta con la versión ejecutable del juego
├── VoidRequiem.exe (Windows) o VoidRequiem (Mac/Linux)
```

## Características
- Sistema de control intuitivo
  - Movimiento con flechas izquierda/derecha
  - Disparos con la tecla ESPACIO
- Sistema de oleadas progresivas (10 oleadas en total)
  - Dificultad progresiva (Fácil, Media, Difícil)
  - Jefe final en la oleada 10
- Sistema de menú completo
  - Menú principal
  - Pantalla de ayuda
  - Sistema de pausa
- Enemigos con patrones de movimiento aleatorio
- Sistema de puntuación
- Sistema de mejoras (power-ups)
  - Disparo doble temporal al alcanzar cada 1000 puntos
- Efectos de sonido para disparos y explosiones
- Gráficos espaciales inmersivos
- Sistema de colisiones
- Indicadores de dificultad por oleada
- Mensajes de transición entre oleadas
- Sistema de vida para el jefe final
- Pantallas de victoria y derrota

## Cómo jugar
1. **Ejecutar desde código:**  
   - Asegúrate de tener Python y Pygame instalados  
   - Navega hasta el directorio del juego  
   - Ejecuta el juego con:
     ```sh
     python main.py
     ```
2. **Ejecutar desde la versión compilada:**  
   - Ve a la carpeta `dist/`
   - Abre `VoidRequiem.exe` (Windows) o `VoidRequiem` (Mac/Linux)

## Desarrollo
El juego está desarrollado utilizando:
- Python 3.x
- Pygame para el motor de juego
- Sistema de estados para gestión de menús y pausas
- Sprites y assets personalizados

## Créditos
Los recursos multimedia (imágenes y sonidos) utilizados en este juego fueron obtenidos de [Pixabay](https://pixabay.com/)

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

