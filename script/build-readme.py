from jinja2 import Environment, FileSystemLoader
import pathlib
current = pathlib.Path(__file__).parent.resolve()
root = current.parent.resolve()

if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader(current / "templates"))    
    template = env.get_template('README.md')

    readme = root / "README.md"
    readme.open("w").write(template.render())