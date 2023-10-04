<p align="center">
  <img src="./docs/vinorsoft_logo.png" width="150">
  <br />
  <br />
  <a href="http://www.vinorsoft.com/"><img alt="Auth Vinorsoft" src="https://img.shields.io/badge/Auth-Vinorsoft-FFD500?style=flat&labelColor=005BBB" /></a>
  <a href="https://github.com/pytorch/fairseq/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
  <a href="https://github.com/optimuskonboi"><img alt="Instructor DanPV" src="https://img.shields.io/badge/Instructor-DanPV-FFD500?style=flat&labelColor=005BBB" /></a>
  <a href="https://github.com/giangnv125"><img alt="Deployer GiangNV" src="https://img.shields.io/badge/Deployer-GiangNV-FFD500?style=flat&labelColor=005BBB" /></a>
</p>

--------------------------------------------------------------------------------
## Text To Speech Processing
- Xử lý text2speech dựa trên gTTS package (đây là package gọi đến Translate Google API để xử lý text to speech) tại [repo này](https://github.com/pndurette/gTTS)
### Installation & Run
- Install package gTTS để xử lý text2speech và package playsound để phát tệp .mp3 sau khi xử lý text2speech
```shell
pip install gTSS
pip install playsound
```
- Run file `main.py` để chuyển đổi text theo từng line từ file `input_text/input_text.py` thành file speech .mp3 vào folder `speech_dir`