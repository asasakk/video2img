import os
import subprocess
import PySimpleGUI as sg

def extract_frames(movie_dir, output_dir):
    if not os.path.exists(movie_dir):
        print(f"The directory {movie_dir} does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(movie_dir):
        if file_name.lower().endswith(".mov"):
            movie_path = os.path.join(movie_dir, file_name)
            movie_name = os.path.splitext(file_name)[0]
            movie_output_dir = os.path.join(output_dir, movie_name)
            os.makedirs(movie_output_dir, exist_ok=True)
            output_path = os.path.join(movie_output_dir, f"{movie_name}_frame%04d.png")
            command = f'ffmpeg -i "{movie_path}" "{output_path}"'
            try:
                subprocess.run(command, shell=True, check=True)
            except (subprocess.CalledProcessError, Exception) as e:
                print(f"Error occurred while processing {file_name}: {str(e)}")

layout = [
    [sg.Text("Movie directory"), sg.Input(), sg.FolderBrowse()],
    [sg.Text("Output directory"), sg.Input(), sg.FolderBrowse()],
    [sg.Button("Run"), sg.Button("Cancel")]
]

window = sg.Window("Movie Frame Extractor", layout)
while True:
    event, values = window.read()
    if event == "Run":
        extract_frames(values[0], values[1])
    elif event in ("Cancel", sg.WINDOW_CLOSED):
        break

window.close()
