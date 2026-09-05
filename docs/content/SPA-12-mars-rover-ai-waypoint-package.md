# Draft for Carlos review — not for publication

## Package 1: Mars rover AI waypoint planning

**Prepared:** 2026-09-05\
**Editorial status:** Offline draft for Chief of Staff source/metadata/claim-mapping QA, then Carlos review. This is not final editorial approval or authorization to publish, produce, upload, contact sources, incur spend, or access production systems.\
**Approved angle:** “When a Mars rover uses generative AI to plan a drive, what is the AI deciding—and what remains under human control?”

## 1. Topic brief

**Proposal — audience.** Curious non-specialists who have seen a headline saying AI “drove” on Mars but do not know the difference between route planning and onboard navigation.

**Proposal — audience promise.** Map the documented handoff precisely: a vision-language model generated orbital-scale route waypoints; JPL engineers reviewed and simulated the commands before transmission; Perseverance’s established AutoNav software handled local terrain during execution.

**Verified fact.** NASA/JPL reported that Perseverance completed two drives on 2025-12-08 and 2025-12-10 using generative-AI-produced waypoints, covering 210 and 246 meters. [C-01]

**Analysis — thesis.** “AI drove the rover” compresses several different decisions into one phrase. The evidence supports a bounded change to the ground route-planning workflow, not end-to-end unsupervised rover operation. [C-01–C-07]

**Proposal — tone and length.** A cautious, visually clear 6–8 minute explainer. Define jargon once; avoid anthropomorphism; separate demonstrated results from forecasts and vendor claims.

**Open question.** Carlos has not selected the companion format in the approved plan. Both a lightweight article outline and teaching-notebook outline appear below.

## 2. Claim-level source ledger

Access date for every URL: **2026-09-05**.

| ID | Material claim | Label | Canonical URL | Publisher | Publication date | Claim-specific support and limitation |
| --- | --- | --- | --- | --- | --- | --- |
| C-01 | A vision-language model used HiRISE orbital imagery and digital-elevation-model slope data to generate waypoints for drives on Dec. 8 and 10, 2025; JPL ran commands through a digital twin and verified more than 500,000 telemetry variables before sending them; the rover drove 210 m and 246 m. | **Verified fact** | https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/ | NASA Jet Propulsion Laboratory | 2026-01-30 | Primary mission release. Supports inputs, output, workflow, dates, and distances. It does not establish independent command authority, comparative safety, or workload savings. |
| C-02 | AutoNav uses rover-camera data to build 3D terrain maps, identify hazards, and plan around obstacles; the team develops plans, signs off, and transmits instructions. | **Verified fact** | https://www.jpl.nasa.gov/news/nasas-self-driving-perseverance-mars-rover-takes-the-wheel/ | NASA Jet Propulsion Laboratory | 2021-07-01 | Primary operational explainer. Supports ground-team/onboard-navigation separation. The headline “self-driving” is shorthand, not unlimited autonomy. |
| C-03 | During the 2023 Snowdrift Peak traverse, humans mapped the general route while AutoNav handled finer navigation and detoured around rocks not visible in orbital imagery. | **Verified fact** | https://www.jpl.nasa.gov/news/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars/ | NASA Jet Propulsion Laboratory | 2023-09-21 | Primary mission example of layered decision-making. Its speed comparisons are context-specific and are not generalized here. |
| C-04 | Perseverance uses several bounded autonomy systems rather than one general-purpose “AI brain”; the reviewed paper describes autonomous capabilities spanning navigation, science targeting, and planning. | **Verified fact** | https://doi.org/10.1126/scirobotics.adi3099 | Science Robotics (AAAS) | 2023-07-19 | Peer-reviewed technical overview. Predates the 2025 generative-waypoint trial and does not evaluate it. |
| C-05 | Rapid-traverse operations could combine an initial directed drive, intermediate waypoints selected by planners, and AutoNav for real-time hazard avoidance. | **Verified fact** | https://doi.org/10.1109/AERO55745.2023.10115835 | IEEE Aerospace Conference | 2023-03-04 | JPL-authored conference paper supporting the distinction among directed driving, waypoint placement, and onboard navigation. Describes 2022 operations, not the AI trial. |
| C-06 | ENav evaluates terrain and candidate paths onboard; as of sol 1312, about 90% of Perseverance’s 32.1 km of driving had used ENav to evaluate terrain. | **Verified fact** | https://doi.org/10.1109/TFR.2025.3636366 | IEEE Transactions on Field Robotics | 2025-11-24 | Peer-reviewed algorithm and operations context. The percentage is cumulative through 2024-10-28 and should not be treated as a statistic about the December 2025 demonstration. |
| C-07 | Anthropic identifies Claude as the model used, says it built waypoints in 10 m segments, and reports that engineers made minor changes after review. | **Verified fact** | https://www.anthropic.com/features/claude-on-mars | Anthropic | 2026-01-30 | First-party vendor disclosure adds implementation detail. Interested-party evidence; its estimated time savings and future autonomy claims are not independently established here. |
| C-08 | The generative model performed one bounded part of ground planning; it did not replace mission intent, engineering review, command transmission, or onboard local navigation in the documented demonstration. | **Analysis** | Synthesis of C-01, C-02, C-03, C-05, and C-07 | Space Exploration News draft | 2026-09-05 | Claim wording deliberately tracks documented actions. “Did not replace” refers to these two demonstrations, not every future workflow. |
| C-09 | Two completed drives do not by themselves demonstrate improved safety, speed, consistency, or labor efficiency versus human waypoint planning. | **Analysis / open question** | Evidentiary gap across C-01 and C-07 | Space Exploration News draft | 2026-09-05 | Anthropic reports an internal estimate of halved planning time; NASA’s release supplies no comparative study. Do not state a benefit as fact without data or independent evaluation. |

