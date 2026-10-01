## G2. The exact instructions each agent received

These are the prompts as sent, copied from the agents' own transcripts. They are included so the research can be repeated, extended or audited. Each research agent also received the channel brief by file path.

**Cap message sent to all eight research agents mid-run** (after the spend measurement):

> Budget update: please wrap up within about 20 more tool calls (hard limit 25) and send your final report.
>
> The user's credit budget is limited, so depth is now capped. Nothing you have gathered is lost.
> - Finish the thread you are on, then prioritize the highest-value remaining items for your slice. Do not start new broad sweeps.
> - First save/update your notes.md so nothing is lost, then send the final report in the format originally specified (max ~1,500 words, evidence grades, sources, caveats).
> - Save context: do not open large pages you do not need. If you must look at thumbnails, combine 8-12 of them into ONE contact-sheet image with Pillow and view that single image instead of viewing them one by one. View at most ~10 more images in total.
> - If something important is still unverified, mark it UNVERIFIED instead of searching further.

### Agent 1: Platform mechanics, specs, policies and testing tools

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: PLATFORM MECHANICS, SPECS, POLICIES AND TESTING TOOLS
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/platform
Cover, from official YouTube sources (Help Center, Creator Academy, Creator Insider, YouTube blog, official statements by YouTube staff such as Todd Beaupre, Rene Ritchie, Matt Koval, etc.) and reputable secondary reporting:
1. Exact current thumbnail specs (resolution, aspect ratio, file size, formats, minimum width), how thumbnails are displayed across surfaces (home feed on phone, suggested videos, search, TV, desktop) and at what displayed pixel sizes; where the duration stamp and other UI overlays sit and therefore which corners are unsafe for text; how Shorts covers/thumbnails work (custom cover vs frame selection, what is shown in the Shorts feed vs the channel page vs search).
2. How YouTube defines impressions and CTR, what the official statements say about CTR vs average view duration vs viewer satisfaction, what YouTube says about "good" CTR ranges and why CTR varies by traffic source (browse, suggested, search) and by audience; what "packaging" (title + thumbnail) means to YouTube staff; official statements about clickbait and what YouTube optimizes for.
3. The "Test & Compare" thumbnail A/B feature: exact mechanics (how many variants, what metric it optimizes - reported as watch time share rather than raw CTR - how long it runs, eligibility, limitations, results interpretation), plus any official or first-hand guidance on how to use it well.
4. YouTube policies that affect disaster/engineering-catastrophe thumbnails: thumbnail policy (misleading thumbnails, violent/graphic content, shocking imagery, age-restriction risk), advertiser-friendly guidelines for tragedy/disaster content and for thumbnails specifically (limited ads triggers), and anything specific about depicting real deaths/victims. The channel never shows graphic injuries, so determine what a safe-but-dramatic thumbnail looks like within the rules.
5. Disclosure rules that could touch this channel: YouTube's altered/synthetic content disclosure and AI-generated imagery rules (the channel uses AI-assisted narration and animation) and whether thumbnails are affected.
Give concrete numbers and quotes with source URLs. End with a checklist of hard technical/policy constraints every thumbnail for this channel must satisfy.
~~~

### Agent 2: Empirical evidence on what gets thumbnails clicked

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: EMPIRICAL EVIDENCE ON WHAT MAKES THUMBNAILS GET CLICKED
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/ctr-evidence
Find the best actual DATA (not vibes) on thumbnail performance:
1. Large-scale analyses and studies: VidIQ, TubeBuddy, Think Media, 1of10 (Jon Youshaei), Paddy Galloway, Colin and Samir, Nate O'Brien, Thumbnail testing platforms (ThumbnailTest, TubeBuddy A/B, etc.) and their published aggregate results; academic papers on YouTube thumbnails (computer vision studies on which visual features predict clicks, eye-tracking studies, clickbait research, thumbnail-title congruence); any dataset-based studies of faces, text, colors, number of words, brightness, saturation, object count, arrows/circles, before/after splits, etc.
2. First-hand experiments by named creators who published real A/B numbers (Veritasium/Derek Muller on thumbnails and titles, Mark Rober, MrBeast's production notes/memo, Ali Abdaal, Matt D'Avella, Kurzgesagt, Wendover, Real Engineering, Practical Engineering, Johnny Harris, Vox, Polymatter, etc.). Extract the exact numbers and what changed between variants.
3. What CTR ranges are considered normal by traffic source and channel size (with the source and its methodology), and how CTR relates to retention and to long-run growth; what happens when CTR rises but watch time falls.
4. A verdict table of the common thumbnail "rules" with evidence strength: human face vs no face, exaggerated emotion, number of words (0, 1-3, 4+), text vs no text, high saturation, warm vs cool colors, contrast/brightness, central single subject vs busy scene, arrows/circles/red highlights, before-vs-after or two-panel splits, close-up vs wide shot, illustrated vs photographic, mystery/hidden element, question marks, logos/branding elements, consistent series template vs varied. For each: supported / contested / myth, with the evidence.
5. Specific evidence for illustrated/cartoon/animated thumbnails versus photographic ones, and for educational/explainer/history/science niches versus entertainment.
Be especially careful to separate 'MrBeast-style entertainment thumbnails' from what works for educational explainer audiences.
~~~

