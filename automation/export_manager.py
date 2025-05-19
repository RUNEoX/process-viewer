import csv
import json
from datetime import datetime

class ExportManager:
    @staticmethod
    def export_json(data, filepath=None):
        if not filepath:
            filepath = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def export_csv(data, filepath=None):
        if not filepath:
            filepath = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        if not data:
            raise ValueError("No data to export")

        keys = data[0].keys()
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

