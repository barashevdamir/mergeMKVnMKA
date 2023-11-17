import os
import subprocess

# Пути к папкам с видео и аудиофайлами
print('Введите путь к папке с видеофайлами:')
video_folder = input()
print('Введите путь к папке с аудиофайлами:')
audio_folder = input()
print('Введите путь к папке где сохранить результат:')
output_folder = input()

# Получаем списки видео и аудиофайлов
video_files = sorted([f for f in os.listdir(video_folder) if f.endswith('.mkv')])
audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith('.mka')])

# Убедимся, что количество видео и аудиофайлов совпадает
if len(video_files) != len(audio_files):
    print("Количество видео и аудиофайлов не совпадает!")
    exit()

# Объединяем видео с аудио
for video, audio in zip(video_files, audio_files):
    video_path = os.path.join(video_folder, video)
    audio_path = os.path.join(audio_folder, audio)
    output_path = os.path.join(output_folder, f'output_{video}')

    # Команда для ffmpeg
    cmd = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c copy -map 0:v -map 1:a "{output_path}"'

    # Запускаем процесс
    subprocess.run(cmd, shell=True)

print("Объединение файлов завершено.")