## 3. YouTube outline

1. **Hook — “Who drove?”** Two real Mars drives, and why the obvious headline is incomplete. [C-01]
2. **Define a waypoint.** A fixed location where the rover takes up a new set of instructions; distinguish a strategic route from wheel-by-wheel motion. [C-01, C-05]
3. **Show the inputs and output.** Orbital imagery plus terrain-slope data went in; a continuous waypoint path came out. [C-01]
4. **Insert the validation gate.** Engineers reviewed the work, used rover simulation/digital-twin checks, and then the commands were sent. [C-01, C-07]
5. **Move onboard.** AutoNav used rover cameras to detect hazards and select short local paths. [C-02, C-03, C-06]
6. **Draw the decision stack.** Mission intent → proposed waypoints → engineering validation/uplink → local navigation.
7. **Demonstrated versus not demonstrated.** Two successful drives are not evidence of unsupervised mission control or comparative gains. [C-01, C-09]
8. **Close on the real significance.** One labor-intensive planning step was tested with generative AI inside an existing safety and operations workflow. [C-08]

## 4. Spoken draft (945 words including production cues and inline claim labels)

**Proposal — script.**

[ON SCREEN: Perseverance track over orbital imagery. Text: “Who drove?”]

In December 2025, NASA’s Perseverance rover completed two drives on Mars using route waypoints generated by a vision-capable form of generative AI. One drive covered 210 meters. The other covered 246. NASA described them as the first drives on another world planned by artificial intelligence. [**Verified fact:** C-01]

That can sound like a chatbot was handed the keys to a Mars rover.

But the real story is more precise—and more interesting. This was a layered handoff among a generative model, human engineers, and navigation software already aboard Perseverance. Each layer made a different kind of decision. [**Analysis:** C-08]

[ON SCREEN: “1. Mission intent  2. Route waypoints  3. Local path”]

Start with a waypoint. A waypoint is a fixed location along a planned route, a little like one breadcrumb in a trail. It tells the rover where to head next. It does not specify every turn of every wheel between here and there. [**Verified fact:** C-01; **Analysis:** plain-language analogy]

Human rover planners normally study orbital images, terrain information, and the rover’s condition to lay out those breadcrumbs. For these two demonstrations, a vision-language model took on that route-planning task. A vision-language model is software that can work with images and language-like instructions. Here, it analyzed high-resolution HiRISE images taken from orbit and slope data derived from elevation models. It identified features including bedrock, boulder fields, and sand ripples, then generated a continuous path with waypoints. [**Verified fact:** C-01]

