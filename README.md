# AntiAFK

Herramienta Anti-AFK desarrollada originalmente para Star Citizen. Simula actividad del usuario para evitar ser desconectado por inactividad.

> ⚠️ **Nota:** Esta herramienta no funciona con Star Citizen debido al sistema de seguridad a nivel de kernel del juego (anti-cheat). Se publica como proyecto de referencia y podría adaptarse a otros juegos o aplicaciones.

## ¿Qué hace?

Ejecuta acciones automáticas en segundo plano (movimientos de ratón, pulsaciones de tecla) para simular actividad y evitar el kick por AFK.

## Tecnologías

- **Python**
- **PyAutoGUI / pynput** — simulación de entrada de teclado y ratón
- **PyInstaller** — empaquetado como ejecutable Windows

## Uso

Descarga el ejecutable desde [Releases](https://github.com/Alowster/AntiAFK/releases) y ejecútalo mientras juegas.

Para ejecutar desde el código fuente:

```bash
git clone https://github.com/Alowster/AntiAFK.git
cd AntiAFK
python main.py
```

## Limitaciones conocidas

- No compatible con juegos que usan anti-cheat a nivel de kernel (Star Citizen, Valorant, etc.)
- Solo para Windows

## Autor

[Alowster](https://github.com/Alowster)
