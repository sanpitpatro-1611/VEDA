import os
import sys
import subprocess


def main():
    compiler = os.path.join(os.path.dirname(__file__), "compiler.py")

    command = [sys.executable, compiler]

    if len(sys.argv) > 1:
        command.extend(sys.argv[1:])

    subprocess.run(command)


if __name__ == "__main__":
    main()