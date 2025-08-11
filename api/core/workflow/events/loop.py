from collections.abc import Mapping
from datetime import datetime
from typing import Any, Optional

from pydantic import Field

from core.workflow.events.base import GraphNodeEventBase, NodeEventBase


class NodeRunLoopStartedEvent(GraphNodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    predecessor_node_id: Optional[str] = None


class NodeRunLoopNextEvent(GraphNodeEventBase):
    index: int = Field(..., description="index")
    pre_loop_output: Optional[Any] = None
    duration: Optional[float] = None


class NodeRunLoopSucceededEvent(GraphNodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    outputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    steps: int = 0
    loop_duration_map: Optional[dict[str, float]] = None


class NodeRunLoopFailedEvent(GraphNodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    outputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    steps: int = 0
    error: str = Field(..., description="failed reason")


class LoopStartedEvent(NodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    predecessor_node_id: Optional[str] = None


class LoopNextEvent(NodeEventBase):
    index: int = Field(..., description="index")
    pre_loop_output: Optional[Any] = None
    duration: Optional[float] = None


class LoopSucceededEvent(NodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    outputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    steps: int = 0
    loop_duration_map: Optional[dict[str, float]] = None


class LoopFailedEvent(NodeEventBase):
    start_at: datetime = Field(..., description="start at")
    inputs: Optional[Mapping[str, Any]] = None
    outputs: Optional[Mapping[str, Any]] = None
    metadata: Optional[Mapping[str, Any]] = None
    steps: int = 0
    error: str = Field(..., description="failed reason")
