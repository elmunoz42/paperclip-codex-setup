# Draft for Carlos review — not for publication

## Package 1: Mars rover AI waypoint planning

**Prepared:** 2026-09-05\
**Repository revision:** 2 — independent QA and editorial cleanup, 2026-09-05\
**Editorial status:** Revised draft for Carlos review. QA was performed by the Codex collaborator in this conversation; the original Paperclip Chief of Staff confirmation is not represented as accepted. See the [QA report](SPA-12-qa-report.md) and [review packet](SPA-12-review.md).\
**Approved angle:** “When a Mars rover uses generative AI to plan a drive, what is the AI deciding—and what remains under human control?”

## 1. Topic brief

**Proposal — audience.** Curious non-specialists who have seen a headline saying AI “drove” on Mars but do not know the difference between route planning and onboard navigation.

**Proposal — audience promise.** Map the documented handoff precisely: a vision-language model generated orbital-scale route waypoints; JPL engineers reviewed and simulated the commands before transmission; Perseverance’s established AutoNav software handled local terrain during execution.

**Verified fact.** NASA/JPL reported that Perseverance completed two drives on 2025-12-08 and 2025-12-10 using generative-AI-produced waypoints, covering 210 and 246 meters. [C-01]

**Analysis — thesis.** “AI drove the rover” compresses several different decisions into one phrase. The evidence supports a bounded change to the ground route-planning workflow, not end-to-end unsupervised rover operation. [C-01–C-07]

**Proposal — tone and length.** A cautious, visually clear 6–8 minute explainer. Define jargon once; avoid anthropomorphism; separate demonstrated results from forecasts and vendor claims.

**Open question.** Carlos has not selected the companion format in the approved plan. Both a lightweight article outline and teaching-notebook outline appear below.

## 2. Claim-level source ledger

QA access date: **2026-09-05**. Seven external source records (C-01–C-07); C-08–C-09 are analysis, not additional sources. Access methods and metadata limits are recorded in the [QA report](SPA-12-qa-report.md).

| ID | Material claim | Label | Canonical URL | Publisher | Publication date | Claim-specific support and limitation |
| --- | --- | --- | --- | --- | --- | --- |
| C-01 | A vision-language model used HiRISE orbital imagery and digital-elevation-model slope data to generate waypoints for drives on Dec. 8 and 10, 2025; JPL ran commands through a digital twin and verified more than 500,000 telemetry variables before sending them; the rover drove 210 m and 246 m. | **Verified fact** | https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/ | NASA Jet Propulsion Laboratory | 2026-01-30 | Primary mission release. Supports inputs, output, workflow, dates, and distances. It does not establish independent command authority, comparative safety, or workload savings. |
| C-02 | AutoNav uses rover-camera data to build 3D terrain maps, identify hazards, and plan around obstacles; the team develops plans, signs off, and transmits instructions. | **Verified fact** | https://www.jpl.nasa.gov/news/nasas-self-driving-perseverance-mars-rover-takes-the-wheel/ | NASA Jet Propulsion Laboratory | 2021-07-01 | Primary operational explainer. Supports ground-team/onboard-navigation separation. The headline “self-driving” is shorthand, not unlimited autonomy. |
| C-03 | During the 2023 Snowdrift Peak traverse, humans mapped the general route while AutoNav handled finer navigation and detoured around rocks not visible in orbital imagery. | **Verified fact** | https://www.jpl.nasa.gov/news/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars/ | NASA Jet Propulsion Laboratory | 2023-09-21 | Primary mission example of layered decision-making. Its speed comparisons are context-specific and are not generalized here. |
| C-04 | The paper surveys AutoNav, autonomous science targeting (AEGIS), and an OnBoard Planner then planned for operational use. “Bounded capabilities” is our interpretation of that architecture. | **Verified fact** | https://doi.org/10.1126/scirobotics.adi3099 | Science Robotics (AAAS) | 2023-07-26 | Corrected against the author’s JPL bibliography. Abstract checked via indexed research record; publisher full text returned 403. OBP was described as planned for operational use in September 2023, not already operational at publication. Predates the waypoint trial. |
| C-05 | Rapid-traverse operations could combine an initial directed drive, intermediate waypoints selected by planners, and AutoNav for real-time hazard avoidance. | **Verified fact** | https://doi.org/10.1109/AERO55745.2023.10115835 | IEEE Aerospace Conference | 2023; JPL lists 2023-03-07 | JPL author bibliography supplies March 7 as the conference listing date; precise online-publication date not verified. Section 7 (p. 7), checked through indexed JPL paper text, supports directed start, planner-selected waypoints, and AutoNav hazard avoidance. Describes earlier operations, not the AI trial. |
| C-06 | ENav evaluates terrain and candidate paths onboard; as of sol 1312, about 90% of Perseverance’s 32.1 km of driving had used ENav to evaluate terrain. | **Verified fact** | https://doi.org/10.1109/TFR.2025.3636366 | IEEE Transactions on Field Robotics | 2025-11-24 | IEEE-indexed abstract supports the historical statistic; JPL author bibliography confirms publication date. Full text was not reviewed. Removed the statistic from narration; it is optional background, not evidence about the December demonstration. |
| C-07 | Anthropic identifies Claude as the model used, says it built waypoints in 10 m segments, and reports that engineers made minor changes after review. | **Verified fact** | https://www.anthropic.com/features/claude-on-mars | Anthropic | Not displayed in retrieved page | Full page checked; the original January 30 publication date was not substantiated by the visible article and is no longer asserted. JPL independently identifies Claude. Ten-meter segments and minor route edits remain attributed vendor details. |
| C-08 | The generative model performed one bounded part of ground planning; it did not replace mission intent, engineering review, command transmission, or onboard local navigation in the documented demonstration. | **Analysis** | Synthesis of C-01, C-02, C-03, C-05, and C-07 | Space Exploration News draft | 2026-09-05 | Claim wording deliberately tracks documented actions. “Did not replace” refers to these two demonstrations, not every future workflow. |
| C-09 | Two completed drives do not by themselves demonstrate improved safety, speed, consistency, or labor efficiency versus human waypoint planning. | **Analysis / open question** | Evidentiary gap across C-01 and C-07 | Space Exploration News draft | 2026-09-05 | Anthropic reports an internal estimate of halved planning time; NASA’s release supplies no comparative study. Do not state a benefit as fact without data or independent evaluation. |

