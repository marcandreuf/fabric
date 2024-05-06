import os
import typer
from .utils import Standalone


home_holder = os.path.expanduser("~")
config = os.path.join(home_holder, ".config", "fabric")
config_patterns_directory = os.path.join(config, "patterns")
config_context = os.path.join(config, "context.md")
env_file = os.path.join(config, ".env")
app = typer.Typer()

@app.command("listmodels")
def listmodels():
    standalone = Standalone(None, None)
    gptmodels, _, _ = standalone.fetch_available_models()
    print("GPT Models:")
    for model in gptmodels:
            print(model)
    
    
@app.command("list")
def list():
    try:
        direct = sorted(os.listdir(config_patterns_directory))
        for d in direct:
            print(d)
    except FileNotFoundError:
        print("No patterns found")

def main() -> None:
    app()