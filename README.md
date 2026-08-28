# 🚨 Accident Detection and Alert System

## Project Overview

This project is an IoT-based accident detection and alert system.

The system uses a Raspberry Pi, MPU6050 accelerometer and NEO-6M GPS module to detect possible vehicle accidents and obtain the accident location.

The accident information can then be sent through Telegram and displayed through a Flutter mobile application.

## Hardware

- Raspberry Pi
- MPU6050 Accelerometer/Gyroscope
- NEO-6M GPS Module

## Software

- Python
- Flutter
- Dart
- Telegram Bot API

## System Architecture

```text
MPU6050
   ↓
Raspberry Pi
   ↓
Acceleration Analysis
   ↓
Accident Detection
   ↓
NEO-6M GPS
   ↓
Latitude + Longitude
   ↓
Telegram Alert
   ↓
Flutter Application
```
