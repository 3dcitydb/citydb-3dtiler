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

=== "within the Docker Container"

    ```bash
    docker run [DOCKER OPTIONS] SUBCOMMAND [OPTIONS] ARGUMENTS
    ```

=== "in the Python Env."

    ```bash
    python3 citydb-3dtiler.py SUBCOMMAND [OPTIONS] ARGUMENTS
    ```

## Options of the main command (citydb-3diler)

| **Option** | **Description** | **Default value** |
|---|---|---|
| [-h, --help](#usage-syntax) | shows a help message and exit the program |  |
| [--tiler-app](#tiler-app) | choose one of the compatible 3D Tile Generator app | pg2b3dm |
| [--tilers-path](#tilers-path) | sets the absolute/relative path of the selected 3D Tile Generator software. | tiler_app/ |
| [--separate-tilesets](#separate-tilesets) | exports separate tilesets for each objectclass or namespace |  |
| [(Database Connection Options)](./db_con_options.md) | This group is expressed as a placeholder to collectively represent the options used for configuring database connections. |  |
| [(Filter Options)](./filters.md) | This group is expressed as a placeholder to collectively represent the options used for filtering the existing features. |  |

??? tip "Check all the subcommands and the options in one diagram"
    If you want to see all the subcommands and the options with possible arguments in one diagram, visit this page : [citydb-3dtiler Functionality Matrix](functionality_matrix.md)

### tiler-app (main option)

If the file name of the tiler application is different, you can use this option. 

- Default value is "pg2b3dm".

??? info "What is planned for this option?"
    We plan to enable the use of the i3dmExport and/or py3dtiles applications with this option in future developments. However, currently only the pg2b3dm application has been tested and is ready for use.

### tilers-path

If you want to use a specific version of pg2b3dm that you have determined, you must put this specific version into another folder and then specify the folder path using this option. This way, you can make the application work with any version you want.

- Default value is "tiler_app".

??? Warning "Some (tile) options might not work in this scenario"
    Since the options of the pg2b3dm application may vary depending on the version, you may not be able to use every argument.

### separate-tilesets

This option is used to specify the criteria for creating multiple tilesets. You can create separate tilesets by considering the objectclasses (Building, Wall, Window etc.) or namespaces (bldg, tun, brid etc.) of the features.

- Default value is "objectclass"

[Sample 3D Scene](https://tinyurl.com/leipzig3d){:target="_blank"}

## Commands

| **Command** | **Description** |
|---|---|
| [help](#usage-syntax) | The help output shows the usage syntax and available arguments. |
| [advise](./advise.md) | Test connection to the database. |
| [tile](./tile.md) | Show database contents and summary information. |

## Usage Syntax

The usage syntax of the main options and the subcommands `advice` and `tile` are as follows. To see this usage syntax on the command line interface (CLI), you can type `-h` or `--help` immediately after the main command (`citydb-3dtiler`) or the docker (run) command. If you want to see the options of the subcommands `advice` and `tile`, click on the relevant links in the [Commands table](#commands).

```bash
citydb-3dtiler [-h] [--tilers-path [File Path of the 3D Tiler]] \
    [--tiler-app {pg2b3dm,py3dtiles}] \
    [--separate-tilesets [{objectclass,namespace}]] \
    [-H Hostname] [-P Port Number] [-d Database Name] \
    [-S Schema] [-u Username] [-p Password] \
    [--limit Limit] [--start-index Start Index] [-i ID Number(s)] \
    [-t Type Name(s) / Objectclasses] \
    [-b Boundary Box] [--bbox-mode Boundary Box Mode] \
    [-f CQL2 Filter] [--sql-filter SQL Filter] \
    {advise,tile} ...
```


Some sample commands given in the code blocks below.

=== "within the Docker container"

    ```bash
    docker run --rm --interactive --tty --name tiler \
        --volume ./:/home/tester/citydb-3dtiler/shared:rw \
        citydb-3dtiler:latest \
        --db-host localhost --db-port 9876 \
        --db-name luebbecke_3d \
        --db-schema citydb \
        --db-username tester --db-password louvre \
        tile \
        --vertical-offset 0.5
    ```

=== "in the Python Env."

    ```bash
    python3 citydb-3dtiler.py \
        --db-host localhost --db-port 9876 \
        --db-name luebbecke_3d \
        --db-schema citydb \
        --db-username tester --db-password louvre \
        tile \
        --vertical-offset 0.5
    ```

??? tip "What is the purpose of the backslash (\\) character in the code block?"
    - When typing commands, the caret (^), backtick (\`), and backslash (\\) are "escape characters" that tell the computer to handle the next symbol as plain text, not as a command.
    - Windows CMD uses ^, PowerShell uses \`, and Linux Bash uses \\ because each system speaks a slightly different language. 
    - Alternatively, you can copy these commands into a text editor and delete both the escape characters and the new line characters (\\n) to turn the command into a single line.