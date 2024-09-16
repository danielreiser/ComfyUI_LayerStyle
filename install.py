import subprocess

whl_files = [
    "./whl/docopt-0.6.2-py2.py3-none-any.whl",
    "./whl/hydra_core-1.3.2-py3-none-any.whl"
]

for whl in whl_files:
    subprocess.run(["pip3", "install", whl], check=True)