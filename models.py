import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import func
from db.db_setup import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    description = Column(String, index=False, nullable=True)
    location = Column(String, index=False, nullable=True)
    event_type = Column(String, index=True, nullable=False)
    event_status = Column(Integer, nullable=False)
    # event_status = Column(Integer, ForeignKey("event_statuses.id"))
    # event_owner = Column(String, ForeignKey("users.id"))
    event_timestamp = Column(DateTime, index=True, default=func.now, nullable=False)
    # asset_id = Column(Integer, ForeignKey("assets.id"))
    

# class Asset(Base):
#     __tablename__ = "assets"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
#     location = Column(String, index=False)
#     asset_type = Column(String, index=True)
#     asset_status = Column(String, index=True)
#     asset_owner = Column(String, ForeignKey("users.id"))


# class Downtime(Base):
#     __tablename__ = "downtimes"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
#     location = Column(String, index=False)
#     downtime_type = Column(String, index=True)
#     downtime_status = Column(Integer, ForeignKey("downtime_statuses.id"))
#     downtime_owner = Column(String, index=True)
#     downtime_timestamp = Column(String, index=True)
#     downtime_end_time = Column(String, index=True)
#     reason_level_1 = Column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_2 = Column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_3 = Column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_4 = Column(String, ForeignKey("reason_tree_nodes.id"))
#     asset_id = Column(Integer, ForeignKey("assets.id"))
#     event_id = Column(Integer, ForeignKey("events.id"))
    
# class EventStatus(Base):
#     __tablename__ = "event_statuses"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
    
# class DowntimeStatus(Base):
#     __tablename__ = "downtime_statuses"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)

# class AssetStatus(Base):
#     __tablename__ = "asset_statuses"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
    
# class AssetStatusTransition(Base):
#     __tablename__ = "asset_statuses_transitions"
    
#     id = Column(Integer, primary_key=True, index=True)
#     from_status_type = Column(Integer, ForeignKey("asset_statuses.id"))
#     to_status_type = Column(Integer, ForeignKey("asset_statuses.id"))
    
# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, index=True)
#     password = Column(String, index=True)
#     is_active = Column(Integer, index=True)
#     is_superuser = Column(Integer, index=True)
    
# # Declare a table representation of a reason tree for downtime
# class ReasonTree(Base):
#     __tablename__ = "reason_trees"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
#     reason_tree = Column(String, index=True)
#     root_node = Column(Integer, ForeignKey("reason_tree_nodes.id"))

# # Declare a table representation of a node in a reason tree for downtime
# class ReasonTreeNode(Base):
#     __tablename__ = "reason_tree_nodes"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=False)
#     parent_node = Column(Integer, ForeignKey("reason_tree_nodes.id"))
#     reason_tree = Column(Integer, ForeignKey("reason_trees.id"))
    
# class AssetReasonTreeAssignment(Base):
#     __tablename__ = "asset_reason_tree_assignments"
    
#     id = Column(Integer, primary_key=True, index=True)
#     asset_id = Column(Integer, ForeignKey("assets.id"))
#     reason_tree_id = Column(Integer, ForeignKey("reason_trees.id"))


