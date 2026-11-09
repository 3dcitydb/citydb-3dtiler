# Structure of the Advice file in YAML Format

```puml
@startyaml

title Structure of the Advice File

'Last Check : 09.11.2026

#highlight "recommended_mft"
#highlight "namespaces" / "recommended_mft"
#highlight "namespaces" / "objectclasses" / "recommended_mft"

commandset:
    - bbox
    - bbox_mode
    - command
    - db_host
    - db_name
    - db_password
    - db_port
    - db_schema
    - db_username
    - filter
    - id
    - ignore_thematic_surfaces
    - limit
    - output_file
    - sql_filter
    - start_index
    - tiler_app
    - tilers_path
    - type_name
namespaces:
    - alias : "Shorten name of package"
    - objectclasses:
        - name
        - properties
        - recommended_mft
    - recommended_mft
recommended_mft : "Recommended Maximum Feature Number per Tile"
used_crs_code : "The EPSG code used in the 3DCityDB"

@endyaml
```