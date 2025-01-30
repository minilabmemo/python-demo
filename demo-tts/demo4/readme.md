# 功能

希望逐行翻譯音黨，中間要加入 幾秒靜音。

## 安裝

```
brew install ffmpeg

FFmpeg 是一個開放原始碼的自由軟體，可以執行音訊和視訊多種格式的錄影、轉檔、串流功能
需下載一段時間...似乎很大

==> Installing ffmpeg dependency: icu4c
==> Pouring icu4c--74.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/icu4c/74.2: 270 files, 77.3MB
==> Installing ffmpeg dependency: harfbuzz
==> Pouring harfbuzz--9.0.0.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/harfbuzz/9.0.0: 77 files, 10MB
==> Installing ffmpeg dependency: lame
==> Pouring lame--3.100.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/lame/3.100: 27 files, 2.2MB
==> Installing ffmpeg dependency: fribidi
==> Pouring fribidi--1.0.15.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/fribidi/1.0.15: 68 files, 702.2KB
==> Installing ffmpeg dependency: libunibreak
==> Pouring libunibreak--6.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libunibreak/6.1: 18 files, 315.2KB
==> Installing ffmpeg dependency: libass
==> Pouring libass--0.17.3.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libass/0.17.3: 12 files, 700.5KB
==> Installing ffmpeg dependency: libbluray
==> Pouring libbluray--1.3.4.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libbluray/1.3.4: 21 files, 908.8KB
==> Installing ffmpeg dependency: cjson
==> Pouring cjson--1.7.18.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/cjson/1.7.18: 24 files, 221.4KB
==> Installing ffmpeg dependency: libmicrohttpd
==> Pouring libmicrohttpd--1.0.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libmicrohttpd/1.0.1: 25 files, 1.5MB
==> Installing ffmpeg dependency: mbedtls
==> Pouring mbedtls--3.6.0.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/mbedtls/3.6.0: 198 files, 13MB
==> Installing ffmpeg dependency: librist
==> Pouring librist--0.2.10_1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/librist/0.2.10_1: 28 files, 713.7KB
==> Installing ffmpeg dependency: libsoxr
==> Pouring libsoxr--0.1.3.ventura.bottle.1.tar.gz
🍺  /usr/local/Cellar/libsoxr/0.1.3: 29 files, 319.7KB
==> Installing ffmpeg dependency: libssh
==> Pouring libssh--0.10.6.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libssh/0.10.6: 23 files, 1.2MB
==> Installing ffmpeg dependency: libvidstab
==> Pouring libvidstab--1.1.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libvidstab/1.1.1: 25 files, 169.5KB
==> Installing ffmpeg dependency: libogg
==> Pouring libogg--1.3.5.ventura.bottle.2.tar.gz
🍺  /usr/local/Cellar/libogg/1.3.5: 103 files, 520.8KB
==> Installing ffmpeg dependency: libvorbis
==> Pouring libvorbis--1.3.7.ventura.bottle.1.tar.gz
🍺  /usr/local/Cellar/libvorbis/1.3.7: 157 files, 2.3MB
==> Installing ffmpeg dependency: libvpx
==> Pouring libvpx--1.13.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libvpx/1.13.1: 20 files, 5.2MB
==> Installing ffmpeg dependency: opencore-amr
==> Pouring opencore-amr--0.1.6.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/opencore-amr/0.1.6: 17 files, 677.6KB
==> Installing ffmpeg dependency: openjpeg
==> Pouring openjpeg--2.5.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/openjpeg/2.5.2: 538 files, 14.0MB
==> Installing ffmpeg dependency: opus
==> Pouring opus--1.5.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/opus/1.5.2: 15 files, 1MB
==> Installing ffmpeg dependency: rav1e
==> Pouring rav1e--0.7.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/rav1e/0.7.1: 14 files, 49.6MB
==> Installing ffmpeg dependency: libsamplerate
==> Pouring libsamplerate--0.2.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libsamplerate/0.2.2: 32 files, 3MB
==> Installing ffmpeg dependency: flac
==> Pouring flac--1.4.3.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/flac/1.4.3: 284 files, 6.9MB
==> Installing ffmpeg dependency: mpg123
==> Pouring mpg123--1.32.6.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/mpg123/1.32.6: 33 files, 1.8MB
==> Installing ffmpeg dependency: libsndfile
==> Pouring libsndfile--1.2.2.ventura.bottle.2.tar.gz
🍺  /usr/local/Cellar/libsndfile/1.2.2: 54 files, 1.7MB
==> Installing ffmpeg dependency: rubberband
==> Pouring rubberband--3.3.0.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/rubberband/3.3.0: 13 files, 1.7MB
==> Installing ffmpeg dependency: sdl2
==> Pouring sdl2--2.30.5.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/sdl2/2.30.5: 94 files, 6.5MB
==> Installing ffmpeg dependency: snappy
==> Pouring snappy--1.2.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/snappy/1.2.1: 19 files, 161.5KB
==> Installing ffmpeg dependency: speex
==> Pouring speex--1.2.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/speex/1.2.1: 25 files, 804.4KB
==> Installing ffmpeg dependency: srt
==> Pouring srt--1.5.3.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/srt/1.5.3: 20 files, 4.4MB
==> Installing ffmpeg dependency: svt-av1
==> Pouring svt-av1--2.1.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/svt-av1/2.1.2: 19 files, 5MB
==> Installing ffmpeg dependency: leptonica
==> Pouring leptonica--1.84.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/leptonica/1.84.1: 56 files, 6.1MB
==> Installing ffmpeg dependency: libb2
==> Pouring libb2--0.98.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libb2/0.98.1: 8 files, 273.7KB
==> Installing ffmpeg dependency: libarchive
==> Pouring libarchive--3.7.4.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libarchive/3.7.4: 64 files, 3.7MB
==> Installing ffmpeg dependency: pango
==> Pouring pango--1.54.0.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/pango/1.54.0: 69 files, 3.3MB
==> Installing ffmpeg dependency: tesseract
==> Pouring tesseract--5.4.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/tesseract/5.4.1: 75 files, 32.7MB
==> Installing ffmpeg dependency: theora
==> Pouring theora--1.1.1.ventura.bottle.4.tar.gz
🍺  /usr/local/Cellar/theora/1.1.1: 97 files, 2MB
==> Installing ffmpeg dependency: x264
==> Pouring x264--r3108.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/x264/r3108: 11 files, 5.7MB
==> Installing ffmpeg dependency: x265
==> Pouring x265--3.6.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/x265/3.6: 11 files, 36.1MB
==> Installing ffmpeg dependency: xvid
==> Pouring xvid--1.3.7.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/xvid/1.3.7: 10 files, 1.3MB
==> Installing ffmpeg dependency: libsodium
==> Pouring libsodium--1.0.20.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libsodium/1.0.20: 78 files, 1.1MB
==> Installing ffmpeg dependency: zeromq
==> Pouring zeromq--4.3.5_1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/zeromq/4.3.5_1: 84 files, 6.2MB
==> Installing ffmpeg dependency: zimg
==> Pouring zimg--3.0.5.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/zimg/3.0.5: 27 files, 2.3MB
==> Installing ffmpeg
==> Pouring ffmpeg--7.0.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/ffmpeg/7.0.1: 287 files, 54.8MB
==> Running `brew cleanup ffmpeg`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).



```

- pip3 install pydub

```
方法一
brew install pipx 安裝
pipx install pydub 沒有用
brew uninstall pipx 沒有用解安裝
Uninstalling /usr/local/Cellar/pipx/1.6.0... (214 files, 1.6MB)

方法二
首先创建并激活一个虚拟环境：
python3 -m venv myenv
source myenv/bin/activate
再次安裝
pip3 install pydub
Installing collected packages: pydub
Successfully installed pydub-0.25.1




```

## 執行

可能無法直接右鍵按下執行，會出現找不到 moudule，所以要去本資料夾下指令。

- 執行 python3 main.py

  - cd 到本資料夾
  - pip3 install gtts 可能需要再次安裝
