---
# title: Tile Command
description: Tile Command
tags:
  - 3DTiles
  - citydb-3dtiler
  - Styling
---

# tile Command

With the `tile` command, features in the database are converted to the 3DTiles format. The generated tilesets are saved under the shared folder in the directory where the program is executed. If the `--separate-tilesets` option is used, a separate folder is created within the `shared` folder for each tileset according to the separation argument (namespace or objectlass name), and the 3DTiles files are saved into these folders.

## help (-h)

If you use the help option after the `tile` command, you will see the usage syntax of that command which is like below.

```bash
tile [-h] [--style-mode {existing-appearances,property-based,objectclass-based,no-style}] [--style-absence-behavior {fall-down,rise-up}] [-o [Output Folder]] [--transparency {blend,mask,opaque}] [--custom-style [Name of the custom style file]] [-a {none,selected,all}] [--selected-attributes [Comma separated list of the selected attributes]] [--attribute-structure {flat,nested}] [--tiles-version {1.0,1.1}] [--vertical-offset [VERTICAL_OFFSET]]
```

## style-mode

Style mode is used to assign material styles to features. Customizing PBR materials using the given CSV file is not the only option. There are four different style modes, and there is a mechanism (called absence-behaviour) that switches to another mode in case a style mode cannot be applied to a feature. The four style modes are like below:

- `existing-appearances` :
    - When this option is selected, tiling application will derive the defined appearences in the database (not the textures yet, but only the materials).
- `property-based` :
    - If you decided to assign colors to the features by considering some attributes, you can fill the relevant columns in `materials_for_features.csv` file and then select this option. See the [styling](./styling.md) page for more detail.
- `objectlass-based` : 
    - This mode is the default value for this option and it simply assigns the defined materials for every individual objectlass by considering the relevant columns in `materials_for_features.csv` file.
- `no-style` : 
    - In this option, there will be no different material for the features. Every feature will be rendered within the color sepcified in the `materials_for_features.csv` file in the column `pbr_metallic_roughness_base_color` for the pseudo-object called `anything-else`.

- Example : `--style-mode existing-appearances`

## style-absence-behaviour

This option can be switched when a special absence behaviour is requested. The default behaviour is `fall-down`. This means that, for example, if the user selected the `property-based` style mode but the application could not find any value for the specified property, it will try to assign material according to the style mode at the next lower level; in this case, that mode will be `objectclass-based`. Only one of the following arguments expected : 

- `fall-down`
- `rise-up`

??? tip "What is the order of the style modes?"
    The vertical order of the style modes is exactly the same as their order in the help documents. The first mode is at the top, and the last mode is at the bottom. Therefore, the vertical order should be accepted from top to bottom as follows: existing-appearances, property-based, objectclass-based, no-style.

## transparency

This is the option that determines the transparency of materials. Default value is `opaque`. Only one of the following arguments expected : 

- `blend` : 
    - When set to this, the last two digits of the color codes in the CSV file (the RGBA code) will determine the amount of transparency.
- `mask` :
    - When the masking option is selected, object textures are not rendered when they fall below a certain alpha value (this option has not been tested yet).
- `opaque` :
    - When set to opaque, any transparency value assigned to materials in the CSV file will be ignored even if present.

- Example : `--transparency-mode blend`

## custom-style

If you want to provide a custom style file (any CSV file not named `materials_for_features`), you can specify the file name (inc. file extension : `.csv`) using this argument.

- Example : `--custom-style materials_for_traffic_areas.csv`