"""Genera la voce darija con Gemini TTS per ogni job in tts/jobs/*.json che non ha ancora audio.

Job JSON:
{
  "voice": "Charon",
  "model": "gemini-3.8-flash-lite-tts",
  "style": "Read this as ...:",
  "blocks": {"01": "testo arabo", "02": "..."}
}
Output: tts/audio/<job>/<blocco>.wav (PCM 24 kHz mono) + status.json
"""
import base64, glob, json, os, sys, time, urllib.error, urllib.request, wave

KEY = os.environ.get("GEMINI_API_KEY", "").strip()
API = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent"


def synth(model, voice, text):
    body = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    req = urllib.request.Request(
        API.format(model), data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": KEY}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.load(r)
    for part in data["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            return base64.b64decode(part["inlineData"]["data"])
    raise RuntimeError("nessun audio nella risposta: " + json.dumps(data)[:500])


def main():
    status_all = {}; stop = set()
    for job_path in sorted(glob.glob("tts/jobs/*.json")):
        name = os.path.splitext(os.path.basename(job_path))[0]
        out = f"tts/audio/{name}"
        os.makedirs(out, exist_ok=True)
        job = json.load(open(job_path, encoding="utf-8"))
        model = job.get("model", "gemini-3.8-flash-lite-tts")
        voice = job.get("voice", "Charon")
        style = job.get("style", "").strip()
        if "lite" not in model:  # il modello Flash (non lite) legge ad alta voce l'istruzione: solo testo
            style = ""
        st = {"model": model, "voice": voice, "ok": [], "errors": {}}
        if not KEY:
            st["errors"]["_"] = "Manca il secret GEMINI_API_KEY nella repository"
        for bid, text in sorted(job["blocks"].items()):
            wav = f"{out}/{bid}.wav"
            if os.path.exists(wav) or not KEY or model in stop:
                continue
            prompt = f"{style}\n\n{text}" if style else text
            for attempt in range(6):
                try:
                    pcm = synth(model, voice, prompt)
                    with wave.open(wav, "wb") as w:
                        w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm)
                    st["ok"].append(bid)
                    st["errors"].pop(bid, None)
                    print(name, bid, "ok", round(len(pcm) / 48000, 1), "s")
                    break
                except urllib.error.HTTPError as e:
                    msg = f"HTTP {e.code}: {e.read().decode(errors='replace')[:1500]}"
                    st["errors"][bid] = msg
                    print(name, bid, msg)
                    if e.code == 429 and ("PerDay" in msg or "per day" in msg.lower() or "daily" in msg.lower()):
                        st["errors"]["_"] = "Limite giornaliero gratuito raggiunto"
                        json.dump(st, open(f"{out}/status.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                        print(json.dumps(st, ensure_ascii=False)); stop.add(model); break
                    if e.code in (429, 500, 503) and attempt < 3:
                        time.sleep(20 * (attempt + 1))
                        continue
                    break
                except Exception as e:  # noqa
                    st["errors"][bid] = repr(e)[:400]
                    print(name, bid, repr(e))
                    time.sleep(10)
            json.dump(st, open(f"{out}/status.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            time.sleep(4)  # resta sotto il limite al minuto del piano gratuito
        json.dump(st, open(f"{out}/status.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        status_all[name] = st
    print(json.dumps(status_all, ensure_ascii=False)[:2000])


if __name__ == "__main__":
    sys.exit(main())