## 3. YouTube outline

1. **Hook — “Who drove?”** Two real Mars drives, and why the obvious headline is incomplete. [C-01]
2. **Define a waypoint.** A target location along a route; distinguish a strategic route from wheel-by-wheel motion. [C-01, C-05]
3. **Show the inputs and output.** Orbital imagery plus terrain-slope data went in; a continuous waypoint path came out. [C-01]
4. **Insert the validation gate.** Engineers reviewed the work, used rover simulation/digital-twin checks, and then the commands were sent. [C-01, C-07]
5. **Move onboard.** AutoNav used rover cameras to detect hazards and select short local paths. [C-02, C-03, C-06]
6. **Draw the decision stack.** Mission intent → proposed waypoints → engineering validation/uplink → local navigation.
7. **Demonstrated versus not demonstrated.** Two successful drives are not evidence of unsupervised mission control or comparative gains. [C-01, C-09]
8. **Close on the real significance.** One planning step was tested with generative AI alongside established engineering checks. [C-08]

## 4. Spoken draft (828 spoken words; source and production cues excluded)

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

Here is what the public accounts establish: in the workflow described publicly, people framed and ran the demonstration, reviewed and simulated its output, adjusted part of the route, and sent the resulting commands. NASA’s earlier description of normal Perseverance operations says specialists develop the navigation and activity plan, sign off, and beam instructions to Mars. [**Verified fact:** C-01, C-02, C-07]

For this story, we can follow the actual handoffs without guessing who had authority over every possible mission decision. [**Analysis:** editorial limitation]

Now move from Earth to the rover.

Route planning is not the same as local navigation. Orbital images provide the big picture, but they cannot reveal every drive-scale obstacle. Perseverance already had an onboard system called AutoNav. Its navigation cameras feed software that builds three-dimensional maps of nearby terrain, identifies hazards, and selects a path around obstacles without asking Earth about each wheel movement. [**Verified fact:** C-02]

We saw that division of labor before this generative-AI test. In 2023, human planners mapped Perseverance’s general route through a boulder field called Snowdrift Peak. AutoNav handled the finer path, including detours around rocks that were not visible in the orbital imagery. [**Verified fact:** C-03]

