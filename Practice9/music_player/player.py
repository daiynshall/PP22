from __future__ import annotations

from pathlib import Path
import pygame


class MusicPlayer:
    def __init__(self, music_folder: Path):
        self.music_folder = Path(music_folder)
        self.current_index = 0
        self.is_playing = False
        self.ignore_end_event = False

        self.audio_ready = self._init_mixer()
        self.tracks = self._load_tracks()
        self.track_lengths = self._read_track_lengths()

        self.music_end_event = pygame.USEREVENT + 1
        if self.audio_ready:
            pygame.mixer.music.set_endevent(self.music_end_event)

    def _init_mixer(self) -> bool:
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            return True
        except pygame.error:
            return False

    def _load_tracks(self) -> list[Path]:
        supported = {".wav", ".mp3", ".ogg"}

        # Ищет файлы и в подпапках тоже
        return sorted(
            path
            for path in self.music_folder.rglob("*")
            if path.is_file() and path.suffix.lower() in supported
        )

    def _read_track_lengths(self) -> dict[str, float]:
        lengths: dict[str, float] = {}

        if not self.audio_ready:
            return lengths

        for track in self.tracks:
            try:
                lengths[str(track)] = pygame.mixer.Sound(str(track)).get_length()
            except pygame.error:
                lengths[str(track)] = 0.0

        return lengths

    def has_tracks(self) -> bool:
        return len(self.tracks) > 0

    def get_current_track(self) -> Path | None:
        if not self.has_tracks():
            return None
        return self.tracks[self.current_index]

    def play(self) -> None:
        if not self.audio_ready or not self.has_tracks():
            return

        current_track = self.get_current_track()
        if current_track is None:
            return

        self.ignore_end_event = False
        pygame.mixer.music.load(str(current_track))
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self) -> None:
        self.is_playing = False

        if self.audio_ready:
            self.ignore_end_event = True
            pygame.mixer.music.stop()

    def next_track(self, autoplay: bool = True) -> None:
        if not self.has_tracks():
            return

        self.current_index = (self.current_index + 1) % len(self.tracks)

        if autoplay:
            self.play()

    def previous_track(self, autoplay: bool = True) -> None:
        if not self.has_tracks():
            return

        self.current_index = (self.current_index - 1) % len(self.tracks)

        if autoplay:
            self.play()

    def handle_event(self, event: pygame.event.Event) -> None:
        if not self.audio_ready:
            return

        if event.type == self.music_end_event:
            if self.ignore_end_event:
                self.ignore_end_event = False
                return

            if self.is_playing:
                self.next_track(autoplay=True)

    def get_position_seconds(self) -> float:
        if not self.audio_ready or not self.is_playing:
            return 0.0

        milliseconds = pygame.mixer.music.get_pos()
        if milliseconds < 0:
            return 0.0

        return milliseconds / 1000.0

    def get_track_length(self) -> float:
        current_track = self.get_current_track()
        if current_track is None:
            return 0.0

        return self.track_lengths.get(str(current_track), 0.0)

    def get_status_lines(self) -> list[str]:
        if not self.audio_ready:
            return ["Audio device is not available"]

        if not self.has_tracks():
            return [f"No tracks found in: {self.music_folder}"]

        track = self.get_current_track()
        status = "Playing" if self.is_playing else "Stopped"
        length = self.get_track_length()
        position = self.get_position_seconds()

        return [
            f"Status: {status}",
            f"Track: {track.name if track else 'None'}",
            f"Track {self.current_index + 1} of {len(self.tracks)}",
            f"Position: {position:05.1f}s / {length:05.1f}s",
            "Controls: P=Play  S=Stop  N=Next  B=Back  Q=Quit",
        ]