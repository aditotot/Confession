# This is database.py
import pymongo 

# --- Guild Configuration (Confession Channel) ---
async def set_confession_channel(db, guild_id, channel_id):
    """Sets the confession channel for a guild."""
    await db.guild_config.update_one(
        {"_id": guild_id},
        {"$set": {"channel_id": channel_id}},
        upsert=True
    )

async def get_confession_channel(db, guild_id):
    """Gets the confession channel config for a guild."""
    return await db.guild_config.find_one({"_id": guild_id})

# --- Confession Index (Counter) ---
async def set_confession_index(db, guild_id, number):
    """Sets the confession counter. The next confession will be this number."""
    await db.guild_counters.update_one(
        {"_id": guild_id},
        {"$set": {"index": number - 1}},
        upsert=True
    )

async def get_next_confession_index(db, guild_id):
    """Increments and returns the next confession index."""
    result = await db.guild_counters.find_one_and_update(
        {"_id": guild_id},
        {"$inc": {"index": 1}},
        upsert=True,
        return_document=pymongo.ReturnDocument.AFTER
    )
    return result.get("index", 1) 

# --- Log Channel Configuration ---
async def set_log_channel(db, guild_id, target_guild_id, target_channel_id):
    """Sets the cross-server logging destination."""
    await db.log_config.update_one(
        {"_id": guild_id},
        {"$set": {
            "target_guild_id": target_guild_id,
            "target_channel_id": target_channel_id
        }},
        upsert=True
    )

async def get_log_channel(db, guild_id):
    """Gets the log channel destination."""
    return await db.log_config.find_one({"_id": guild_id})

# --- Confession Index Mapping (UPDATED) ---

async def save_confession_map(db, guild_id, index, channel_id, message_id, type):
    """Saves the mapping of confession index, message details, and type."""
    await db.confession_map.update_one(
        {"guild_id": guild_id, "index": index},
        {"$set": {"channel_id": channel_id, "message_id": message_id, "type": type}}, # <-- Saves 'type'
        upsert=True
    )

async def get_confession_map(db, guild_id, index):
    """Retrieves the mapping of confession index to message details."""
    return await db.confession_map.find_one({"guild_id": guild_id, "index": index})