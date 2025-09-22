import csv
import subprocess
IDS_FILE = "ids.txt"
OUTPUT_CSV = "output.csv"
def fetch_file_content(file_id):
    cmd = [
        "gh", "api", file_id,
        "--jq", ".content"
    ]
    try:
        # Run the gh command and decode base64 output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        content_b64 = result.stdout.strip()
        if content_b64:
            # Decode base64 content
            decoded = subprocess.run(["base64", "--decode"], input=content_b64, capture_output=True, text=True, check=True)
            return decoded.stdout
        else:
            return ""
    except subprocess.CalledProcessError as e:
        print(f"Error fetching {file_id}: {e}")
        return ""
# Read file IDs from the text file
with open(IDS_FILE, "r", encoding="utf-8") as f:
    ids = [line.strip() for line in f if line.strip()]
# Fetch content for each ID
rows = []
for file_id in ids:
    content = fetch_file_content(file_id)
    rows.append({"id": file_id, "content": content})
# Write to CSV
with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["id", "content"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print(f"Fetched content for {len(rows)} files. Output written to {OUTPUT_CSV}")
