
# 動画フレーム抽出ツール

動画フレーム抽出ツールは、動画ファイル（.mov）からフレームを抽出し、それぞれのフレームを個別の画像ファイルとして保存するPython製のツールです。

## 必要な環境

- Python 3.7以上
- ffmpeg
- PySimpleGUI

## インストール

1. Pythonをインストールします（すでにインストール済みの場合はこの手順をスキップしてください）。Pythonの公式サイト（https://www.python.org/）から最新版をダウンロードし、インストーラに従ってインストールします。

2. ffmpegをインストールします。ffmpegの公式サイト（https://ffmpeg.org/download.html）から最新版をダウンロードし、インストーラに従ってインストールします。

3. PySimpleGUIをインストールします。コマンドプロンプトまたはターミナルを開き、以下のコマンドを実行します：

    ```
    pip install PySimpleGUI
    ```

4. このリポジトリをクローンまたはダウンロードします。

## 使い方

1. コマンドプロンプトまたはターミナルを開き、動画フレーム抽出ツールのスクリプトが存在するディレクトリに移動します。

2. 次のコマンドを実行して、動画フレーム抽出ツールを起動します：

    ```
    python main.py
    ```

3. GUI上で、動画ファイルが保存されているディレクトリと、抽出したフレームを保存するディレクトリを指定します。

4. "Run"ボタンをクリックして、フレームの抽出を開始します。

各動画ファイルから抽出したフレームは、指定した出力ディレクトリ内に、動画ファイルと同名のサブディレクトリに保存されます。

---

このREADMEは一例ですので、具体的な環境や使用方法に合わせて適宜調整してください。