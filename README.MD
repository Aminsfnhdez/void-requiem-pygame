# Void Requiem 🚀

## Descripción
Un juego arcade donde controlas una nave espacial y debes derrotar oleadas de enemigos. Desarrollado con Python y Pygame, este juego te pone al mando de una nave espacial en una batalla contra invasores alienígenas.

## Requisitos Previos
- Python 3.x instalado en tu sistema
- pip (gestor de paquetes de Python)

## Instalación
1. Clona o descarga este repositorio
2. Instala Pygame usando pip:
`pip install pygame`

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
```

## Características
- Sistema de control intuitivo
  - Movimiento con flechas izquierda/derecha
  - Disparos con la tecla ESPACIO
- Sistema de oleadas progresivas (10 oleadas en total)
- Enemigos con patrones de movimiento aleatorio
- Sistema de puntuación
- Sistema de mejoras (power-ups)
  - Disparo doble temporal al alcanzar cierta puntuación
- Efectos de sonido para disparos y explosiones
- Gráficos espaciales inmersivos
- Sistema de colisiones
- Pantalla de inicio
- Mensajes de transición entre oleadas
- Pantalla de victoria al completar todas las oleadas

## Cómo jugar
1. Asegúrate de tener todos los requisitos instalados
2. Navega hasta el directorio del juego
3. Ejecuta el juego: main.py

## Desarrollo
El juego está desarrollado utilizando:
- Python 3.x
- Pygame para el motor de juego
- Sprites y assets personalizados

## Créditos
Los recursos multimedia (imágenes y sonidos) utilizados en este juego fueron obtenidos de [Pixabay](https://pixabay.com/)

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
