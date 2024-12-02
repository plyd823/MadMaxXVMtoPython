# List of bio IDs to unlock
bio_ids = [
    "bio_max", "bio_scrotus", "bio_chum", "bio_corw_dazzle", "bio_jeet", "bio_gutgash", "bio_warpup", 
    "bio_jabberboy", "bio_top_dog_1", "bio_sniper", "bio_spotter", "bio_rammerhead", "stank_gum_rat_soldier", 
    "stank_gum_tweakrod", "stank_gum_scatterbug", "bio_roadkill_pup", "bio_roadkill_shanks", 
    "bio_roadkill_pounder", "bio_roadkill_sniper", "bio_roadkill_spotter", "bio_roadkill_crusher", 
    "bio_buzzard_night_lizard", "bio_buzzard_spiker", "bio_buzzard_fire_raider", "bio_location_great_white", 
    "bio_location_dead_barrens_pass", "bio_location_graveyard", "bio_location_chums_hideout", 
    "bio_location_jeet_territory", "bio_location_jeet_stronghold", "bio_location_gutgash_territory", 
    "bio_location_gutgash_stronghold", "bio_location_outer_graves", "bio_location_fuel_veins_region", 
    "bio_location_dry_gustie_region", "bio_location_balefire_flatland_region", "bio_location_blackmaws_region", 
    "bio_location_colossus_region", "bio_location_grit_canyons_region", "bio_location_chalkies_region", 
    "bio_location_statue", "bio_tool_canteen", "bio_tool_binoculars", "bio_tool_flaregun", 
    "bio_tool_small_jimmy_bar", "bio_tool_shotgun", "bio_tool_harpoon", "bio_tool_sniper_gun", 
    "bio_tool_melee_weapons", "bio_tool_fuel_can"
]

# Function to quietly unlock all bios
def quietly_unlock_bio():
    for bio_id in bio_ids:
        game.PostEvent("quietly_unlock_bio", bio_id)

# Assuming the game object is initialized and available
class Game:
    @staticmethod
    def PostEvent(event, bio_id):
        print(f"Event '{event}' triggered for bio ID '{bio_id}'")

# Initialize game object
game = Game()

# Trigger the unlock process
quietly_unlock_bio()
