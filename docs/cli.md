---
# title: Docker
description: citydb-3dtiler CLI Overview
tags:
  - CLI
  - citydb-3dtiler
  - commands
---

# CLI Overview

citydb-3dtiler is the main command of the application. When run with the Docker container, this main command is automatically invoked, so there is no need to retype it. However, when running in a Python environment, the main command must be typed. Besides the main command, there are two subcommands: "advise" and "tile". The "--help" option provides explanatory information about the typed command and, depending on the command, other options that can be used.

## Synopsis

=== "with Docker Container"

    ```bash
    docker run [DOCKER OPTIONS] SUBCOMMAND [OPTIONS] ARGUMENTS
    ```

=== "in Python Env."

    ```bash
    python3 citydb-3dtiler.py SUBCOMMAND [OPTIONS] ARGUMENTS
    ```

## Options of the main command (citydb-3diler)

--8<-- "docs/includes/global_options.md"

If you want to see all the subcommands and the options with possible arguments in one diagram, visit this page : [citydb-3dtiler Functionality Matrix](functionality_matrix.md)