### Agent 3: Psychology and visual perception of clicking

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: PSYCHOLOGY AND VISUAL PERCEPTION OF CLICKING
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/psychology
Find peer-reviewed or otherwise solid research (with citations, DOIs/URLs) on the mechanisms that make a small image in a feed get chosen, and translate each one into a concrete, testable thumbnail design principle:
1. Curiosity: Loewenstein's information-gap theory and follow-ups (e.g. curiosity peaks with a moderate gap and a promise of resolution; 'curiosity gap' in headlines; the role of knowing a little), question-format headlines vs statements, and how a picture can pose a question the title answers or the other way round.
2. Visual attention and saliency in feeds: pre-attentive features (color contrast, luminance contrast, size, isolation/pop-out), figure-ground, clutter and visual-search costs, how many elements a viewer can process in ~1 second at phone size, eye-tracking findings on thumbnails, reading of text overlays vs images, F-pattern and center bias, gaze cueing (a figure looking at something makes viewers look there).
3. Faces and emotion: research on faces capturing attention, and crucially on SCHEMATIC / cartoon / emoticon / stick-figure faces: do dot-eyes-and-line-mouth faces still trigger face detection, pareidolia, emotional contagion and attention capture? Does exaggeration help? What about expressions of fear, surprise, worry; negativity bias; and do faces without eyes contact, or objects with 'faces', work?
4. Threat, danger and anomaly: attention to hazards, 'something is wrong' detection, tension before the event (the moment before vs the aftermath), the role of scale (tiny human vs huge structure, size contrast), and the appeal of 'safe danger' for curious viewers; ethical framing for real tragedies.
5. Cognitive fluency and processing: simple images being liked and trusted more, 'one idea per image', rule of thirds vs central composition, symmetry, use of negative space, minimal text (word count that can be read at thumbnail size), color psychology evidence that is real vs folklore (red/yellow/blue claims), warm-vs-cool contrast, the effect of a limited consistent palette on recognition.
6. Familiarity and branding: mere-exposure effect, recognition of a channel by consistent visual identity, how much consistency helps vs hurts novelty in feeds (habituation / banner blindness).
For each principle give: the study, the finding, evidence strength, and a one-line 'how to use it in a cartoon stick-figure disaster thumbnail'. Flag where popular creator advice is unsupported by the research.
~~~

### Agent 4: Visual audit of the engineering-disaster and documentary niche

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: VISUAL AUDIT OF THE ENGINEERING-DISASTER / DOCUMENTARY NICHE (real thumbnails, actually looked at)
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/niche-audit
Task: study real thumbnails of the channels that compete for this audience. Candidate channels (verify each exists and pick the most relevant, add others you discover): Real Engineering, Practical Engineering, Mentour Pilot, Fascinating Horror, Wendover Productions, Polymatter, Half as Interesting, Veritasium, Vox, The B1M, Plainly Difficult, Disaster Breakdown, Lemmino, Mustard, Kyle Hill, Fern, Just Have a Think, Jared Owen, Scott Manley, Cleo Abram, Tom Scott, Real Life Lore, Dark Docs style channels, Grunge/Insider disaster documentaries, and any fast-growing 'engineering disaster' or 'why did X collapse/fail' channels from 2023-2026 (use searches to discover them).
Procedure:
1. For each channel, collect the video list with view counts (parse ytInitialData from the channel /videos page, also try the 'Popular' sort), then download the thumbnails (i.ytimg.com/vi/<id>/maxresdefault.jpg) of AT LEAST 5 of its most-viewed disaster/engineering videos and 3 of its least-viewed recent ones, and LOOK at them with the Read tool. Aim for 80+ thumbnails from 15+ channels in total. Save them in your folder with the video id, title and view count recorded in an index file (CSV). Report view counts only as read from pages you fetched, with the fetch date, and remember views depend on video age and channel size, so compare within a channel, not across.
2. Classify each thumbnail: subject (structure/disaster scene, person, object, diagram, map, split comparison, before/after...), composition (single focal point vs busy), text (word count, position, font style), color scheme, presence of faces/emotion, use of scale contrast, arrows/circles/highlights, photo vs illustration vs 3D render, the 'moment' shown (before, during, after), and the curiosity mechanism (what question does it raise?).
3. Extract the recurring visual FORMULAS (name them descriptively, e.g. 'the lone tiny structure under a huge looming threat') and note which formulas cluster among the top-viewed videos within each channel, and which cluster among the weak ones. Distinguish formulas that depend on photographic footage (which this channel cannot use) from those that translate into flat cartoon illustration.
4. Note gaps: what visual approaches are NOT being used in this niche (opportunities for differentiation) and what is overused.
5. Note how thumbnails handle death/tragedy tastefully vs sensationally, and what audience/comment reactions say (only if you actually read them).
In the final report include a table of the top ~12 formulas with 2-3 concrete example videos each (title, channel, video ID, views as fetched), and a list of what would translate to this channel's flat cartoon style.
~~~

