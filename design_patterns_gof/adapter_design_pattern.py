"""
Adapter design pattern:
The Adapter design pattern is a structural design pattern that allows two incompatible
interfaces to work together. It acts as a bridge between two interfaces, enabling them
to collaborate without modifying their source code. The Adapter pattern is particularly
useful when you want to reuse an existing class that doesn't quite fit the interface you
need, or when you want to provide a consistent interface to a set of classes with different
interfaces.
"""

from abc import ABC, abstractmethod

from loguru import logger


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, media_format: str, file_name: str):
        pass


class MP3Player(MediaPlayer):

    def play(self, media_format: str, file_name: str):
        logger.info(f"Playing media with MP3 format using file {file_name}")


class ModernMediaPlayer:
    def __init__(self, file_name: str):
        self._file_name = file_name

    def play_with_vlc(self):
        logger.info(f"Playing media with VLC format using file {self._file_name}")

    def play_with_mp4(self):
        logger.info(f"Playing media with MP4 format using file {self._file_name}")


class ModernMediaPlayerAdapter(MediaPlayer):
    def __init__(self, modern_media_player: ModernMediaPlayer):
        self._modern_media_player = modern_media_player

    def play(self, media_format: str, file_name: str):
        if media_format == "VLC":
            self._modern_media_player.play_with_vlc()
        if media_format == "MP4":
            self._modern_media_player.play_with_mp4()


def main():
    media_format = input("What is the format of media file? MP3, VLC or MP4 \n")
    file_name = input("Give the media file name. \n")

    mp3_player = MP3Player()
    modern_media_player_adapter = ModernMediaPlayerAdapter(ModernMediaPlayer(file_name=file_name))

    if media_format == "MP3":
        mp3_player.play(media_format=media_format, file_name=file_name)

    if media_format in ["VLC", "MP4"]:
        modern_media_player_adapter.play(media_format=media_format, file_name=file_name)


if __name__ == "__main__":
    main()

# EOF
