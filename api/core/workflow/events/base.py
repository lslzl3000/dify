from typing import Optional

from pydantic import BaseModel, Field

from core.workflow.enums import NodeType
from core.workflow.node_events import NodeRunResult


class GraphEngineEvent(BaseModel):
    pass


class BaseGraphEvent(GraphEngineEvent):
    pass


class GraphNodeEventBase(GraphEngineEvent):
    id: str = Field(..., description="node execution id")
    node_id: str
    node_type: NodeType

    in_iteration_id: Optional[str] = None
    """iteration id if node is in iteration"""
    in_loop_id: Optional[str] = None
    """loop id if node is in loop"""

    # The version of the node, or "1" if not specified.
    node_version: str = "1"
    node_run_result: NodeRunResult = Field(default_factory=NodeRunResult)


class BaseIterationEvent(GraphNodeEventBase):
    node_title: str
    parallel_mode_run_id: Optional[str] = None
    """iteratoin run in parallel mode run id"""

    @property
    def iteration_id(self) -> str:
        """Alias for id to maintain backward compatibility"""
        return self.id

    @property
    def iteration_node_id(self) -> str:
        """Alias for node_id to maintain backward compatibility"""
        return self.node_id

    @property
    def iteration_node_type(self) -> NodeType:
        """Alias for node_type to maintain backward compatibility"""
        return self.node_type


class GraphAgentNodeEventBase(GraphNodeEventBase):
    pass
