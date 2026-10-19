---
# title: Sample Commands & Tests
description: Sample Commands & Tests
tags:
  - Samples
  - citydb-3dtiler
  - Tests
---

# Samples

## Difference between the Docker and Python Env. Usage

There are two main ways to use the citydb-3dtiler application: The first and relatively easier one is to run it inside a container using the Docker image. It does not require any installation other than Docker, but the parameters specified in the documentation must be used. The second way is to set up a Python virtual environment and run the application within that environment. It requires installation, but the commands are shorter. For this reason, we will list the Python commands in the example commands below. If you want to run the example commands below using a Docker container, all you need to do is simply replace the `python3 citydb-3dtiler.py` expression in the commands with the `docker run ...` expression.

Here below there are examples for such a replacement:

=== "Take report within Python setup"
    ```bash
    python3 citydb-3dtiler.py \
    --db-host localhost --db-port 9876 \
    --db-name citydb-visualizer \
    --db-schema citydb \
    --db-username tester --db-password louvre \
    advise
    ```

=== "Take report using Docker"
    ```bash
    docker run \
    --rm --interactive --tty \
    --name citydb-3dtiler \
    --volume ./:/home/tester/citydb-3dtiler/shared:rw \
    citydb-3dtiler:latest \
    --db-host localhost --db-port 9876 \
    --db-name citydb-visualizer --db-schema citydb \
    --db-username tester --db-password louvre \
    advise
    ```

??? tip "What is the purpose of the backslash (\\) character in the code block?"
    - When typing commands, the caret (^), backtick (\`), and backslash (\\) are "escape characters" that tell the computer to handle the next symbol as plain text, not as a command.
    - Windows CMD uses ^, PowerShell uses \`, and Linux Bash uses \\ because each system speaks a slightly different language. 
    - Alternatively, you can copy these commands into a text editor and delete both the escape characters and the new line characters (\\n) to turn the command into a single line.

## Help (-h) commands

You can use the help command for both main commands and subcommands.

=== "General help document"
    ```bash
    python3 citydb-3dtiler.py --help
    ```

=== "Help doc for advise command"
    ```bash
    python3 citydb-3dtiler.py advise --help
    ```

=== "Help doc for tile command"
    ```bash
    python3 citydb-3dtiler.py tile --help
    ```

## Advise command samples

### Take an advice for the existing dataset to generate a single tileset

```bash
python3 citydb-3dtiler.py \
--db-host localhost --db-port 9876 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password louvre \
advise
```

### Take an advice for the existing dataset to generate separate tilesets


```bash
python3 citydb-3dtiler.py \
--db-host localhost --db-port 9876 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password louvre \
--separate-tilesets objectclass \
advise
```

## Tile command samples

### Generate 3DTiles using property-based styling

#### (Customization Step) How to assign custom property values to set the materials/colors?

To set such a color/material set, you have to check the existing properties in your dataset. To see the available properties, you can also check the advice document created by the advise command. However, you still need to find the value sets for the existing dataset. After that you can add the property names and the values to the materials document like below:

 namespace of classname | classname | namespace of property | property name | column name of property value | property value | pbr metallic roughness base color 
---|---|---|---|---|---|---
 bldg | Building |  |  |  |  | #00E5EE80 
 bldg | Building | bldg | roofType | val_string | flat | #66DEF3FC 
 bldg | Building | bldg | roofType | val_string | gabled | #F35FCBFC 

??? info "Style-Modes"
    Default style-mode is objectclass-based. Check the materials_for_features.csv table to view existing objectclasses.

```bash
    python3 citydb-3dtiler.py \
    --db-host localhost --db-port 9876 \
    --db-name citydb-visualizer \
    --db-schema citydb \
    --db-username tester --db-password louvre \
    tile \
    --style-mode property-based
```

### Generating separated 3DTiles using objectclass-based separation and property-based styling

```bash
    python3 citydb-3dtiler.py \
    --db-host localhost --db-port 9876 \
    --db-name citydb-visualizer \
    --db-schema citydb \
    --db-username tester --db-password louvre \
    --separate-tilesets objectclass \
    tile \
    --style-mode property-based
```