### Agent 5: Visual audit of cartoon and stick-figure explainer channels

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: VISUAL AUDIT OF CARTOON / STICK-FIGURE / ANIMATED EXPLAINER CHANNELS (real thumbnails, actually looked at)
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/cartoon-audit
The brief says the narration is modelled on the channel "Ink Explainer". Study how flat-cartoon, stick-figure and hand-drawn animated explainer channels make thumbnails that get clicked WITHOUT photos or realistic people. Candidate channels (verify each exists, pick the most relevant, and discover others through searches, especially 2023-2026 growth stories): Ink Explainer, Kurzgesagt, TED-Ed, Oversimplified, Sam O'Nella Academy, Historia Civilis, Ten Minute History, TheOdd1sOut, Jaiden Animations, Casually Explained, MinuteEarth, MinutePhysics, Fireship-like illustrated tech channels, Vox-style illustrated shorts, Sideways, Bobby Duke Arts, Alex Trebek-style history animation channels, 'Explained in animation' disaster/true-crime/history channels (e.g. animated true-story or 'Fascinating Horror'-style) and stick-figure channels such as Zack D. Films-like, Draw My Life-style, Mark Rober-adjacent animation, Wendover-like maps, Bright Side/Ted-style etc. Use searches to find channels actually built on stick figures or simple cartoon characters that reached large audiences.
Procedure:
1. Collect video lists with view counts (parse ytInitialData from channel /videos pages; try the Popular sort), download the thumbnails of AT LEAST 5 top-viewed and 3 weak recent videos per channel, and LOOK at them with the Read tool. Aim for 80+ thumbnails from 15+ channels. Keep an index CSV (video id, title, channel, views as fetched, fetch date). Compare views within a channel only (age and channel size differ).
2. Determine how these thumbnails create curiosity and emotion using only flat cartoon means: character pose and face exaggeration, scale contrast, object-as-hero, split panels, color pops, background treatment (flat color vs full scene), outlines, text treatment (word count, font, placement), recurring templates, icon/props, hand-drawn 'imperfection'. Find what distinguishes a high performer from a weak one WITHIN the same channel.
3. Study specifically stick figures with minimal faces (round head, dot eyes, line mouth): how do thumbnails make them emotionally readable at phone size? Which poses, eyebrow angles, body language, prop placements and sizes work? Any evidence that these characters perform worse or better than realistic ones?
4. Study how these channels adapt a consistent visual identity across thumbnails and whether the top performers vary the layout or keep a template. Note specific palette/outline/lighting conventions.
5. Note failure modes: cluttered scenes, tiny characters, unreadable text, low contrast, pale palettes on the white YouTube feed background (and dark mode).
In the final report include the top ~12 formulas that work in flat cartoon style with 2-3 concrete examples each (channel, title, video ID, views as fetched), the pose/face 'vocabulary' for stick figures, and a list of specific mistakes to avoid.
~~~

