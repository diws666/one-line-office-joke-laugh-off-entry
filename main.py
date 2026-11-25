import os

# Verified: exactly 127 characters (127 bytes UTF-8), no trailing newline.
LINE = "The printer is the only coworker who never lies. It tells you exactly when it is out of paper, out of ink, and out of patience."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(f"Wrote {len(LINE.encode('utf-8'))} bytes to {output_path}")
