from datetime import datetime
from pydantic import BaseModel, ConfigDict, NaiveDatetime
from typing import List, Optional

class EventBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    description: Optional[str] = None
    location: Optional[str] = None
    event_type: str
    event_status: int
    # event_owner: str
    event_timestamp: datetime
    # asset_id: int

class EventCreate(EventBase):
    pass

class Event(EventBase):    
    id: int
    # asset: models.Asset



# class AssetBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     location: Optional[str] = None
#     asset_type: str
#     asset_status: str
#     asset_owner: str

# class Asset(AssetBase):
#     id: int
#     events: List[models.Event] = []
#     downtimes: List[models.Downtime] = []

#     class Config:
#         orm_mode = True


# class DowntimeBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     location: Optional[str] = None
#     downtime_type: str
#     downtime_status: int
#     downtime_owner: str
#     downtime_timestamp: str
#     downtime_end_time: str
#     reason_level_1: int
#     reason_level_2: int
#     reason_level_3: int
#     reason_level_4: int
#     asset_id: int

# class DowntimeCreate(DowntimeBase):
#     pass

# class Downtime(DowntimeBase):
#     id: int
#     asset: models.Asset
#     event: models.Event
#     reason_level_1: models.ReasonTreeNode
#     reason_level_2: models.ReasonTreeNode
#     reason_level_3: models.ReasonTreeNode
#     reason_level_4: models.ReasonTreeNode
    
#     class Config:
#         orm_mode = True

# class UserBase(BaseModel):
#     name: str
#     email: str
#     is_active: Optional[bool] = True
#     is_superuser: Optional[bool] = False

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     assets: List[models.Asset] = []

#     class Config:
#         orm_mode = True

# class AssetStatus(BaseModel):
#     name: str
#     description: Optional[str] = None

#     class Config:
#         orm_mode = True

# class AssetStatusTransition(BaseModel):
#     from_status_type: int
#     to_status_type: int

#     class Config:
#         orm_mode = True

# class EventStatus(BaseModel):
#     name: str
#     description: Optional[str] = None

#     class Config:
#         orm_mode = True

# class DowntimeStatus(BaseModel):
#     name: str
#     description: Optional[str] = None

#     class Config:
#         orm_mode = True

    
# class ReasonTreeBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     parent_id: Optional[int] = None
    
# class ReasonTreeCreate(ReasonTreeBase):
#     pass

# class ReasonTree(ReasonTreeBase):
#     id: int
#     children: List[ReasonTreeBase] = []

#     class Config:
#         orm_mode = True

# class ReasonTreeNodeBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     parent_id: Optional[int] = None
#     reason_tree_id: int
    
# class ReasonTreeNodeCreate(ReasonTreeNodeBase):
#     pass

# class ReasonTreeNode(ReasonTreeNodeBase):
#     id: int
#     children: List[ReasonTreeNodeBase] = []
    
#     class Config:
#         orm_mode = True
        
# class ReasonTreeNodeWithTree(ReasonTreeNodeBase):
#     id: int
#     children: List[ReasonTreeNodeBase] = []
#     reason_tree: ReasonTreeBase
    
#     class Config:
#         orm_mode = True

# class AssetReasonTreeAssignmentBase(BaseModel):
#     asset_id: int
#     reason_tree_id: int
    
#     class Config:
#         orm_mode = True
        
# class AssetReasonTreeAssignmentCreate(AssetReasonTreeAssignmentBase):
#     pass
        
# class AssetReasonTree(AssetReasonTreeAssignmentBase):
#     id: int
#     asset: AssetBase
#     reason_tree: ReasonTreeBase
    
#     class Config:
#         orm_mode = True