### Agent 6: Design system, color math and production workflow

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: DESIGN SYSTEM, COLOR/CONTRAST MATH AND PRODUCTION WORKFLOW
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/design-system
The channel palette is fixed: #1a1a1a (ink), #ffffff, #f3ead8 (paper), #bfe2ea (sky), #8fbf5a, #4f7d3a (greens), #9a6b43 (brown), #d2b48c (tan), #e6b23a (amber), #d94a38 (red). Style rules: clean black outlines, soft flat colors with gentle cel shading, whole richly illustrated places, stick-figure characters (round white head, dot eyes, line brows and mouth, single-line limbs, one prop), and the image generator must NEVER put text, letters, numbers, arrows, dashed lines or motion lines inside images, so any thumbnail text (1-4 words) has to be added afterwards as a separate overlay layer.
Do real computation with Bash/python (write scripts in your folder):
1. Compute WCAG contrast ratios and also perceptual lightness differences (CIELAB delta E / L* difference, APCA if you can) for every pair of palette colors; list which pairs give strong pop-out at phone size for (a) text overlays, (b) a subject against a background, (c) outlines. Identify which palette colors work as the single accent that pulls the eye (#d94a38 vs #e6b23a), and which combinations fail (for example pale sky on paper white). Simulate the three common color-blindness types and report which pairs stay distinguishable.
2. Simulate how thumbnails look in the YouTube feed: white background (light mode) and near-black background (dark mode), at the actual displayed sizes (find them: about 360x202 px full-width on phones, about 168x94 for small suggested-video thumbnails, and around 246x138 or 360x202 on desktop; verify the numbers from sources). Build a small test rig in python (Pillow) that takes any image, renders it at those sizes on both backgrounds with the duration badge in the bottom-right corner and produces a contact sheet, and save it as tools/thumb_preview.py in your folder with usage notes. Test it on synthetic sample images using the palette.
3. Text overlays: research and recommend typeface classes and specific FREE fonts (Google Fonts) that match a hand-drawn cartoon explainer and stay legible at 168x94 px; minimum cap height in pixels for readability at that size; ideal word count; outline/stroke/shadow treatment to keep contrast on any palette background; placement that avoids the timestamp and other UI overlays. Give concrete numbers for a 1280x720 canvas.
4. Series consistency: research (with sources) how strongly a consistent template (color, layout, character) helps recognition vs. how it risks banner blindness, and propose a system of 'fixed anchors' (things that never change, e.g. outline weight, palette, ink-black text box, character style) versus 'variables' (composition, hero object, accent color, emotion) so that 10 different styles still look like one channel.
5. Production workflow: how to make these thumbnails with AI image generation (given the 'no text in the image' rule) and compositing: prompt structure that keeps stick-figure consistency (character sheet reference), how to request simple/bold compositions with big shapes, negative-space for text, what image generators struggle with (hands, small figures, consistent proportions, text), inpainting/edit tools, compositing tools (Figma, Canva, Photopea, Affinity, GIMP), export settings (1280x720, under 2 MB, sRGB, JPG vs PNG), and a per-thumbnail QA checklist (squint test, phone-size test, grayscale test).
Deliver hard numbers and a table of palette pair scores, and include the exact path of your preview script in the final report.
~~~

### Agent 7: From story to thumbnail moment (fact-checked)

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: FROM STORY TO THUMBNAIL MOMENT (FACT-CHECKED)
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/story-visuals
The channel's rule is 'nothing invented, ever', and a thumbnail must never promise something the video does not deliver. So the example thumbnails in the final deliverable need to be built on facts that are exactly right. Choose 12 well-documented engineering failures or failed inventions that PASS the channel's constraints (no ongoing legal cases; not less than 2 years old, i.e. nothing after 2024-09-30; no terrorism or deliberate attacks; no medical or financial advice; politics only as regulatory facts) and that differ in type so the thumbnails can vary: a dam or flood, a suspension/steel bridge, a building or walkway, an aircraft, a rocket/spacecraft, a nuclear or chemical plant, a ship or offshore platform, a tunnel or mine, a software/control-system failure, a failed invention or product, a structure that collapsed during construction, and a 'nothing broke but it still failed' case. Candidates to consider (verify status and facts, drop any that fail the filter or lack a solid primary source): Vajont Dam 1963, Tacoma Narrows Bridge 1940, Hyatt Regency walkways 1981, St. Francis Dam 1928, Challenger 1986, Sleipner A platform 1991, Ronan Point 1968, Tay Bridge 1879, de Havilland Comet 1954, Sampoong Department Store 1995, Banqiao Dam 1975, Quebec Bridge 1907, Therac-25, Mars Climate Orbiter 1999, Apollo 13 oxygen tank, Piper Alpha 1988, Kaprun 2000, Chernobyl 1986, Columbia 2003, Lac-Megantic 2013 (check the legal status), Grenfell/Morandi/Boeing 737 MAX (check whether legal cases are ongoing before considering), and any others you find that fit better.
For EACH of the 12 selected stories deliver, with source URLs for every fact:
1. Year, place, the verified headline numbers (deaths, size, cost, whatever is the strongest and clearly documented) with the primary source by name (official investigation/commission report, patent, memoir) and where it can be read.
2. The legal/age filter check result (state explicitly why it passes).
3. The single most striking VERIFIED physical or human moment or object that could carry a thumbnail without misleading: what exactly was seen or happened, and what can safely be depicted in a flat cartoon (for example: the one bolt/detail that failed, the size contrast, the 'nothing looked wrong' moment before, the cutaway of what no camera recorded). Be precise about what is documented vs. inferred, so the illustration never invents. Avoid graphic depiction of death.
4. The natural question-title a curious stranger would ask (must be a question, no colon, no case name first) and the honest promise of that title: what the video will actually deliver.
5. One 'planted object' candidate (a simple object that can appear in the opening, at the turn and at the end).
Finish with a short table of the 12 stories and a ranking of which are the strongest thumbnail candidates and why.
~~~

### Agent 8: Packaging strategy, title-thumbnail pairing, testing and Shorts

~~~text
You are one of 8 parallel research agents. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test.

## Project context
The user runs a YouTube channel called "Stress Riser": documentary-style stories of engineering disasters and failed inventions, told as a chain of small reasonable decisions, in English, for curious adults 18-50 in the US/UK/CA/AU who watch on their phone. Videos are hand-drawn cartoon animation with stick-figure characters (flat colors, black outlines). Every video title is a question (e.g. "Why did 1,900 people die under a dam that never broke?"). Long-form is 8-12 min; Shorts are 45-60 s. Read the full brief first: /home/user/test/stress-riser/channel-brief.md. The whole project will end with 10 clearly different thumbnail styles that suit this channel and maximize click-through rate (CTR). You own ONE research slice, below. Today is 2026-09-30.

## Research rules (strict)
- Be rigorous, detailed and exact. Take as long as you need. Use many sources (aim for 15+ distinct, credible ones for your slice), and prefer 2024-2026 material but note classic older work.
- NEVER invent statistics, quotes, video IDs, view counts or studies. Every quantitative claim needs: source URL, date, and what exactly was measured. If you cannot verify a claim, write "UNVERIFIED" next to it or leave it out.
- Grade every finding: [A] official documentation / peer-reviewed / large dataset; [B] first-hand data reported by a creator or company; [C] opinion or anecdote. Report contradictions between sources and call out myths (things repeated everywhere that the evidence does not support).
- Tools: load WebSearch and WebFetch with ToolSearch (query "select:WebSearch,WebFetch"). Bash curl works through the proxy for youtube.com pages and for thumbnails at https://i.ytimg.com/vi/<VIDEOID>/maxresdefault.jpg (fallback hqdefault.jpg); the Read tool can view downloaded images. WebFetch summaries come from a small model, so for critical facts fetch the raw page with curl and grep it. Channel video lists: curl "https://www.youtube.com/@Handle/videos" returns HTML containing ytInitialData JSON (videoId, title, viewCountText) that you can parse with python; try the popular sort too.
- Work in your own folder: create it with mkdir -p and save notes and downloads there. Write a detailed notes file (notes.md) with all findings, URLs and evidence grades as you go.
- Your final reply (this is what I receive) must be a dense, structured report of at most ~1,500 words: key findings with evidence grades, what each means for thumbnails for THIS channel (cartoon stick figures, question titles, disaster subject matter, phone viewers), the sources list, and caveats/what you could not verify. Write it in English.

## Your slice: PACKAGING STRATEGY, TITLE-THUMBNAIL PAIRING, TESTING AND ITERATION (LONG-FORM AND SHORTS)
Your folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/packaging
Research how the best educational and documentary channels treat the title + thumbnail as ONE unit and how they test and iterate, then turn it into a practical system for a NEW or small channel:
1. Title-thumbnail pairing: principles from Paddy Galloway, Jon Youshaei/1of10, Colin and Samir, Veritasium (Derek Muller's talks on titles and thumbnails), Kurzgesagt, Wendover, Real Engineering, Mark Rober, MrBeast's leaked production memo, Nathan Graham, Think Media, and YouTube staff. What must the thumbnail say that the title does not (complementarity vs repetition)? How should a QUESTION title (this channel's fixed format) pair with the image and with 0-4 words of thumbnail text? Give concrete pairing patterns and 8+ real examples you fetched (title, thumbnail, channel, video ID, views as fetched, date) with analysis of why the pair works or fails. Include how long a title can be before it truncates on phones (find real limits) and how thumbnail text should avoid repeating truncated title text.
2. Curiosity vs clickbait: how top educational channels stay honest (deliver on the promise) while still winning the click; what YouTube and viewers punish (e.g. satisfaction surveys, early drop-off); how to write a thumbnail that raises a question the video really answers. The channel's brief forbids clickbait the video does not deliver.
3. Testing: how to run thumbnail tests on a small channel (Test & Compare mechanics, minimum impressions, statistical significance rules of thumb, traffic-source mixing, how long to wait, avoiding false wins), what to change in each variant (one variable at a time vs. radically different concepts), the day-1/day-2/week-1 refresh cadence and what creators report about changing thumbnails after publishing.
4. Cold-start reality: what CTR do new/small channels get, how the first impressions are tested on small subscriber groups, and which thumbnail properties matter most when the audience does not know the channel yet (recognition of the topic vs the brand).
5. Consistent identity vs variety across many videos: case studies (Kurzgesagt, Veritasium, Practical Engineering, Real Engineering, Ink Explainer, etc.) showing how top channels balance a recognizable template with novelty; evidence on 'series blindness'.
6. Shorts: how Shorts covers work (custom cover, frame selection, what viewers actually see in the feed vs on the channel page vs search), whether the cover matters for swipe-through, and what good Shorts covers look like for animated explainers; what is the fast 'first-frame' equivalent of a thumbnail for Shorts (the brief demands the outcome in the first 3 seconds).
End with a step-by-step packaging workflow (title first or thumbnail first, number of concepts drafted, tests, decision rules) that fits a small channel producing one long video per week.
~~~

### Reviewer 1: fact and claim audit

~~~text
You are an adversarial fact-checker. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test. Write scratch files only under /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/review/factcheck (create it). Use at most about 45 tool calls. Today is 2026-09-30.

## What you are checking
A report for the YouTube channel "Stress Riser" (engineering-disaster explainers; the channel's non-negotiable rule is "nothing invented, every number, date, name and quote is one you are certain of from the sources"). The report proposes 10 thumbnail styles: /home/user/test/stress-riser/thumbnail-styles.md. The Slovenian captions of the visual gallery are in /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/build/make_lookbook.py (do not open the 3 MB HTML file; it is base64). The channel brief is /home/user/test/stress-riser/channel-brief.md. The report was written from eight research agents' notes, copied to /home/user/test/stress-riser/research/*.md (platform, ctr-evidence, psychology, niche-audit, cartoon-audit, design-system, packaging, story-visuals); raw pages, CSV indexes and downloaded files are under /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/<name>/ .

## Your tasks
1. Read thumbnail-styles.md completely. List every factual or numeric claim (statistics, dates, view counts, video IDs, study names and findings, platform rules, policy statements, story facts, evidence grades A/B/C) and check each against the research notes. Flag any claim that is (a) not supported by the notes, (b) stronger than the notes say (overstated, dropped hedge, wrong evidence grade, correlational finding presented as causal), (c) attributed to the wrong source, or (d) contradicted elsewhere in the same report or by another research note.
2. Spot-check at least 12 of the most consequential claims against live primary sources with curl or WebFetch (outbound HTTPS works through a proxy; YouTube watch pages are bot-gated, Help pages and most others are fine). Suggested: the thumbnail spec and 2 MB / 50 MB limits (support.google.com/youtube/answer/72431); the 2-10% CTR statement (answer 7628154); Test & Compare mechanics and the 480p downscale rule (answer 16391400); Vajont death toll and dam height (Italian Civil Protection page or ASDSO); Hyatt "essentially doubled" (NBS report nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir82-2465.pdf); Big Dig 26 tons (NTSB HAR0702.pdf); Tacoma 42 mph and 1 July / 7 Nov 1940 (wsdot.wa.gov/tnbhistory/); Challenger 36 F and 15 F colder (Rogers Commission volume 1 on nasa.gov/history/rogersrep/); Flixborough "no drawing" (hse.gov.uk/comah/sragtech/caseflixboroug74.htm); Blackout 14:14 (energy.gov Blackout Final report); 1of10's 19% text, 36% cyan and 11% numbers-in-titles (1of10.com/blog/what-actually-makes-a-youtube-video-go-viral-in-2025/). For every spot-check report: claim, source, exact supporting quote or number, verdict (confirmed / partly / not found / contradicted).
3. Check the example video IDs, titles and view counts cited in the report against the CSV indexes and notes (cartoon-audit/index.csv, niche-audit/index2.csv, packaging notes, etc.). Report mismatches.
4. Recompute the sample-size table (two-proportion test, 80% power, alpha 0.05) and report if any figure is off by more than 5%.
5. Check every draft title in section 5: it must be a question, no colon, no case name first, about 60 characters or fewer; and every overlay word must add information the title does not already say.
6. Check the story-fact registry (section 8): does each row say only what the primary source says, with the right confidence? Are any of the 'myths' actually supported by the notes?
7. Check the Slovenian captions in make_lookbook.py for factual drift from the English report (numbers, hedges).

## Output
Reply with at most ~1,300 words in English: a verdict line, then a numbered list of findings ordered by severity (MUST-FIX = a false or unsupported factual claim; SHOULD-FIX = overstatement or wrong hedge; NIT). For each: where (section/style), what is wrong, evidence, and the exact replacement wording. Then the spot-check table. Be adversarial. Do not praise. If something is fine, say nothing about it.
~~~

### Reviewer 2: brief compliance and design critique

~~~text
You are an adversarial design and brief-compliance reviewer. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test. Write scratch files only under /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/review/design (create it). Use at most about 45 tool calls. Today is 2026-09-30.

## What you are reviewing
The YouTube channel "Stress Riser" has a strict brief: /home/user/test/stress-riser/channel-brief.md (read all of it: voice, visual style, palette, character rules, 'Must never appear in images', forbidden topics, title rules). A report proposes 10 distinct thumbnail styles: /home/user/test/stress-riser/thumbnail-styles.md. Ten vector mockups (final composites with an overlay text layer) are in /home/user/test/stress-riser/thumbnails/NN-*.png; the image-only layers (what an image generator would output, no words) are in thumbnails/art-only/; editable SVGs are in thumbnails/svg/; the generator code is in tools/scenes.py and tools/lib.py; a phone-size test sheet is thumbnails/qa-phone-sizes.png. Use the Read tool to LOOK at the PNGs (it shows images). Research notes with evidence are in /home/user/test/stress-riser/research/*.md.

## Your tasks
1. Palette audit with Python (Pillow, numpy are available): scan every composite and art-only PNG for pixels outside the 10 brand colors (#1a1a1a, #ffffff, #f3ead8, #bfe2ea, #8fbf5a, #4f7d3a, #9a6b43, #d2b48c, #e6b23a, #d94a38), ignoring antialiasing at edges (for example count only pixels farther than a small distance from every palette color and from a blend of two neighbours), and grep the SVG fill/stroke values. Report the share of off-palette pixels per file and any off-palette color used on purpose.
2. Art-only layer audit: for each file in art-only/ (and the styles that have no words: 03 and 07 composites) confirm there is no text, letter, digit, arrow, dashed line, motion line, diagram symbol, logo, watermark. Try OCR (rapidocr-onnxruntime may be installed: try `python3 -c "import rapidocr_onnxruntime"`; if not, do not pip install anything large, just inspect visually). Also check the thumbnails' shapes for accidental arrows or diagram-like symbols (for example a windsock that reads as an arrow, a bolt with thread lines that reads as a diagram).
3. Character rules from the brief: check every stick figure in the ten mockups (read tools/lib.py figure() and look at the images): round white head with black outline, two dot eyes, line eyebrows and mouth, small white body, limbs as SINGLE thin black lines in every shot including the close-up, no fingers, shoes, trousers, sleeves; only one prop; no smile unless asked. Report violations and questionable cases (for example the side view in style 9, the very large head in style 10, the three-figure crowd in style 8, the clipboard and thermometer props, a figure that has two props).
4. Check each of the 10 styles against the brief's 'Never' list, forbidden topics, tone rules and title rules: question titles with no colon and no case name first; failures attributed to systems not people; nothing graphic; nothing that mocks; no victims depicted; honest promise (does the picture show only what the documented story delivers? use research/story-visuals.md for the documented moments and the facts registry in thumbnail-styles.md section 8). Flag any depiction that is invented or inaccurate (for example the Hyatt rod-and-nut geometry, the Comet airliner, the Vasa hull and gunports, the Quebec chord, the Flixborough bypass, the Challenger stack, the Big Dig anchor).
5. Distinctness: are the ten styles truly different concepts (as needed for YouTube's Test & Compare, where small tweaks cannot be detected)? Name any pair that is effectively the same layout or same idea, and any style that is really a variant of another. Is any style so dependent on one story that it cannot be reused? Rate the ten from strongest to weakest concept for THIS channel and say why.
6. Phone-size legibility: look at qa-phone-sizes.png. Do you agree with the verdicts in section 6 of the report? Which mockups fail the 168 px squint test? Would a stranger understand the subject at a glance?
7. The report's design-system rules (section 4) and the safe zones: check whether the mockups actually obey them (text margins 64/36 px, bottom-right 230x90 px free, top-right about 110x110 px free, cap height at least 90 px for the main word, one red accent 3-8% of the frame, amber only on ink, red and amber never touching, ink edge band on dark scenes). Measure with Python where possible.
8. Missing: is there an important style the evidence supports that the ten miss, or a style among the ten that the evidence does not support and should be replaced? Keep it short and justified from the research notes.
9. Give concrete fixes for the three weakest mockups (which elements to enlarge, recolor or move, with approximate coordinates on the 1280x720 canvas).

## Output
Reply with at most ~1,300 words in English: a verdict line, then a numbered list of findings ordered by severity (MUST-FIX = violates the brief or misdepicts a documented fact; SHOULD-FIX; NIT), each with where, what, evidence and the exact fix. Then the ranked list of the ten styles. Be adversarial. Do not praise. If something is fine, say nothing about it.
~~~

### Reviewer 3: verification of the master synthesis

~~~text
You are an adversarial fact-checker for NEW synthesis text. Do NOT spawn other agents. Do NOT edit, commit or push anything in /home/user/test. Write scratch files only under /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/review/master (create it). Use at most about 35 tool calls. Today is 2026-10-01.

## Context
The channel "Stress Riser" (engineering-disaster explainers) has a strict rule: "nothing invented, every number, date, name and quote is one you are certain of from the sources". A research project (eight research agents, two reviewers) produced thumbnail research. A master dossier was then compiled. Its NEW text (written by the orchestrator, not by the research agents) is in /home/user/test/stress-riser/master/:
- A-summary-sl.md (Slovenian summary)
- B1-context-and-method.md, B2-key-numbers.md, B3-myths-and-contradictions.md, B4-recommendations.md, B5-roadmap-risks-decisions.md, B6-review-audit-and-spend.md
The sources of truth for those claims are:
- the eight final research reports and two review reports: /home/user/test/stress-riser/master/reports/*.md
- the raw notes: /home/user/test/stress-riser/research/*.md
- the corrected report of the ten styles: /home/user/test/stress-riser/thumbnail-styles.md
- the channel brief: /home/user/test/stress-riser/channel-brief.md
- data tables: /home/user/test/stress-riser/data/*.csv and *.md
- the agents' transcripts (for tool-call counts, durations, costs): /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/tasks/*.output (large JSONL files: NEVER print them; parse them with Python and print only aggregates)

## Your tasks
1. B2-key-numbers.md is a ledger of facts, numbers and quotes (about 200 rows). Check EVERY row against the reports and notes: wrong numbers, wrong units, wrong attribution (who said it, which study, which year), wrong evidence grade, quotes that are not verbatim, claims stronger than the source, claims not in any source. Be exhaustive on numbers.
2. B3-myths-and-contradictions.md: check each myth and contradiction row (verdict and reason) against the sources; flag anything unsupported or overstated.
3. B1: check the method table (tool calls, durations, estimated costs per agent) against the transcripts (count tool_use blocks in assistant messages per agent file; durations from first and last timestamps; costs are estimates from usage fields at $2/$10 per million input/output, $0.20 cache read, $2.50 cache write: just check they are plausible and the totals add up). Check the brief-constraint table against channel-brief.md and the 'observations about the brief' for accuracy.
4. B4: check that every recommendation is supported by the reports (or clearly marked as the orchestrator's heuristic), that numbers and specs match the sources (text spec, color rules, export sizes, margins, testing arithmetic), and that nothing contradicts the brief.
5. B5: check the 10-video rotation table: each row must have one human, one mechanism and one scale-or-scene variant and must NOT put two 'close cousins' together (cousins: 1 and 8; 4 and 5; 2 and 9). Check the log template and risks for consistency with the sources.
6. B6: check that each status ('Fixed', 'Partly', 'Open', 'Moot') matches what thumbnail-styles.md and the mockup code (/home/user/test/stress-riser/tools/scenes.py) actually now contain; check the reviewers' findings are summarised accurately against master/reports/review-*.md; check the spend table.
7. A-summary-sl.md: check it against the English content for drift in numbers or hedges; check basic Slovenian grammar problems you are confident about (do not nitpick style).
8. Check every cross-reference in these files (for example 'see C6', 'D1', 'G8', 'F1', 'E1', 'H1', 'B3', 'B4.7'): the chapter or section it names must exist and must contain what is claimed. The chapter scheme: Part A summary; B1-B6 synthesis; C1-C12 = sections 1-12 of thumbnail-styles.md; D1-D8 = the eight final reports in this order: platform, ctr-evidence, psychology, niche-audit, cartoon-audit, design-system, story-visuals, packaging; E1-E2 = review-factcheck, review-design; F1-F6 data; G1 intro, G2 briefs, G3-G10 = raw notes in this order: platform, ctr-evidence, psychology, niche-audit, cartoon-audit, story-visuals (G8), design-system, packaging; H1 sources, H2 brief, H3 file map, H4 glossary.

## Output
Reply with at most ~1,200 words in English: a verdict line; then a numbered list of findings ordered by severity (MUST-FIX = a false or unsupported factual claim or a wrong number; SHOULD-FIX = overstatement, wrong hedge or grade, broken cross-reference; NIT). For each: file and row or section, what is wrong, the evidence (file and quote), and the exact replacement text. Then one line saying how many B2 rows you checked. Be adversarial. Do not praise. If something is fine, say nothing about it.
~~~