That was a meaningful decision: which broad path should connect the rover’s starting point to its destination?

It was also a bounded decision.

The public NASA account does not say the model chose Perseverance’s science goals or independently transmitted commands to Mars. Instead, JPL engineers processed the drive commands through a digital twin—a virtual replica used to check compatibility with the rover. NASA says the team verified more than 500,000 telemetry variables before sending the commands. Anthropic’s account adds that engineers reviewed the route and made minor changes where ground-level camera views revealed terrain detail the model had not seen. [**Verified fact:** C-01, C-07]

[ON SCREEN: “AI proposal → engineering review and simulation → uplink”]

This is the safest answer to what remained under human control: in the workflow described publicly, people framed and ran the demonstration, reviewed and simulated its output, adjusted part of the route, and sent the resulting commands. NASA’s earlier description of normal Perseverance operations says specialists develop the navigation and activity plan, sign off, and beam instructions to Mars. [**Verified fact:** C-01, C-02, C-07]

Notice how narrow that wording is. We can document those actions. We cannot turn them into a complete responsibility chart for every operational decision without more evidence. [**Analysis:** editorial limitation]

Now move from Earth to the rover.

Route planning is not the same as local navigation. Orbital images provide the big picture, but they cannot reveal every drive-scale obstacle. Perseverance already had an onboard system called AutoNav. Its navigation cameras feed software that builds three-dimensional maps of nearby terrain, identifies hazards, and selects a path around obstacles without asking Earth about each wheel movement. [**Verified fact:** C-02]

We saw that division of labor before this generative-AI test. In 2023, human planners mapped Perseverance’s general route through a boulder field called Snowdrift Peak. AutoNav handled the finer path, including detours around rocks that were not visible in the orbital imagery. [**Verified fact:** C-03]

The rover’s current Enhanced Autonomous Navigation system, or ENav, evaluates terrain and candidate paths while respecting engineering constraints. A technical paper reports that, by October 2024, roughly 90 percent of Perseverance’s 32.1 kilometers of driving had used ENav to evaluate terrain. That statistic gives context for how established local autonomy already was. It does not measure the new generative-AI experiment. [**Verified fact:** C-06]

[ON SCREEN: Orbital route with widely spaced dots beside rover-camera view bending around a rock.]

So the new part was not that Perseverance suddenly learned to avoid a rock. The new part was upstream: a generative model drafted the waypoint trail normally prepared by human route planners. Existing onboard software still handled a different problem—choosing safe, immediate motion through terrain the rover could see. [**Analysis:** C-08]

That is why saying simply “AI drove on Mars” is misleading. Perseverance does not have one all-purpose AI brain. Its autonomy consists of bounded capabilities. A peer-reviewed overview describes separate systems for navigation, science targeting, and onboard planning. Even inside driving, a JPL operations paper distinguishes directed driving, intermediate waypoints, and real-time hazard avoidance. [**Verified fact:** C-04, C-05]

[ON SCREEN: “What was demonstrated / What remains unknown”]

What did these two drives demonstrate? A vision-language model generated waypoints from mission data. The commands passed the team’s checks. Perseverance then completed both drives. [**Verified fact:** C-01]

What did they not establish? They did not show a generative model independently running the rover mission, authorizing its own commands, or replacing AutoNav. And successful completion alone does not prove the new method is safer, faster, or less labor-intensive than human waypoint planning. Anthropic reports an estimate that the workflow could halve planning time, but NASA’s public release provides no comparative study. That benefit remains an open question, not a verified result. [**Analysis / open question:** C-07, C-09]

The careful conclusion is still remarkable. Engineers tested generative AI in one consequential piece of interplanetary route planning, checked its work, and placed it inside an established operational stack. The achievement is not a rover escaping human control. It is a sharper example of how control can be divided—across people on Earth, a model proposing a route, and a machine on Mars navigating the ground in front of it. [**Analysis:** C-08]

## 5. Companion options

### Option A — companion article outline

**Proposal — headline:** *Who Is Really Driving? Inside Perseverance’s Generative-AI Route Test*

