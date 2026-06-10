
"""
Advanced E-Waste Data Sanitization System
Features:
- Multi-pass secure deletion
- SHA256 hashing
- Batch deletion
- Folder sanitization
- Large file scanner
- Duplicate file detection
- File type analytics
- Audit logging (CSV)
- Audit report generation
"""

import os
import csv
import hashlib
import secrets
import shutil
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

REPORT_FILE = "deletion_report.csv"


class EWasteSanitizer:

    def __init__(self):
        self.total_files_deleted = 0
        self.total_bytes_deleted = 0

        if not os.path.exists(REPORT_FILE):
            with open(REPORT_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["Timestamp", "File", "Size", "SHA256", "Status"]
                )

    def calculate_hash(self, file_path):
        sha = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha.update(chunk)
        return sha.hexdigest()

    def log(self, file_path, size, file_hash, status):
        with open(REPORT_FILE, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([
                datetime.now(),
                file_path,
                size,
                file_hash,
                status
            ])

    def overwrite(self, file_path, passes=3):
        size = os.path.getsize(file_path)

        for p in range(1, passes + 1):
            print(f"Pass {p}/{passes}")
            with open(file_path, "r+b") as f:
                remaining = size
                while remaining > 0:
                    chunk = min(4096, remaining)
                    f.write(secrets.token_bytes(chunk))
                    remaining -= chunk
                f.flush()
                os.fsync(f.fileno())

    def secure_delete_file(self, file_path, passes=3):
        if not os.path.isfile(file_path):
            print("File not found.")
            return

        try:
            size = os.path.getsize(file_path)
            file_hash = self.calculate_hash(file_path)

            self.overwrite(file_path, passes)

            new_name = os.path.join(
                Path(file_path).parent,
                secrets.token_hex(16)
            )

            os.rename(file_path, new_name)
            os.remove(new_name)

            self.total_files_deleted += 1
            self.total_bytes_deleted += size

            self.log(file_path, size, file_hash, "DELETED")

            print("Secure deletion successful.")

        except Exception as e:
            print("Error:", e)

    def secure_delete_folder(self, folder, passes=3):
        for root, _, files in os.walk(folder):
            for file in files:
                self.secure_delete_file(
                    os.path.join(root, file),
                    passes
                )

        shutil.rmtree(folder, ignore_errors=True)
        print("Folder sanitized successfully.")

    def batch_delete(self, folder, extension):
        count = 0

        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(extension):
                    self.secure_delete_file(
                        os.path.join(root, file),
                        3
                    )
                    count += 1

        print(f"Deleted {count} matching files.")

    def scan_large_files(self, folder):
        print("\nLarge Files (>10MB)\n")

        for root, _, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)

                try:
                    size = os.path.getsize(path)

                    if size > 10 * 1024 * 1024:
                        print(
                            f"{file} -> "
                            f"{size/(1024*1024):.2f} MB"
                        )
                except:
                    pass

    def file_type_analytics(self, folder):
        stats = Counter()

        for root, _, files in os.walk(folder):
            for file in files:
                ext = Path(file).suffix.lower()

                if ext:
                    stats[ext] += 1

        print("\nFILE TYPE ANALYTICS")
        print("-" * 40)

        for ext, count in stats.most_common():
            print(f"{ext:<10} : {count}")

    def find_duplicates(self, folder):
        hashes = defaultdict(list)

        for root, _, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)

                try:
                    file_hash = self.calculate_hash(path)
                    hashes[file_hash].append(path)
                except:
                    pass

        print("\nDUPLICATE FILES")
        print("-" * 40)

        found = False

        for _, paths in hashes.items():
            if len(paths) > 1:
                found = True
                print()
                for p in paths:
                    print(p)

        if not found:
            print("No duplicates found.")

    def statistics(self):
        print("\nSTATISTICS")
        print("-" * 40)
        print("Files Deleted :", self.total_files_deleted)
        print("Bytes Deleted :", self.total_bytes_deleted)
        print(
            "MB Recovered  :",
            round(self.total_bytes_deleted / (1024 * 1024), 2)
        )

    def generate_audit_report(self):
        report = f"audit_report_{datetime.now():%Y%m%d_%H%M%S}.txt"

        with open(report, "w", encoding="utf-8") as f:
            f.write("ADVANCED E-WASTE AUDIT REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated : {datetime.now()}\n")
            f.write(f"Files Deleted : {self.total_files_deleted}\n")
            f.write(f"Bytes Deleted : {self.total_bytes_deleted}\n")

        print("Audit report created:", report)


def main():
    app = EWasteSanitizer()

    while True:
        print("\n" + "=" * 60)
        print("ADVANCED E-WASTE DATA SANITIZATION SYSTEM")
        print("=" * 60)
        print("1. Secure Delete File")
        print("2. Secure Delete Folder")
        print("3. Batch Delete Files")
        print("4. Scan Large Files")
        print("5. File Type Analytics")
        print("6. Duplicate File Detection")
        print("7. View Statistics")
        print("8. Generate Audit Report")
        print("9. Exit")

        choice = input("\nEnter Choice: ").strip()

        if choice == "1":
            app.secure_delete_file(
                input("File Path: "),
                int(input("Passes (1/3/7): "))
            )

        elif choice == "2":
            app.secure_delete_folder(
                input("Folder Path: "),
                int(input("Passes (1/3/7): "))
            )

        elif choice == "3":
            app.batch_delete(
                input("Folder Path: "),
                input("Extension (e.g .tmp): ")
            )

        elif choice == "4":
            app.scan_large_files(input("Folder Path: "))

        elif choice == "5":
            app.file_type_analytics(input("Folder Path: "))

        elif choice == "6":
            app.find_duplicates(input("Folder Path: "))

        elif choice == "7":
            app.statistics()

        elif choice == "8":
            app.generate_audit_report()

        elif choice == "9":
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
