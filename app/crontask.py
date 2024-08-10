import os
import asyncio
import time


async def clean_old_files(directory: str, days_old: int):
    now = time.time()
    cutoff = now - (days_old * 86400)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_time = os.path.getmtime(file_path)
            if file_time < cutoff:
                os.remove(file_path)

# Использование:
# asyncio.run(clean_old_files("/path/to/files", 30))
