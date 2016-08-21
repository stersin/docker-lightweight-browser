# Docker : Lightweight webkit based browser

## Prerequisites

Add docker to host x server access control list :

```xhost +local:docker```

## Usage

```docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix stersin/lightweight-browser http://www.google.fr```
