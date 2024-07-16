# Inlined from /metadata-ingestion/examples/library/dataset_schema.py
# Imports for urn construction utility methods
from datahub.emitter.mce_builder import make_data_platform_urn, make_dataset_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
import sys
import logging
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph


API = sys.argv[1]

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

graph = DataHubGraph(
    config=DatahubClientConfig(
        server="http://localhost:8080",
    )
)

dataset_urn = make_dataset_urn(name=API, platform="go-API")

# Soft-delete the dataset.
graph.delete_entity(urn=dataset_urn, hard=True)

log.info(f"Deleted dataset {dataset_urn}")

# Imports for metadata model classes
from datahub.metadata.schema_classes import (
    AuditStampClass,
    DateTypeClass,
    OtherSchemaClass,
    SchemaFieldClass,
    SchemaFieldDataTypeClass,
    SchemaMetadataClass,
    StringTypeClass,
)

event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
    entityUrn=make_dataset_urn(platform="go-API", name=API, env="PROD"),
    aspect=SchemaMetadataClass(
        schemaName="customer",  # not used
        platform=make_data_platform_urn("go-API"),  # important <- platform must be an urn
        version=0,  # when the source system has a notion of versioning of schemas, insert this in, otherwise leave as 0
        hash="",  # when the source system has a notion of unique schemas identified via hash, include a hash, else leave it as empty string
        platformSchema=OtherSchemaClass(rawSchema=""),
        lastModified=AuditStampClass(
            time=1640692800000, actor="urn:li:corpuser:ingestion"
        ),
        fields=[
            SchemaFieldClass(
                fieldPath="ID",
                type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                nativeDataType="SERIAL PRIMARY KEY",  # use this to provide the type of the field in the source system's vernacular
                description="",
                lastModified=AuditStampClass(
                    time=1640692800000, actor="urn:li:corpuser:ingestion"
                ),
            ),
            SchemaFieldClass(
                fieldPath="Name",
                type=SchemaFieldDataTypeClass(type=StringTypeClass()),
                nativeDataType="VARCHAR(100)",
                description="",
                lastModified=AuditStampClass(
                    time=1640692800000, actor="urn:li:corpuser:ingestion"
                ),
            ),
            SchemaFieldClass(
                fieldPath="Age",
                type=SchemaFieldDataTypeClass(type=DateTypeClass()),
                nativeDataType="INT",
                description="",
                lastModified=AuditStampClass(
                    time=1640692800000, actor="urn:li:corpuser:ingestion"
                ),
            ),
        ],
    ),
)

# Create rest emitter
rest_emitter = DatahubRestEmitter(gms_server="http://localhost:8080")
rest_emitter.emit(event)