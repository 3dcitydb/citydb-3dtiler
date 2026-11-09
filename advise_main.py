#External libraries
import os, sys

# Internal Libraries
from io_tools.pg_sql import read_sql_file
from io_tools.yaml import write_yaml
from database.pg_connection import pg_establish, get_query_results
from classes.advisement import Advice, ObjectClass, ObjectClassRecommendations, Namespace
from default_paths import get_base_path, get_shared_folder_path
from instances.in_advise import *

def advise(args):
    # Establish the Connection with PostgreSQL
    conn = pg_establish(args)

    # Take the existing objectclasses in the database instance
    # If --ignore-thematic-surfaces is selected ignore them
    if args.ignore_thematic_surfaces == True:
        existing_features, existing_features_file_name = read_sql_file("standalone_queries", "get_all_available_namespaces_wo_thematics.sql")
    else:
        existing_features, existing_features_file_name = read_sql_file("standalone_queries", "get_all_available_namespaces.sql")


    result = get_query_results(args, existing_features, name=existing_features_file_name)
    # print(result)

    # If the CRS is not specified when using BBox, 
    # following query will expose the used CRS on database.
    crs_code, crs_sql = read_sql_file("standalone_queries", "get_crs_code.sql")
    result_crs = get_query_results(args, crs_code, name=crs_sql)
    
    # Take the used command arguments and save as list 
    commandset = dict(args._get_kwargs())
    # Added for security purpose
    commandset['db_password'] = '****'
 
    # Following part is canceled because the given advice comprise every scenario 
    # (for exp. namespace, objectclass based separations)

    # if args.separate_tilesets is not None:
    #     if args.separate_tilesets == "objectclass":
    #         ocs = []
    #         for oc in result_oc[0]:
    #             # Set a Where condition for each calculator query that filters objectclasses
    #             cndtn = f"oc.classname = '{oc}'"
    #             whrs = WhereElements(
    #                 WhereElement(condition = cndtn))
    #             geometry_statistics.where_elements = whrs

    #             # Calculates Maximum Features per Tile for the specificied Objectclass
    #             qry_name = "recommended_max_features_per_tile for : " + f"{oc}" + " (instance)"
    #             oc_statistics = get_query_results(args, str(recommended_max_features_per_tile), name=qry_name)
    #             rmf = oc_statistics[3] # Statistics Order: 0:min, 1:max, 2:avg, 3:mxm_ftr_pr_tl
                
    #             # Remove the null/none values
    #             properties_list = [prop for prop in result_oc[0][oc]["properties"] if prop is not None]
                
    #             # Add to the list of the ObjectClasses
    #             oc_new = dict(ObjectClass(oc, objectclass_recommendations = int(rmf), properties = properties_list))
    #             ocs.append(oc_new)

            
    #         # Set the Advice class by considering every objectclasses separately
    #         adv = Advice(commandset, max_features=None, crs_code=result_crs[0], objectclasses=ocs)

    #         try:
    #             write_yaml(get_shared_folder_path(), args.output_file, dict(adv))
    #         except OSError as err:
    #             print(f"File Writing Error:\n{err}")
        
    #     #if args.separate_tilesets == "namespace":
            

    # else:

    # ENDOF Cancelled part

    # Calculate the Overall Value for the Maximum Features per Tile (mft)
    if args.ignore_thematic_surfaces == True:
        general_statistics = get_query_results(args, str(recommended_max_features_per_tile_wo_thematics), name="recommended_max_features_per_tile_wo_thematics (instance)")
    else:
        # Calculate the recommended max features per tile by considering all the features
        general_statistics = get_query_results(args, str(recommended_max_features_per_tile), name="recommended_max_features_per_tile (instance)")
    recommended_mft = general_statistics[3]

    # Add the existing namespaces and objectclasses to the Advice document

    # namespace_list = [v for v in result[0].keys()]
    # objectclass_list = [k for v in result[0].values() for k in v.keys()]

    # print(recommended_max_features_per_tile)

    namespace_dicts  = []
    for ns in result[0] :
        #Calculate the individual values of the recommended MFT for Namespaces:
        # Set a Where condition for each calculator query that filters namespaces
        cndtn = f"ns.alias = '{ns}'"
        whrs = WhereElements( WhereElement(condition = cndtn) )
        geometry_statistics.where_elements = whrs
        qry_name = "recommended_max_features_per_tile for : " + f"{ns}" + " (instance)"
        ns_statistics = get_query_results(args, str(recommended_max_features_per_tile), name=qry_name)
        recommended_mft_4_namespace = ns_statistics[3] # Statistics Order: 0:min, 1:max, 2:avg, 3:mxm_ftr_pr_tl
        # print("Here it is : ", recommended_mft_4_namespace)
        
        # Build the Dictionary for every namespace
        objectclass_dicts = []
        for oc in result[0][ns]:
            #Calculate the individual values of the recommended MFT for Objectclasses:
            # Set a Where condition for each calculator query that filters objectclasses
            cndtn = f"oc.classname = '{oc}'"
            whrs = WhereElements( WhereElement(condition = cndtn) )
            geometry_statistics.where_elements = whrs
            qry_name = "recommended_max_features_per_tile for : " + f"{oc}" + " (instance)"
            oc_statistics = get_query_results(args, str(recommended_max_features_per_tile), name=qry_name)
            recommended_mft_4_objectclass = oc_statistics[3] # Statistics Order: 0:min, 1:max, 2:avg, 3:mxm_ftr_pr_tl
            
            # Build the dictionary for the objectlass
            oc_new = dict(ObjectClass(oc, recommended_mft = int(recommended_mft_4_objectclass), properties = result[0][ns][oc]["properties"]))
            objectclass_dicts.append(oc_new)

        ns_new = dict(Namespace(ns, recommended_mft= int(recommended_mft_4_namespace), objectclasses = objectclass_dicts))
        namespace_dicts.append(ns_new)
    # print(namespace_dicts)
    
    
    # Set the Advice class
    adv = Advice(commandset, recommended_mft=int(recommended_mft), crs_code=result_crs[0], namespaces = namespace_dicts)
    # Write the Advice as a YAML file
    try:
        write_yaml(get_shared_folder_path(), args.output_file, dict(adv))
    except OSError as err:
        print(f"File Writing Error:\n{err}")
