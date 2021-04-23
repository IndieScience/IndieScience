from jinja2 import Environment, FileSystemLoader
import pathlib
root = pathlib.Path(__file__).parent.parent.resolve()

print(root)
if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader('templates'))    
    template = env.get_template('README.md')
    text = template.render()

    readme = root / "README.md"
    readme.open("w").write(text)
