import json
import subprocess 

tailscaleStatus = subprocess.run(['tailscale', 'status', '--json'], capture_output=True, text=True) 
x = json.loads(tailscaleStatus.stdout.replace('\\n', '\n'))
print(json.dumps(x, indent=4))
