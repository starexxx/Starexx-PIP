import os
import subprocess

def scan_and_install():
    print("Scanning all Python scripts for dependencies...")

    modules = set()
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("import ") or line.startswith("from "):
                            module = line.split()[1].split(".")[0]
                            modules.add(module)

    if not modules:
        print("No missing modules found.")
        return

    print("Installing required modules:", ", ".join(modules))
    subprocess.run(["pip", "install"] + list(modules))

if __name__ == "__main__":
    scan_and_install()
