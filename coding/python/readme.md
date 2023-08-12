# Program templete

1. Main entrance
    - parse argument
    - process config
    - setup device (cuda, mpi)
    - setup checkpoint
    - setup logger
    - choose sub-process

# src
1. Static parameters
    - configs (.py .yaml .json)
    - scripts (.sh)

2. Environment
    - init
    - wrapper
    - data loader

3. Utils
    - file utils
    - array utils
    - math utils

4. Component
    - checkpoint
    - logger



