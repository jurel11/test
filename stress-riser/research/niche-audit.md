# Niche audit: engineering-disaster / documentary thumbnails (fetch date 2026-09-30)

Folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/niche-audit
- index.csv / index2.csv : 405 thumbnails (channel, video id, title, views AS LISTED on channel page at fetch, age as listed, image stats)
- thumbs/ : 405 JPGs (maxresdefault, hqdefault fallback). sheet_*.jpg : 9 contact sheets (12 thumbs each) that were actually viewed.
- data/*.json : parsed ytInitialData (recent = default /videos tab, popular = Popular sort via youtubei continuation)
- yt.py, search.py, discover*.py, analyze.py : scripts.

## Method and honesty notes
- View counts come from channel /videos pages (recent list: "1.3M"; popular list: "14M views", rounded to 2 significant figures) fetched 2026-09-30. Exact counts from watch pages could not be parsed (regex found no viewCount) -> only rounded counts, except where a YouTube SEARCH page showed an exact number (marked "search page"). [B: first-hand platform data]
- 58 channels fetched; 405 thumbnails downloaded and measured (brightness, saturation, warm/cool share, edge density). Because of a budget cap, only ~105 thumbnails (9 contact sheets: PE+Fascinating Horror; Brick Immortar+Plainly Difficult; Dark Records+Storified; Hydraulic Record+Mentour+Disaster Breakdown; B1M+Sabin+Real Engineering; Ink Explainer+OverSimplified+Infographics; USCSB+Andy R+Jared Owen+Kyle Hill; 12 LOW performers; small fast channels Overengineered/Beyond Sky/Forgotten Disasters/Iron and Memory) were VISUALLY classified. The rest were measured programmatically only.
- Comment reactions were NOT read -> UNVERIFIED.
- Views depend on video age, topic, search demand and channel size. Top-viewed videos are mostly OLD evergreen; "low" group = lowest-viewed among the latest ~30 uploads (mostly 1-9 months old). Compare within channel only.

## Channels verified (subs at fetch)
T1 (direct niche): Practical Engineering @PracticalEngineeringChannel 4.83M; Real Engineering 5.12M; Mentour Pilot 2.51M; Fascinating Horror 1.46M; Plainly Difficult 1.1M; Disaster Breakdown 262K; The B1M 4.08M; Sabin Civil Engineering 6.97M; Dark Records 653K; Brick Immortar 401K; Dark Docs 1.2M (military history mostly); The Hydraulic Record 25.3K; What On Earth Is This? 109K; Storified 164K; That Chernobyl Guy 108K; USCSB 427K (official US Chemical Safety Board 3D animations); Andy R Animations 72.9K; Oceanliner Designs 970K; Mayday: Air Disaster 1.11M; Kyle Hill 2.83M; Two Bit da Vinci 814K; The Infographics Show 15.5M; Scott Manley 1.87M; Adam Something 1.32M; The Efficient Engineer 1.5M; Tom Scott 6.74M; Overengineered 11.5K (6 videos, one at 4.2M in 1 month); Beyond Sky 38.3K; Forgotten Disasters 7.2K; Iron and Memory 18.9K; Dennis Farley 1.86K; Casey Jones PE 78.8K; donoteat01 (Well There's Your Problem) 90.2K; jeffostroff 748K.
T2 (explainer neighbours): Veritasium 21.3M; Vox 12.7M; Wendover 4.92M; PolyMatter 1.93M; Half as Interesting 2.94M; LEMMiNO 5.92M; Mustard 2.39M; fern 5.54M; Just Have a Think 746K; Jared Owen 4.44M; Cleo Abram 8.79M; RealLifeLore 7.94M; Joe Scott 2.56M; Lost Industries 24.1K.
T3 (cartoon/illustrated analogues): Ink Explainer @Inkexplainer96 106K (NOTE @InkExplainer is a different 39-sub channel); OverSimplified 9.64M; Simple History 5.11M; Casual Geographic 4.31M; Simple Paint 514K; Kurzgesagt 25.6M; TED-Ed 22.9M; MinuteEarth 3.33M.
Checked and NOT relevant: Insider @Insider 9.61M (lifestyle/"how X works", no disaster docs in top 14); Grunge @GrungeHQ 2.53M (celebrity/trivia; recent uploads are rock-music lists at 2K-13K views). Vox has the one relevant classic: "This plane could cross the Atlantic in 3.5 hours. Why did it fail?" a_wuykzfFzE 17M.
Discovery: many tiny 2025-26 channels (hundreds of views) imitate "one small change killed 114 people" titles (e.g. @MarginofError404, @Old_Alignment, @EngineeringPostMortem): the phrase/format is getting crowded by low-view, likely AI-assisted channels (my inference from search results, view counts read from search pages 2026-09-30).

## Quantitative check (own computation on 268 T1 thumbnails; within-channel top vs low, 32 channels)
mean(top-low): luminance +0.012, saturation +0.004, dark-pixel share -0.023, warm-hue share -0.023, red share -0.017, cool share +0.022, edge density (busyness) -0.002; top>low in only 12-19 of 32 channels for every metric = coin flip. => Global colour/brightness/busyness do NOT separate strong from weak within a channel [own analysis, confounded by age].
Niche colour profile: T1 mean luminance 0.43, near-white share 8%, dark share 21%; T3 cartoon channels luminance 0.52, near-white 20%, dark 15%. The disaster niche skews dark and photographic; light flat-colour thumbnails are rare there.

## Visual classification (viewed contact sheets)
See report. Key tallies (own eyeball count, approximate): of ~75 viewed thumbnails with text, median 3-4 words, max 7, nearly all <= 6; text position mostly top-left or right third; typefaces: condensed heavy sans (Hydraulic Record, Overengineered, Storified), serif/gothic (Fascinating Horror, Forgotten Disasters, Brick Immortar), rounded bold yellow/white (Ink Explainer). Faces: only Hydraulic Record (6/6, same worried presenter), Practical Engineering (2/6, smiling host) and cartoon channels; aviation/structure channels show none. Death: dominant approach = no bodies, structure/vehicle only; casualty numbers used as hooks; sensational end = Storified ("IMPALED", "BRUTAL DEATH"), Plainly Difficult recall thumbnail with crash dummy.

## Example rows (title | channel | id | views as listed 2026-09-30)
- The Nepal Flood: What We Know | Hydraulic Record | 9pH_3n23_8o | 2M ("WHERE THE FLOOD WENT")
- Teton Dam: The Dam That Failed Its First Fill | Hydraulic Record | aRYq2kuHL2E | 1M ("THE ELEVEN")
- Banqiao Dam: The Deadliest Dam Failure in History | Hydraulic Record | CFnh54FeNo0 | 358K ("62 DAMS GONE")
- How Close Oroville Dam Came to Failing in 2017 | Hydraulic Record | mwwdnfaNKxk | 132K ("3 FEET FROM DISASTER")
- DISASTROUS INDIFFERENCE: The Loss of SS El Faro | Brick Immortar | -BNDub3h2_I | 4.8M
- CRUSH DEPTH: The Nightmarish Loss of USS Thresher | Brick Immortar | g-uJ1do3yV8 | 4.7M
- OFFSHORE NIGHTMARE: The Collapse of Texas Tower 4 | Brick Immortar | yal0RZvzW-0 | 2.4M
- The Sunshine Skyway Bridge Disaster | Fascinating Horror | EPaBRegvkuQ | 4.6M
- The Halifax Explosion | Fascinating Horror | VA8jIgvA8fo | 2.6M
- Joints Stuffed With Newspaper: The Ronan Point Disaster | Fascinating Horror | BtJUbTa8q0M | 2.7M
- A Brief History of: The Demon Core | Plainly Difficult | VE8FnsnWz48 | 7.9M
- A Brief History of: The Sodium Reactor Experiment Accident | Plainly Difficult | 7-NKdWV5SCg | 1.6M
- The Bizarre Paths of Groundwater Around Structures | Practical Engineering | bY1E2IkvQ3k | 14M
- Why Are Beach Holes So Deadly? | Practical Engineering | 0kQXOTcEB_E | 7M
- The Wild Story of the Taum Sauk Dam Failure | Practical Engineering | zRM2AnwNY20 | 11M
- What's inside the Titanic? | Jared Owen | HLrBUwNSEo0 | 22M
- Golden Gate Bridge | The CRAZY Engineering behind it | Sabin Civil | E6tp8DCAJ-0 | 19M
- The 2020 Beirut Explosion Disaster Documentary | Dark Records | NgQ7jh9mrWs | 4.8M ("1,500 TONS OF TNT")
- The Kaprun Alpine Railway Disaster 2000 | Dark Records | 0SFcWZx3L4g | 2.7M ("161 PEOPLE")
- They Kept Driving Off the Bridge - Sunshine Skyway Disaster | Storified | 0QXvhtPaKoY | 613K ("26 PEOPLE")
- Killed in 4 Milliseconds - America's Deadliest Nuclear Accident | Storified | iorhSlFYpDc | 2.7M ("IMPALED")
- The Crash that KILLED Concorde | Mentour Pilot | C-nALYF73hU | 16M ("THE REAL STORY")
- What REALLY Caused the Worst Airport Disaster In History?! | Mentour Pilot | 2d9B9RN5quA | 11M
- Did This Small Mistake Kill Everyone? (Air Canada) | Disaster Breakdown | wSmtnuFoAv0 | 1.4M
- 777X: The "Simple Upgrade" That Became Boeing's WORST Nightmare | Beyond Sky | 4UM9ZJx6fLI | 1.2M ("BUILT BY CLOWNS")
- The Real Reason Why China's Airbus A320 Clone Failed | Beyond Sky | JeVIb9K6a5U | 1.6M ("CHINA'S BIG MISTAKE")
- Why Airlines Are REJECTING Boeing's Brand-New 777X | Beyond Sky | Scc1nRqhPo0 | 1.7M in 6 days ("WHAT WAS BOEING THINKING?")
- What Did Ancient Humans Actually Do All Day? | Ink Explainer | 49_Ph2q6uIM | 9.7M in ~1 month ("NO JOBS"); channel median of its top-14 ~340K, so 9.7M is a ~28x outlier
- What Did Ancient Humans Do When It Rained All Week? | Ink Explainer | SD7XyG2wd1k | 1.5M
- Why Are We the Only Human Species Left? | Ink Explainer | OCr6NteWSQ8 | 1.2M ("Why Us?")
- Small Decisions That Caused HUGE Impacts on History | The Infographics Show | vRAsU_ov84Q | 957,455 (search page, 2026-09-30; "SMALL THING -> BIG OUTCOME": key -> sinking Titanic)
- Chernobyl Nuclear Explosion Disaster Explained (Hour by Hour) | Infographics Show | 2uJhjqBz5Tk | 6,136,985 (search page)
- The 400 km Wall Japan Built to Stop the Sea | Overengineered | Eg0djVfKXU8 | 4.2M ("JAPAN DID IT"), channel 11.5K subs
- The Tragic Story of the Bath School Disaster of 1927 | Forgotten Disasters | xa4d7sXaDgc | 178K, channel 7.2K subs
- The Spinning Giants: Flywheels That Stored Dangerous Power | Iron and Memory | HN2svHJpRRg | 668K, channel 18.9K subs
- Weak examples (same template as strong ones): FORTH BRIDGE ALMOST A DISASTER (Brick Immortar 0tEEVNHbUWQ 300K); Fascinating Horror Shorts compilation typographic (FTkmRF_TYRQ 74K); Disaster Breakdown "They Blamed One Guy / April 1st Video" (sFNhVrv6L6o 67K); Storified "ESCAPED" (zVR8Dqmn5WQ 20K); Hydraulic Record "HISTORY REPEATS" (-KBjE-6B_ws 19K); Real Engineering Sagrada Familia 1926/2026 split (UiPJbxryrkU 413K); B1M Tokyo Skytree text-less aerial (dbmXZUZwdeg 358K).

## Caveats / unverified
- Causation between thumbnail and views is NOT established anywhere in this audit.
- No CTR data (only YouTube Studio has it). No comments read.
- Rounded view counts; ages as listed by YouTube.
- 300 of 405 thumbnails measured but not visually inspected (budget cap).