1. Two drives and the exact NASA claim: dates, distances, and waypoint output. [C-01]
2. What a waypoint decides—and what it does not. [C-01, C-05]
3. The ground workflow: model proposal, human review, simulation, and uplink. [C-01, C-02, C-07]
4. The onboard workflow: camera-based mapping, hazard detection, and ENav. [C-02, C-03, C-06]
5. A “demonstrated / not demonstrated” table. [C-08, C-09]
6. Visible source notes and a short methods box explaining the first-party/vendor evidence distinction.

### Option B — teaching-notebook outline

**Proposal — notebook title:** *Waypoints Are Not Wheel Commands: A Toy Mars Route Planner*

1. Markdown introduction with the real mission workflow and explicit warning that the notebook is illustrative, not flight software.
2. Create a small synthetic grid with passable ground, steep cells, and rocks; no NASA imagery or copyrighted mission assets required.
3. Plot a human-defined start and destination plus several strategic waypoints.
4. Use a simple A* pathfinder—not generative AI—to show how a local planner can connect nearby points while avoiding hazards.
5. Change one waypoint and visualize how the local path changes without altering the mission destination.
6. Reflection prompts: Which decisions came from humans, the waypoint generator, and the local planner? What real constraints are absent?
7. Sources and limitations cell tied to C-01, C-02, C-05, and C-06.

**Open question.** Carlos should select Option A or B at the companion-format gate. The article is faster to review; the notebook makes the planning/navigation distinction tangible but requires technical QA.

## 6. Revision note

**Analysis.** This package narrows the earlier phrasing “humans retained mission control” to observable workflow: engineers reviewed and simulated the commands, adjusted part of the route, and sent the commands to Mars. That avoids implying a full governance or authorization structure the public sources do not document.

**Proposal.** Keep the three-layer visual, but label the middle output “proposed route waypoints” until Carlos approves stronger wording. Avoid using Anthropic’s planning-time estimate in narration except as an attributed, unverified vendor claim.

## 7. Unresolved-question and editorial-risk register

| Item | Label | Why unresolved / risk | Required treatment or owner |
| --- | --- | --- | --- |
| Which person or mission role formally authorized each command set? | **Open question** | Public sources describe review and transmission but not a complete responsibility matrix. | Carlos decides whether the narrow workflow wording is sufficient; otherwise request a primary mission-operations source before assertion. |
| Did generative waypoint planning reduce planning time, improve safety, or improve consistency? | **Open question** | Only the vendor publishes a time-saving estimate; no comparative NASA dataset or peer-reviewed evaluation was found. | Keep out of verified narration; attribute if retained. |
| Did the model generate final flight commands or draft route artifacts later converted by JPL tooling? | **Open question** | NASA says the AI created waypoints and the team processed drive commands; Anthropic says Claude wrote Rover Markup Language. The exact tool boundary is not fully documented. | Use “generated waypoints” as the stable cross-source claim. |
| “First AI-planned drive” terminology | **Analysis / risk** | “AI” can obscure decades of onboard autonomous navigation; NASA’s claim refers specifically to planning drives on another world. | Always explain the scope immediately. |
| Companion format | **Open question** | Approved plan records no selection. | Carlos selects article or notebook; notebook then receives technical QA. |
| Visual assets | **Open question / copyright risk** | NASA/JPL assets usually carry credits and may have third-party marks; this package does not clear any asset. | Obtain asset-specific credit/use review before production. No asset download is authorized here. |
| Vendor framing | **Analysis / conflict risk** | Anthropic benefits reputationally from the story. | Use its page only for attributed implementation detail and flag unverified promotional/future claims. |
| Investment or sponsorship implications | **Analysis / risk** | AI/space coverage can be read as endorsement. | Include no investment advice, valuation language, affiliate framing, or implied sponsor endorsement. |

## 8. Research and verification disclosure

**Verified process statement.** Generative AI assisted with research organization and drafting. Each cited URL was re-opened or independently surfaced during research on 2026-09-05, and claim-specific limits are recorded above. The script uses paraphrase rather than direct quotations. Bibliographic metadata and all material claim mappings remain subject to Chief of Staff QA and Carlos’s editorial review.

**Draft for Carlos review — not for publication.**
