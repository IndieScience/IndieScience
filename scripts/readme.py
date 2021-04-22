import pathlib
root = pathlib.Path(__file__).parent.parent.resolve()

print(root)
if __name__ == "__main__":
    readme = root / "README.md"
    readme.open("w").write("hello world")
