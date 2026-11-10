"""Controllo: trascrive ogni wav con Whisper e segnala parole in caratteri latini (es. istruzioni lette ad alta voce)."""
import sys, re, subprocess, numpy as np, soundfile as sf, sherpa_onnx
d = '/home/claude/tts/sherpa-onnx-whisper-small/'
asr = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d + 'small-encoder.int8.onnx', decoder=d + 'small-decoder.int8.onnx',
                                                 tokens=d + 'small-tokens.txt', language='', task='transcribe', num_threads=2)
bad = 0
for f in sys.argv[1:]:
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-ac', '1', '-ar', '16000', '/tmp/q.wav'])
    x, _ = sf.read('/tmp/q.wav'); x = x.astype(np.float32); txt = []
    for s in range(0, len(x), 16000 * 20):
        st = asr.create_stream(); st.accept_waveform(16000, x[s:s + 16000 * 20]); asr.decode_stream(st); txt.append(st.result.text)
    t = ' '.join(txt); lat = re.findall(r'[A-Za-z]{3,}', t)
    print(('ATTENZIONE ' if len(lat) > 2 else 'ok ') + f, round(len(x) / 16000, 1), 's', lat[:12])
    print('   ', t[:300]); bad += len(lat) > 2
sys.exit(1 if bad else 0)
