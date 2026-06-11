#!/usr/bin/env python3
"""Sync the GitHub repository count across all meta tags and text components."""

import os
import re

REPO_COUNT = "369"
DOWNLOAD_COUNT = "200,000"

def sync_counts():
    for root, dirs, files in os.walk("public"):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                # Replace repo counts
                new_content = re.sub(r'\d+ repos', f"{REPO_COUNT} repos", content)
                # Replace download counts
                new_content = re.sub(r'200,000 downloads', f"{DOWNLOAD_COUNT} downloads", new_content)
                new_content = re.sub(r'200K downloads', f"{DOWNLOAD_COUNT.replace(',000', 'K')} downloads", new_content)
                
                if new_content != content:
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"✓ Synced {file}")

if __name__ == "__main__":
    sync_counts()
