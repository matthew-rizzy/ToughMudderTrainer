# workout_plan.py
# Stores the structured workout plan data

# Note: Ensure 'key' is unique within each day's list of tasks.
# The full unique ID for database storage (like 'week1-thu-frontsquat-check' or 'week1-thu-frontsquat-weight')
# will be constructed in the template/backend based on week, day, and this key.

WORKOUT_PLAN = [
    # Week 1: April 2 – 8
    {
        "week_num": 1, "dates": "April 2 – 8",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 139, "unit": "lbs"},
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 40, "unit": "lb dumbbells"},
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 70, "unit": "lbs/hand"},
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"}, # Changed from string list item
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"}, # Changed from string list item
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 70, "unit": "lbs/hand"},
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"}, # Kept simple for now
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
    # Week 2: April 9 – 15
    {
        "week_num": 2, "dates": "April 9 – 15",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 144, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 40, "unit": "lb dumbbells"},
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 75, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 75, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"},
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
    # Week 3: April 16 – 22
    {
        "week_num": 3, "dates": "April 16 – 22",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 149, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 45, "unit": "lb dumbbells"}, # Updated
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 80, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 80, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"},
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
     # Week 4: April 23 – 29
    {
        "week_num": 4, "dates": "April 23 – 29",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 154, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 45, "unit": "lb dumbbells"},
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 85, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 85, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"},
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
    # Week 5: April 30 – May 6
    {
        "week_num": 5, "dates": "April 30 – May 6",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 159, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 50, "unit": "lb dumbbells"}, # Updated
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 90, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 90, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"},
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
    # Week 6: May 7 – 13
    {
        "week_num": 6, "dates": "May 7 – 13",
        "days": {
            "Wednesday": [
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 164, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 50, "unit": "lb dumbbells"},
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 95, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [
                "**Active Recovery + Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(swim/row/zone 2 walk)"},
                "**Grip Work:**",
                {"type": "simple", "key": "deadhange", "exercise": "Dead Hangs", "details": "3x Max (goal: 30–45s)"},
                {"type": "simple", "key": "wristroller", "exercise": "Wrist Roller", "details": "3x sets (moderate resistance)"},
                {"type": "simple", "key": "towelrow", "exercise": "Towel Ring Rows", "details": "3x8"},
                {"type": "weighted", "key": "farmercarry_fri", "exercise": "Farmer Carries", "details": "2x40 yds", "default_weight": 95, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [
                "**Mountain Biking + Grip Burner**",
                {"type": "simple", "key": "mtb", "exercise": "Mountain Biking", "details": "60–90 mins moderate-hard intensity"},
                "**Grip Burner:**",
                {"type": "weighted", "key": "kbswing", "exercise": "KB Swings", "details": "3x20", "default_weight": 53, "unit": "lbs"},
                {"type": "simple", "key": "towelpullup", "exercise": "Towel Pull-ups", "details": "3 sets to failure"},
                {"type": "simple", "key": "platepinch", "exercise": "Plate Pinch Carries", "details": "3x30s @ 25 lb plates"},
                {"type": "weighted", "key": "trapbarcarry", "exercise": "Trap Bar Farmer Carry", "details": "2x40 yds", "default_weight": 180, "unit": "lbs Total"}, # Range 180-200, default 180
            ],
            "Sunday": [
                "**Full Rest**",
                "Stretch, hydrate, high-protein meals, optional sauna or cold plunge."
            ]
        }
    },
    # Week 7: May 14 – 17 (Taper Week)
    {
        "week_num": 7, "dates": "May 14 – 17",
        "days": {
            "Wednesday": [ # May 14
                "**Obstacle Simulation Run**",
                {"type": "simple", "key": "run", "exercise": "Run", "details": "5 miles"},
                {"type": "simple", "key": "pushups", "exercise": "Push-ups", "details": "10 (every mile)"},
                {"type": "simple", "key": "airsquats", "exercise": "Air Squats", "details": "10 (every mile)"},
                {"type": "simple", "key": "burpees", "exercise": "Burpees", "details": "5 (every mile)"},
                {"type": "simple", "key": "pullup_hang", "exercise": "Pull-up / Dead Hang", "details": "1 pull-up or 10s dead hang (every mile)"}
            ],
            "Thursday": [ # May 15
                "**Lower Body Power + Carries**",
                {"type": "weighted", "key": "frontsquat", "exercise": "Front Squat", "details": "3x8", "default_weight": 169, "unit": "lbs"}, # Updated
                {"type": "weighted", "key": "dbthruster", "exercise": "DB Thrusters", "details": "3x12", "default_weight": 55, "unit": "lb dumbbells"}, # Updated
                {"type": "simple", "key": "sledpush", "exercise": "Sled Push", "details": "2x20 yds (heavy)"},
                {"type": "weighted", "key": "farmercarry", "exercise": "Farmer's Carry", "details": "2x40 yds", "default_weight": 100, "unit": "lbs/hand"}, # Updated
                {"type": "simple", "key": "boxjump", "exercise": "Box Jumps", "details": "3x8 (24–30” box)"},
                {"type": "simple", "key": "battleropes", "exercise": "Battle Ropes Tabata", "details": "4 rounds (20s on / 10s off)"},
                "**Core Finisher:**",
                {"type": "simple", "key": "plankwalkout", "exercise": "Plank Walkouts", "details": "3x10"},
                {"type": "simple", "key": "hangingraise", "exercise": "Hanging Knee Raises", "details": "3x12"},
                {"type": "weighted", "key": "russiantwist", "exercise": "Russian Twists", "details": "3x20 (10/side)", "default_weight": 25, "unit": "lb plate"},
            ],
            "Friday": [ # May 16 - Lighter Recovery
                "**Active Recovery + Light Grip**",
                {"type": "simple", "key": "lightcardio", "exercise": "Optional light cardio", "details": "(short walk/swim)"},
                "**Light Grip Work:**",
                {"type": "simple", "key": "deadhange_light", "exercise": "Dead Hangs", "details": "2x 20-30s"}, # Specific taper instruction
                {"type": "simple", "key": "mobility", "exercise": "Mobility", "details": "hips, ankles, shoulders"}
            ],
            "Saturday": [ # May 17 - Very Light / Rest
                "**Pre-Race Prep / Rest**",
                {"type": "simple", "key": "lightactivity", "exercise": "Very light activity", "details": "Short walk"},
                {"type": "simple", "key": "prep", "exercise": "Prep", "details": "Focus on hydration, nutrition, packing"},
                {"type": "simple", "key": "mentalprep", "exercise": "Mental Prep", "details": ""}
            ],
            # No Sunday for Week 7 as plan ends May 17
        }
    },
]

