# Test Procedures

## Test Procedures Diagram

This diagram shows the list of test procedures to be carried out in order to perform an internal quality check or to prevent function loss during developments.

```puml
@startmindmap
title Test Procedure of citydb-3dtiler application
header
<font color=indianred size=12><b>Last Check : 03.11.2026</b></font>
<font color=indianred size=12><b>Expected Release : 0.9.5</b></font>
<font color=indianred size=12><b>Checks made on Tokio-CityGML3 (UDX)</b></font>
endheader

'!include card-style.puml

* Tests

** help <&check>

** advise
*** advise (T001) <&check>
*** --ignore-thematic-surfaces advise (T002) <&check>



** (filter options)

***: filter by id and type-name (T005) <&check>

***: filter by limit and start-index together (T006) <&check>

***: filter by bbox filtering with CRS code (T007) <&check>

***: filter by bbox filtering with contains-precise mode <&check>

***: filter by CQL2 Expressions (--filter) <&check>
"--filter bldg_storeysaboveground > 5 AND con_height__con_value > 12"
"--attributes selected "
"--selected-attributes gen_grundhoehenn,gen_grundflaeche2d"
;
***: use sql-filter <&check>
"gen_citygrid_unitid.pro_value like '2021%'"
"AND st_dwithin(st_geomfromtext('POINT(566924 5934737)',25832), gmdt.geometry, 2000)"
"--attributes selected \"
"--selected-attributes gen_citygrid_unitid"
;

** tile

***: tile (T003) <&check>

****: Custom Color Set 
<font color=gray><i>tile --custom-style tum_colors.csv</i></font>
;
****: Property-based Color Set
<font color=gray><i>tile --style-mode property-based</i></font>
;
****: Transparency Mode
<font color=gray><i>tile --transparency blend</i></font>
;
****: To a Custom Folder
<font color=gray><i>tile --output-folder</i></font>
;
****: No Style Mode
<font color=gray><i>tile --style-mode no-style</i></font>
;
***: For Separate Tilesets (objectclass)
<font color=gray><i>--separate-tilesets objectclass \ </i></font>
<font color=gray><i>tile</i></font>
;
****: Property-based Color Set
<font color=gray><i>--separate-tilesets objectclass \ </i></font>
<font color=gray><i>tile \ </i></font>
<font color=gray><i>--style-mode property-based</i></font>
;
*****: Selected Attributes in tabular format
<font color=gray><i>--separate-tilesets objectclass \ </i></font>
<font color=gray><i>tile \ </i></font>
<font color=gray><i> --style-mode property-based \ </i></font>
<font color=gray><i>--attributes selected \ </i></font>
<font color=gray><i>--selected-attributes  core_name,gen_objektart</i></font>
;
*****: Selected Attributes in nested/json format
<font color=gray><i>--separate-tilesets objectclass \ </i></font>
<font color=gray><i>tile \ </i></font>
<font color=gray><i>--style-mode property-based \ </i></font>
<font color=gray><i>--attributes selected \ </i></font>
<font color=gray><i>--attribute-structure nested \ </i></font>
<font color=gray><i>--selected-attributes core_name,gen_objektart,con_height</i></font>
;
*****: All Attributes in nested/json format
<font color=gray><i> --separate-tilesets objectclass \ </i></font>
<font color=gray><i>tile \ </i></font>
<font color=gray><i>--style-mode property-based \ </i></font>
<font color=gray><i>--attributes all \ </i></font>
<font color=gray><i>--attribute-structure nested</i></font>
;
*****: Separate Tilesets & Property-based Color Set & All Attributes in nested/json format
<font color=gray><i>--separate-tilesets objectclass tile \ </i></font>
<font color=gray><i>tile \ </i></font>
<font color=gray><i>--style-mode property-based \ </i></font>
<font color=gray><i>--attributes selected \ </i></font>
<font color=gray><i>--attribute-structure nested \ </i></font>
<font color=gray><i>--tiles-version 1.0 \ </i></font>
<font color=gray><i>--vertical-offset 3.5</i></font>
;

***: --ignore-thematic-surfaces tile (T004) <&check>

legend left
Recommended Datasets:
  Samplycity : https://muratkendir.github.io/samplycity/
  Tokio CityGML3 UDX : https://www.geospatial.jp/ckan/dataset/plateau-tokyo-takeshiba-cg3-sample
  Hamburg LoD3 (CG2) : https://suche.transparenz.hamburg.de/dataset/3d-gebaeudemodell-lod3-0-hh-hamburg17
  Switzerland (CG2) : https://www.swisstopo.admin.ch/de/landschaftmodell-swissbuildings3d-3-0-beta#swissBUILDINGS3D-3.0-Beta---Download
endlegend

@endmindmap
```

## Previous Tests

The following list contains the links of the previous tests carried out by following the test procedures.
Test procedures are usually handled before publishing a new release.

- Before release 0.9.3
    - [Tests done with Swisstopo dataset](https://www.3dcitydb.net/3dcitydb/fileadmin/public/kendir/#bern_full_procedure){:target="_blank"}
- Before release 0.9.2
    - [Tests done for SamplyCity Dataset](https://www.3dcitydb.net/3dcitydb/fileadmin/public/kendir/#test_campaign_03_samplycity){:target="_blank"}
- Test with Hamburg LoD3 dataset
    - [Hamburg Buildings LoD3](https://www.3dcitydb.net/3dcitydb/fileadmin/public/kendir/#test_campaign_02_hamburg){:target="_blank"}
- Test with Melbourne dataset
    - [Melbourne Buildings & Roads](https://www.3dcitydb.net/3dcitydb/fileadmin/public/kendir/#tests_for_3dtiler_melbourne){:target="_blank"}

