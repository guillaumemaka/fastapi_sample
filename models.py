from datetime import datetime
from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db.db_setup import Base

class Event(Base):
    __tablename__ = "events"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True, unique=True)
    description: Mapped[str] = mapped_column(index=False, nullable=True)
    location: Mapped[str] = mapped_column(index=False, nullable=True)
    event_type: Mapped[str] = mapped_column(index=True, nullable=False)
    event_status: Mapped[int] = mapped_column(nullable=False)
    # event_status: Mapped[int] = mapped_column(ForeignKey("event_statuses.id"))
    # event_owner: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, server_default=func.now(), nullable=True)
    # asset_id: Mapped= mapped_column(ForeignKey("assets.id"))
    

# class Asset(Base):
#     __tablename__ = "assets"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
#     location = mapped_column(String, index=False)
#     asset_type = mapped_column(String, index=True)
#     asset_status = mapped_column(String, index=True)
#     asset_owner = mapped_column(String, ForeignKey("users.id"))


# class Downtime(Base):
#     __tablename__ = "downtimes"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
#     location = mapped_column(String, index=False)
#     downtime_type = mapped_column(String, index=True)
#     downtime_status = mapped_column(Integer, ForeignKey("downtime_statuses.id"))
#     downtime_owner = mapped_column(String, index=True)
#     downtime_timestamp = mapped_column(String, index=True)
#     downtime_end_time = mapped_column(String, index=True)
#     reason_level_1 = mapped_column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_2 = mapped_column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_3 = mapped_column(String, ForeignKey("reason_tree_nodes.id"))
#     reason_level_4 = mapped_column(String, ForeignKey("reason_tree_nodes.id"))
#     asset_id = mapped_column(Integer, ForeignKey("assets.id"))
#     event_id = mapped_column(Integer, ForeignKey("events.id"))
    
# class EventStatus(Base):
#     __tablename__ = "event_statuses"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
    
# class DowntimeStatus(Base):
#     __tablename__ = "downtime_statuses"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)

# class AssetStatus(Base):
#     __tablename__ = "asset_statuses"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
    
# class AssetStatusTransition(Base):
#     __tablename__ = "asset_statuses_transitions"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     from_status_type = mapped_column(Integer, ForeignKey("asset_statuses.id"))
#     to_status_type = mapped_column(Integer, ForeignKey("asset_statuses.id"))
    
# class User(Base):
#     __tablename__ = "users"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     email = mapped_column(String, index=True)
#     password = mapped_column(String, index=True)
#     is_active = mapped_column(Integer, index=True)
#     is_superuser = mapped_column(Integer, index=True)
    
# # Declare a table representation of a reason tree for downtime
# class ReasonTree(Base):
#     __tablename__ = "reason_trees"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
#     reason_tree = mapped_column(String, index=True)
#     root_node = mapped_column(Integer, ForeignKey("reason_tree_nodes.id"))

# # Declare a table representation of a node in a reason tree for downtime
# class ReasonTreeNode(Base):
#     __tablename__ = "reason_tree_nodes"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     name = mapped_column(String, index=True)
#     description = mapped_column(String, index=False)
#     parent_node = mapped_column(Integer, ForeignKey("reason_tree_nodes.id"))
#     reason_tree = mapped_column(Integer, ForeignKey("reason_trees.id"))
    
# class AssetReasonTreeAssignment(Base):
#     __tablename__ = "asset_reason_tree_assignments"
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     asset_id = mapped_column(Integer, ForeignKey("assets.id"))
#     reason_tree_id = mapped_column(Integer, ForeignKey("reason_trees.id"))


