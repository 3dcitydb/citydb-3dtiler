# Advise

## T001
python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
advise

## T002
python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--ignore-thematic-surfaces \
advise

# Tiling

## T003
python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
tile

## T004

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--ignore-thematic-surfaces \
tile

## T005

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--id bldg_97287e3a-7844-4b71-b95f-840f8bdf224e,bldg_3fad10e5-8d5c-46b0-83c1-7d23afc798de,bldg_02fcca4c-df92-40b0-9895-9046578e3f1c,bldg_bc1eb1f9-0246-4335-9736-c7888b0f8c85 \
--type-name Building \
tile

## T006

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--limit 1000 --start-index 3000 \
tile

## T007

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--bbox 139.7496291,35.6608369,139.7568912,35.6651614,6697 \
tile

## T008

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--bbox 139.7496291,35.6608369,139.7568912,35.6651614,6697 \
--bbox-mode contains-precise \
tile

## T009

python3 citydb-3dtiler.py \
--db-host 172.17.0.2 --db-port 5432 \
--db-name citydb-visualizer \
--db-schema citydb \
--db-username tester --db-password 123456 \
--filter "bldg_storeysaboveground > 5 AND con_height__con_value > 12" \
tile \ 
--attributes selected \
--selected-attributes bldg_storeysaboveground,con_height__con_value
