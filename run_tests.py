import subprocess
import os
from datetime import datetime
import sys
import configparser

# katalog główny projektu
project_root = os.path.dirname(os.path.abspath(sys.argv[0]))

# katalog z raportami
reports_dir = os.path.join(project_root, "reports")
os.makedirs(reports_dir, exist_ok=True)

# katalog z testami
tests_dir = os.path.join(project_root, "tests")

# ścieżka do pliku .ini
ini_file_path = os.path.join(project_root, "test_config.ini")

# wczytaj konfigurację z pliku .ini
config = configparser.ConfigParser()
config.read(ini_file_path)

# lista testów do uruchomienia
tests_to_run = []

if "Tests" in config:
    for test_name, status in config["Tests"].items():
        if status.strip().upper() == "T":
            test_path = os.path.join(tests_dir, test_name)
            if os.path.isfile(test_path):
                tests_to_run.append(test_path)
            else:
                print(f"⚠️ Plik testowy nie istnieje: {test_path}")
else:
    print("❌ Sekcja [Tests] nie została znaleziona w pliku .ini.")
    sys.exit(1)

if not tests_to_run:
    print("⚠️ Brak testów do uruchomienia.")
    sys.exit(0)

# wspólny raport dla wszystkich testów
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = os.path.join(reports_dir, f"report_ALL_{timestamp}.html")

# komenda pytest
cmd = [
    "pytest",
    *tests_to_run,
    f"--html={report_file}",
    "--self-contained-html",
    "-q",
    "-s"
]

print(f"Uruchamiam testy: {', '.join(os.path.basename(t) for t in tests_to_run)}")

try:
    subprocess.run(cmd, check=True, stdin=sys.stdin)
except subprocess.CalledProcessError:
    print(f"\n❌ Testy zakończyły się błędem!")
    sys.exit(1)

print(f"\n✅ Wszystkie testy zakończone pomyślnie. Raport: {report_file}")