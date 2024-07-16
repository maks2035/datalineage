import logging

from datahub.emitter.mce_builder import make_dataset_urn
from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

graph = DataHubGraph(
    config=DatahubClientConfig(
        server="http://localhost:8080",
    )
)

dataset_urn = make_dataset_urn(name="api", platform="go-API")

# Soft-delete the dataset.
graph.delete_entity(urn=dataset_urn, hard=True)

log.info(f"Deleted dataset {dataset_urn}")