#External Libraries
import sys

# Internal Libraries
from classes.sql_blocks import *
from database.pg_connection import get_query_results

# Geometry Statistics (Min, Max, Average, Total number of points per feature geometry):

gmt_stt_selects = SelectElements(
        SelectElement(
            select_type="field",
            field="MIN(st_npoints(gd.geometry))",
            range_alias="min_vertices"),
        SelectElement(
            select_type="field",
            field="MAX(st_npoints(gd.geometry))",
            range_alias="max_vertices"), 
        SelectElement(
            select_type="field",
            field="ROUND(AVG(st_npoints(gd.geometry)),2)",
            range_alias="avg_vertices"), 
        SelectElement(
            select_type="field",
            field="count(gd.id)",
            range_alias="geometries_total")
        )
gmt_stt_froms = FromElements(
        FromElement(
            table="geometry_data",
            alias="gd"
        )
    )

# Objectclass based separation (Separates the statistics by considering objectclasses)
oc_spr_joins = JoinElements(
    JoinElement(
        join_type = "left",
        table = "feature",
        range_alias = "ftr",
        condition = "ftr.id = gd.feature_id"
        ), 
    JoinElement(
        join_type = "left",
        table = "objectclass",
        range_alias = "oc",
        condition = "ftr.objectclass_id = oc.id"
        ),
    JoinElement(
        join_type = "left",
        table = "namespace",
        range_alias = "ns",
        condition = "ns.id = oc.namespace_id"
        )
    )

geometry_statistics = QueryBlock(
    name = "Statistics of Geometries",
    range_alias = "stt",
    type_of_effect = "Spatial",
    order_number = 1,
    select_elements = gmt_stt_selects,
    from_elements = gmt_stt_froms,
    join_elements = oc_spr_joins
    )

# Adds an option to filter out the thematic surfaces

fltr_ot_thmtc_srfcs = WhereElements(
    WhereElement(
        condition="oc.id not in (612,715,15,718,713,203,710,615,711,300,614,716,714,712,613,709,1503,1502,719)",
        operator="AND"
        )
    )

geometry_statistics_wo_thmtcs = QueryBlock(
    name = "Statistics of Geometries",
    range_alias = "stt",
    type_of_effect = "Spatial",
    order_number = 1,
    select_elements = gmt_stt_selects,
    from_elements = gmt_stt_froms,
    join_elements = oc_spr_joins,
    where_elements = fltr_ot_thmtc_srfcs
    )

# Combination of "Statistics of Geometries" and "Addition of Objectclasses"

# geometry_statistics_w_objectclasses = QueryBlock(
#     name = "Statistics of Geometries by every Objectclasses",
#     type_of_effect = "Ontological",
#     order_number = 1,
#     inner_query_blocks = geometry_statistics)

# Recommended Maximum Features Per Tile (encapsulates Geometry Statistics)

rcm_mxm_ftr_pr_tl_selects = SelectElements(
        SelectElement(
            select_type="field",
            field="min_vertices"
            ), 
        SelectElement(
            select_type="field",
            field="max_vertices"
            ), 
        SelectElement(
            select_type="field",
            field="avg_vertices"
            ), 
        SelectElement(
            select_type="field",
            field = "ROUND(10000/avg_vertices)",
            range_alias = "max_features_per_tile"
        )
    )
rcm_mxm_ftr_pr_tl_selects_froms = FromElements(
    FromElement(
        inner_query_blocks = [geometry_statistics])
    )

# Adds an option to filter out the thematic surfaces

rcm_mxm_ftr_pr_tl_selects_froms_wo_thmtcs = FromElements(
    FromElement(
        inner_query_blocks = [geometry_statistics_wo_thmtcs])
    )

recommended_max_features_per_tile = QueryBlock(
    name = "Recommended Max Features Per Tile",
    type_of_effect = "Ontological",
    order_number = 1,
    select_elements = rcm_mxm_ftr_pr_tl_selects,
    from_elements = rcm_mxm_ftr_pr_tl_selects_froms
    )

# Adds an option to filter out the thematic surfaces

recommended_max_features_per_tile_wo_thematics = QueryBlock(
    name = "Recommended Max Features Per Tile",
    type_of_effect = "Ontological",
    order_number = 1,
    select_elements = rcm_mxm_ftr_pr_tl_selects,
    from_elements = rcm_mxm_ftr_pr_tl_selects_froms_wo_thmtcs,
    )
