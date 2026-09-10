from pathlib import Path
import hashlib,json,subprocess,sys
from replay import collatz_packet,emergent_one_return
p=Path(__file__).resolve().parent
r=p.parents[1]
for name,digest in json.loads((p/'SHA256SUMS.json').read_text()).items():
    assert hashlib.sha256((r/name).read_bytes()).hexdigest()==digest,name
actual=json.loads(subprocess.check_output([sys.executable,str(p/'replay.py')],text=True))
assert actual==json.loads((p/'replay-result.json').read_text())
assert actual['status']=='PASS'
packet=collatz_packet(149)
packet['U']+=2
assert not emergent_one_return(packet)['certificate']['valid']
print('PASS: source hashes; 100000 odd addresses; four fixtures; corrupted packet rejected')