There is a useful distinction here for anyone who writes software. Choosing a destination, proposing a route, checking that proposal, and reacting to nearby obstacles are separate jobs. A change to one job does not tell us that the others have disappeared. Think of the diagram as a set of responsibilities, rather than a single box labeled artificial intelligence. [**Analysis:** C-08; **Proposal:** teaching analogy]

[ON SCREEN: Orbital route with widely spaced dots beside rover-camera view bending around a rock.]

So the new part was not that Perseverance suddenly learned to avoid a rock. The new part was upstream: a generative model drafted the waypoint trail normally prepared by human route planners. Existing onboard software still handled a different problem—choosing safe, immediate motion through terrain the rover could see. [**Analysis:** C-08]

That is why saying simply “AI drove on Mars” is misleading. Perseverance does not have one all-purpose AI brain. Its autonomy consists of bounded capabilities. A JPL operations paper describes drive plans that start with a directly specified path, then switch to AutoNav and use intermediate waypoints. In that mode, the rover handles hazard avoidance locally. This is a concrete example of different kinds of control working together within one drive. [**Verified fact:** C-05]

[ON SCREEN: “What was demonstrated / What remains unknown”]

What did these two drives demonstrate? A vision-language model generated waypoints from mission data. The commands passed the team’s checks. Perseverance then completed both drives. [**Verified fact:** C-01]

What did they not establish? They did not show a generative model independently running the rover mission, authorizing its own commands, or replacing AutoNav. Successful completion alone also does not prove that the new method is safer or saves operators time. Those are separate questions requiring comparative evidence. The releases checked for this episode do not establish an independently validated answer. [**Analysis / open question:** C-09]

The careful conclusion is still remarkable. Engineers tested generative AI in one consequential piece of interplanetary route planning, checked its work, and placed it inside an established operational stack. The useful question to carry into the next AI headline is: which decision moved, what information did that system have, and who or what checked the result? On Mars, following those handoffs gives us a much clearer picture of what was achieved. [**Analysis:** C-08]

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

**Proposal.** Use the original conceptual handoff diagram in the review packet. This revision removes the vendor time-saving estimate and the historical ENav percentage from narration, corrects source metadata, and recommends the article companion. Format selection and final tone remain Carlos’s decisions.

## 7. Unresolved-question and editorial-risk register

| Item | Label | Why unresolved / risk | Required treatment or owner |
| --- | --- | --- | --- |
| Which person or mission role formally authorized each command set? | **Open question** | Public sources describe review and transmission but not a complete responsibility matrix. | Carlos decides whether the narrow workflow wording is sufficient; otherwise request a primary mission-operations source before assertion. |
| Did generative waypoint planning reduce planning time, improve safety, or improve consistency? | **Open question** | Only the vendor publishes a time-saving estimate; no comparative NASA dataset or peer-reviewed evaluation was found. | Keep out of verified narration; attribute if retained. |
| Did the model generate final flight commands or draft route artifacts later converted by JPL tooling? | **Open question** | NASA says the AI created waypoints and the team processed drive commands; Anthropic says Claude wrote Rover Markup Language. The exact tool boundary is not fully documented. | Use “generated waypoints” as the stable cross-source claim. |
| “First AI-planned drive” terminology | **Analysis / risk** | “AI” can obscure decades of onboard autonomous navigation; NASA’s claim refers specifically to planning drives on another world. | Always explain the scope immediately. |
| Companion format | **Open question** | Approved plan records no selection. | Carlos selects article or notebook; notebook then receives technical QA. |
| Visual assets | **Open question / copyright risk** | This package does not clear any external visual asset. Use the original conceptual diagram in the review packet while production assets remain undecided. | Obtain asset-specific credit/use review before production. No asset download is authorized here. |
| Vendor framing | **Analysis / conflict risk** | Anthropic benefits reputationally from the story. | Use its page only for attributed implementation detail and flag unverified promotional/future claims. |
| Investment or sponsorship implications | **Analysis / risk** | AI/space coverage can be read as endorsement. | Include no investment advice, valuation language, affiliate framing, or implied sponsor endorsement. |

## 8. Research and verification disclosure

**Verified process statement.** This revision was checked independently by the Codex collaborator on 2026-09-05. The QA report identifies full-page checks, indexed primary-source excerpts, and publisher access failures separately. It does not claim full-text review of every paper. The script paraphrases sources and preserves claim cues; Carlos’s editorial acceptance remains pending.

**Draft for Carlos review — not for publication.**