# --- Add-ons & Nutrition ---
# These are just displayed, not actively tracked with weights/checkboxes via this structure

PRIORITY_ADDONS = {
    "Pull-Up Progression": [
        "Grease the Groove: Do 2–3 sets of pull-ups (or assisted) spread throughout the day",
        "Goal: Add 1 unassisted pull-up per week"
    ],
    "Grip Training": [
        "Dead Hangs: 3 sets to failure every workout",
        "Fat Gripz or Towels on Pull Movements",
        "Plate Pinch Carries: 2x per week",
        "Towel Pull-ups or Rows 2x per week"
    ],
    "Recovery": [
        "Sleep: 7.5–9 hours per night",
        "Foam roll post-lift and post-run",
        "Track soreness and mood each morning (quick journal or app)"
    ]
}

NUTRITION_GUIDE = {
    "Daily Nutrition": [
        "Protein: 0.8–1g per pound of bodyweight (approx. 145–180g/day)",
        "Carbs: 2–2.5g per pound on training days for fuel",
        "Fats: ~0.3–0.4g per pound",
        "Hydration: At least 0.7 oz of water per pound of bodyweight"
    ],
    "Supplements": [
        "Creatine Monohydrate: 5g daily",
        "Electrolyte Mix: Especially before/after long runs or hot days",
        "Fish Oil: 1–2g EPA/DHA for joint health",
        "Multivitamin (optional): If diet lacks diversity"
    ],
    "Pre-Workout (Optional)": [
        "Caffeine + Beta-Alanine blend for tough gym sessions",
        "Avoid right before evening workouts"
    ],
    "Fuel During Long Runs": [
        "Banana or small carb source beforehand",
        "Electrolyte gummies or water mix mid-run"
    ]
}
