import sys
import datahub.emitter.mce_builder as builder
from datahub.emitter.rest_emitter import DatahubRestEmitter

#удалит все соединения идущиее к # Downstream потом создает соединение от # Upstream к # Downstream

API = sys.argv[1]
flag = sys.argv[2]
arguments = sys.argv[3:]

if flag =="up":
   list = []
   for arg in arguments:
      list.append(builder.make_dataset_urn("postgres", "mydatabase.public." + arg))
   # Construct a lineage object.
   lineage_mce = builder.make_lineage_mce(
      list,  # Upstream
      builder.make_dataset_urn("go-API", API),  # Downstream
   )
      # Create an emitter to the GMS REST API.
   emitter = DatahubRestEmitter("http://localhost:8080")

   # Emit metadata!
   emitter.emit_mce(lineage_mce)

if flag =="down":
   # Construct a lineage object.
   lineage_mce = builder.make_lineage_mce(
      [
         builder.make_dataset_urn("go-API", API ),  # Upstream
      ],
      builder.make_dataset_urn("postgres", "mydatabase.public." + arguments[0]),  # Downstream
   )

   # Create an emitter to the GMS REST API.
   emitter = DatahubRestEmitter("http://localhost:8080")

   # Emit metadata!
   emitter.emit_mce(lineage_mce)
