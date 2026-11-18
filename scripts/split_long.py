"""Divide un video lungo in parti (es. sotto i 15 minuti per i canali YouTube non verificati).
Uso: python3 scripts/split_long.py IN.mp4 OUT_PREFIX t1 t2 ...   (t = secondi dei tagli, di solito inizi di capitolo)
Crea OUT_PREFIX-p1.mp4, -p2.mp4, ... con dissolvenza di 0,4 s all'inizio e 1,2 s alla fine."""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor

src, pre, cuts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]))
pts = [0.0] + cuts + [dur]


def cut(k):
    a, b = pts[k], pts[k + 1]; d = b - a; fo = d - 1.2; out = f"{pre}-p{k + 1}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", src,
                    "-vf", f"fade=t=in:st=0:d=0.4,fade=t=out:st={fo}:d=1.2",
                    "-af", f"afade=t=in:st=0:d=0.4,afade=t=out:st={fo}:d=1.2",
                    "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-crf", "30", "-g", "300",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
    return out, d


with ThreadPoolExecutor(2) as ex:
    for out, d in ex.map(cut, range(len(pts) - 1)):
        print(out, f"{int(d // 60)}:{int(d % 60):02d}", "OK" if d < 14.9 * 60 else "TROPPO LUNGO")
