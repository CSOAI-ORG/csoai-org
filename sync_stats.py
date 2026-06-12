#!/usr/bin/env python3
"""Sync the GitHub repository count across all meta tags and text components."""

import os
import re
from datetime import datetime, timezone

REPO_COUNT = "369"
DOWNLOAD_COUNT = "200,000"

def get_eu_days():
    target_date = datetime(2026, 8, 2, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    delta = target_date - now
    return max(0, delta.days)

def sync_counts():
    eu_days = get_eu_days()
    for root, dirs, files in os.walk("public"):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()

                # Replace repo counts
                new_content = re.sub(r'\d+ repos', f"{REPO_COUNT} repos", content)
                new_content = re.sub(r'\d+ open-source repositories', f"{REPO_COUNT} open-source repositories", new_content)

                # Replace download counts
                new_content = re.sub(r'200,000 downloads', f"{DOWNLOAD_COUNT} downloads", new_content)
                new_content = re.sub(r'200K downloads', f"{DOWNLOAD_COUNT.replace(',000', 'K')} downloads", new_content)

                # Replace EU AI Act countdown
                new_content = re.sub(r'EU AI Act: \d+ days', f"EU AI Act: {eu_days} days", new_content)
                new_content = re.sub(r'EU AI Act Article 50 enforcement begins in \d+ days', f"EU AI Act Article 50 enforcement begins in {eu_days} days", new_content)

                if new_content != content:
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"✓ Synced {file}")

if __name__ == "__main__":
    sync_counts()
