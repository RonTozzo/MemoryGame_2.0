from cx_Freeze import setup, Executable

setup(
    name = "MemoryGame", 
    options = {
        "build_exe":
        {
            "packages":
            ["pygame"],
            "include_files":
            ["fonts", "pic", "sound"]
        }
    }, 
    executables = [Executable (script = "MemoryGame.py")]
)