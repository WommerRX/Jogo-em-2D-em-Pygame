import cx_Freeze

executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/MarioIco.ico")]

cx_Freeze.setup(
    name="Mario x Bowser",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables = executables
)





