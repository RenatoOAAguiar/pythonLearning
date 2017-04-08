#Usar essa instalação https://github.com/RenatoOAAguiar/pythonLearning.git

import cmu_sphinx4

audio_url = "1.mp3"
transcriber = cmu_sphinx4.Transcriber(audio_url)

for line in transcriber.transcript_stream():
    print(line)


