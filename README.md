## Описание
Этот проект реализует определение наличия или отсутствия руки человека в кадре с веб-камеры в режиме реального времени.
This project implements real-time detection of the presence or absence of a human hand in a webcam frame.

**Выводимая информация на экране**
*   Видеопоток с камеры / Live camera feed
*   Статус обнаружения руки (DETECTED / NOT FOUND)
*   Текущий показатель FPS

## Установка и запуск
1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ВАШ_НИКНЕЙМ/HandDetector.git
    cd HandDetector
    ```
2.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Скачайте файл модели `hand_landmarker.task`** с [официального источника](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task) и поместите его в корень папки проекта (рядом с `HandDetector.py`).
4.  Запустите программу:
    ```bash
    python HandDetector.py
    ```
5.  Для выхода нажмите клавишу **'q'** в окне программы.

## Технологии
*   Python 3
*   OpenCV (для работы с видео)
*   MediaPipe Tasks API (для обнаружения руки)
