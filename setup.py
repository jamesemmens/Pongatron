import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
  name="Pongatron",
  options={"build.exe": {"packages":["pygame"],
                          "include_files":["images/car.png"]}},
                          executables = executables


)
