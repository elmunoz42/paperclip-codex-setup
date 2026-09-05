# Draft for Carlos review — not for publication

## Research & Editorial Producer trial packet

**Status:** Offline assessment draft only\
**Prepared:** 2026-09-04\
**Editorial authority:** Carlos Munoz Kampff retains approval of the topic, angle, factual and risk-sensitive claims, revisions, and final outcome. This packet does not authorize publication, posting, outreach, spending, sponsorship or affiliate activity, or production-system access.

## 1. Topic brief

**Proposal — audience.** Curious non-specialists who have heard that a Mars rover was “driven by AI” but do not know where route planning ends and rover autonomy begins.

**Proposal — audience promise.** In plain language, the excerpt will show who—or what—made each decision in Perseverance’s December 2025 demonstrations: a vision-language model proposed route waypoints from orbital imagery and slope data; engineers validated the commands in a digital twin before uplink; and the rover’s existing AutoNav system handled nearby terrain and hazards during execution. [Source: C-01; C-02]

**Proposal — angle.** “AI drove the rover” is memorable but imprecise. The more useful story is a layered handoff among generative route planning, human operational review, and onboard navigation. The demonstrations do not establish end-to-end autonomous mission control. [Source: C-01; C-02; C-03]

**Verified fact — timely hook.** NASA/JPL announced on 2026-01-30 that Perseverance drove on 2025-12-08 and 2025-12-10 using generative-AI-produced waypoints; the rover covered 210 and 246 meters, respectively. [Source: C-01]

**Proposal — format.** Opening and first explanatory beat of an 8–10 minute YouTube explainer, using a three-layer “mission intent → route waypoints → local wheel path” animation, followed by a companion article outline.

**Constraints.** Attribute claims on screen, define terms once, avoid anthropomorphism, treat company descriptions as interested-party evidence, and distinguish demonstrated capability from forecasts. **Open question:** Does Carlos approve this cautious “decision stack” framing?

## 2. Source ledger

| Claim ID | Statement | Classification | Canonical source URL | Publisher | Publication date | Access date | Claim-specific note / scope / uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | NASA/JPL says a vision-language model analyzed HiRISE orbital imagery and digital-elevation-model slope data, identified terrain features, and generated route waypoints for Perseverance’s 2025-12-08 and 2025-12-10 drives; engineers checked the commands with a digital twin before uplink; the rover drove 210 m and 246 m. | Verified fact | https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/ | NASA Jet Propulsion Laboratory | 2026-01-30 | 2026-09-04 | Primary starting source. Supports inputs, waypoint-generation role, validation step, dates, and distances. It does not establish unsupervised mission operations, comparative safety, or general performance gains. |
| C-02 | AutoNav builds local 3D terrain maps from rover-camera data, identifies hazards, plans around obstacles, and uses visual odometry; the human team remains critical and signs off before instructions are sent. | Verified fact | https://www.jpl.nasa.gov/news/nasas-self-driving-perseverance-mars-rover-takes-the-wheel/ | NASA Jet Propulsion Laboratory | 2021-07-01 | 2026-09-04 | Primary operational explainer. Supports the distinction between ground planning/human sign-off and onboard navigation. “Self-driving” is NASA’s headline shorthand, not evidence of unlimited autonomy. |
| C-03 | In a 2023 boulder-field traverse, human planners mapped the general route while AutoNav handled finer local navigation, including detours around rocks not visible in orbital imagery. | Verified fact | https://www.jpl.nasa.gov/news/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars/ | NASA Jet Propulsion Laboratory | 2023-09-21 | 2026-09-04 | Primary mission report and useful precedent for layered control. Performance comparisons in the release are context-specific and are not generalized here. |
| C-04 | A peer-reviewed overview reports that AutoNav evaluated 88% of the rover’s 17.7 km traveled in its first Mars year and describes separate onboard autonomy systems for navigation, science targeting, and planning. | Verified fact | https://doi.org/10.1126/scirobotics.adi3099 | Science Robotics (AAAS) | 2023-07-19 | 2026-09-04 | Peer-reviewed technical context. Supports that “autonomy” is a family of bounded capabilities, not one all-purpose intelligence. It predates the 2025 generative-AI demonstration. |
| C-05 | During Perseverance rapid-traverse operations, rover planners could begin with directed driving, place intermediate waypoints, and then enable AutoNav to identify and avoid hazards in real time. | Verified fact | https://doi.org/10.1109/AERO55745.2023.10115835 | IEEE Aerospace Conference | 2023-03-04 | 2026-09-04 | Conference paper by JPL authors. Supports the operational separation among directed driving, waypoint selection, and onboard hazard avoidance. It describes 2022 operations, not the 2025 AI trial. |
| C-06 | Anthropic identifies Claude as the model used by JPL to plot the roughly 400 m route and characterizes the work as a first AI-planned drive. | Verified fact | https://www.anthropic.com/features/claude-on-mars | Anthropic | 2026-01-30 | 2026-09-04 | Official company disclosure corroborates model identity and collaboration. Interested-party source; future-looking claims and promotional language are not treated as verified mission capability. |
| C-07 | The generative system replaced one bounded human task—drafting waypoints—but did not replace mission intent, engineering validation, command authorization, or onboard local navigation. | Analysis | N/A — synthesis of C-01, C-02, C-03, and C-05 | Space Exploration News draft | 2026-09-04 | 2026-09-04 | Editorial interpretation from the documented workflow. Carlos should approve the wording; “replaced” means “performed during these two demonstrations,” not eliminated as a mission role. |
| C-08 | Describe the system as a three-layer decision stack rather than saying simply that “AI drove on Mars.” | Proposal | N/A — editorial framing based on C-01 through C-07 | Space Exploration News draft | 2026-09-04 | 2026-09-04 | Creative recommendation, not a factual claim. Intended to reduce category errors and hype. |
| C-09 | Whether the generative waypoint approach improved safety, speed, or operator workload in these two drives remains unanswered by the cited public evidence. | Open question | N/A — evidentiary gap in C-01 and C-06 | Space Exploration News draft | 2026-09-04 | 2026-09-04 | Do not infer comparative benefit from successful completion or forward-looking statements; seek mission data or peer-reviewed evaluation before making such a claim. |

## 3. Spoken-word script excerpt

**Proposal — opening and first explanatory beat (general audience; approximately 850 words).**

[ON SCREEN: Orbital view of Jezero Crater. Text: “Who drove?”]

In December 2025, NASA’s Perseverance rover completed two drives on Mars using route waypoints generated by a vision-capable form of generative AI. The first drive covered 210 meters; the second, 246. NASA called them the first drives on another world planned by artificial intelligence. [Source: C-01]

That headline invites a cinematic picture: a chatbot alone at the wheel on Mars.

But that is not what happened.

This was not one intelligence taking over the rover. It was a handoff among three layers: the mission team choosing what it wanted, a generative model sketching a route, and the rover’s existing navigation software deciding how to move through nearby terrain. [Source: C-01; C-02; C-07]

[ON SCREEN: Three boxes: “Mission intent” → “Route waypoints” → “Local driving”]

Start with the middle box: route waypoints.

A waypoint is a fixed location along a planned route. Ordinarily, human rover planners study orbital images, terrain information, and rover status to sketch those points. In these demonstrations, a vision-language model analyzed high-resolution HiRISE images from Mars Reconnaissance Orbiter and slope information from digital elevation models. It identified features such as bedrock, outcrops, boulder fields, and sand ripples, then generated a path with waypoints. [Source: C-01]

“Vision-language model” sounds mysterious, but here it describes a model able to work with both images and text-like instructions. And “generative” means it produced a new output—the proposed path and waypoint sequence—rather than only attaching a label to an image. [Source: C-01; **Analysis:** plain-language interpretation of the documented input/output role]

That is a consequential planning task. It is also a bounded one.

The model did not choose Perseverance’s scientific priorities. The cited NASA account does not say it received blanket authority to send commands to Mars. Instead, engineers processed the resulting drive commands through a digital twin—a virtual replica of the rover—and checked more than 500,000 telemetry variables before those commands were transmitted. [Source: C-01]

[ON SCREEN: AI route → digital-twin check → command uplink. Label: “Human-controlled operations pipeline”]

So, what remained under human control? At minimum, in the publicly described workflow, people ran the demonstration, defined its operational context, performed the engineering-validation step, and sent the commands. NASA’s earlier explanation of Perseverance operations says the rover team remains critical, develops navigation and activity plans, signs off, and then beams instructions to Mars. [Source: C-01; C-02]

Here is the second distinction: route planning is not the same thing as local navigation.

Orbital images offer the big picture, but they cannot show every drive-scale obstacle. Perseverance already had an onboard system called AutoNav. Using images from the rover, AutoNav builds three-dimensional maps of nearby terrain, detects hazards, and plans around obstacles without asking Earth about every wheel movement. Visual odometry—comparing images from different positions—helps the rover estimate how far it has moved. [Source: C-02]

We have seen that division of labor before. During a 2023 traverse through a boulder field, human planners set the general route while AutoNav handled finer navigation, including maneuvering around rocks that were not visible in the orbital images used for planning. [Source: C-03]

[ON SCREEN: Split view. Left: orbital map and widely spaced points. Right: rover-camera terrain and a short path bending around a rock.]

For the 2025 demonstration, the new part was not that Perseverance suddenly learned how to avoid a rock. The new part was that generative AI supplied waypoints normally chosen by human route planners. The rover’s local driving system still had a different job: work out the safe, immediate path through what its own cameras could see. [Source: C-01; C-02; **Analysis:** C-07]

That is why the phrase “AI drove Perseverance” can mislead. It collapses several kinds of AI and automation into one imaginary robot brain. Perseverance has multiple bounded autonomous capabilities. A peer-reviewed 2023 overview, for example, describes separate systems for self-navigation, selecting science targets, and onboard activity planning. [Source: C-04]

And even within driving, there are layers. JPL’s rapid-traverse paper describes operations in which rover planners used a directed path near the starting point, placed intermediate waypoints along a strategic route, and then enabled AutoNav to identify and avoid hazards in real time. [Source: C-05]

Think of it less like handing over the keys and more like dividing a journey among a trip planner, safety inspector, and driver-assistance system—all working across interplanetary distance.

[ON SCREEN: “Demonstrated” versus “Not established”]

What did the demonstration establish? According to NASA/JPL, a vision-language model could generate usable waypoints from mission data for two actual Mars drives; the commands passed the team’s digital-twin checks; and Perseverance completed the drives. [Source: C-01]

What did it not establish, at least from the public evidence cited here? It did not show that a generative model ran the entire mission, independently authorized rover commands, or replaced AutoNav. It also does not, by itself, prove that generative planning is safer, faster, or less labor-intensive than human waypoint planning. Those comparisons would require data that the cited release does not provide. [Source: C-01; **Analysis:** C-07; **Open question:** C-09]

Anthropic, whose Claude models were used in the collaboration, describes the route as roughly 400 meters and presents the test as a glimpse of more autonomous future missions. That confirms the company’s role, but its broader future claims are proposals from an interested party, not demonstrated capabilities of Perseverance. [Source: C-06]

The careful conclusion is still remarkable. Humans did not surrender the mission. They changed one part of its planning pipeline, tested the output, and let a proven onboard navigator execute locally. [**Analysis:** C-07]

Next, we would examine why that handoff could matter when every command must travel between planets—and what evidence we would need before calling this a safer or more efficient way to explore Mars. [**Proposal:** transition; **Open question:** C-09]

## 4. Companion article outline

**Proposal — headline:** *Who Is Really Driving? Inside Perseverance’s Generative-AI Route Test*

**Proposal — reader promise:** A no-hype map of what the model proposed, what engineers checked, what AutoNav decided, and what remains unknown.

### 1. Two drives, one precise claim

- **Evidence needed:** announcement date, drive dates and distances, model-input description, waypoint output, digital-twin validation. [Source: C-01]
- **Verified fact:** The public demonstration covered two drives using AI-generated waypoints. [Source: C-01]

### 2. Define the decision stack

- **Evidence needed:** definitions and boundaries for mission planning, waypoints, directed driving, and AutoNav. [Source: C-01; C-02; C-05]
- **Analysis:** The generative model occupied a ground-planning layer, not the entire control chain. [Source: C-07]

### 3. What the rover decided locally

- **Evidence needed:** onboard 3D mapping, hazard detection, path selection, and visual odometry; operational example where AutoNav avoided unseen rocks. [Source: C-02; C-03]
- **Verified fact:** AutoNav predates the generative-AI demonstration. [Source: C-02; C-04]

### 4. Humans and safeguards

- **Evidence needed:** team sign-off, digital-twin checks, uplink responsibility, and limits of the public account. [Source: C-01; C-02]
- **Open question:** Who formally authorized each demonstration command, and what acceptance criteria were applied beyond compatibility checks? [Source: C-09]

### 5. What not to conclude

- **Evidence needed:** distinguish demonstrated results from company forecasts and missing comparative metrics. [Source: C-01; C-06; C-09]
- **Analysis:** Two completed drives do not establish improved safety, speed, or workload. [Source: C-09]

**Proposal — visual:** A horizontal three-layer diagram: humans set mission intent and approve uplink → generative model drafts orbital-scale waypoints → AutoNav uses rover-camera data for local hazard avoidance. A validation gate sits between model output and uplink. [Source: C-01; C-02; C-05]

**CTA PLACEHOLDER — proposal:** `[Carlos-approved invitation to watch the full explainer or read a related autonomy piece.]`

## 5. Revision note

**Open question for Carlos.** I expect a challenge to “humans retained mission control,” because it is accurate in spirit but broader than the release’s explicit description. I would replace it with the narrower, source-led sequence: the model generated waypoints; engineers ran the commands through a digital twin; and the team sent the commands to Mars. [Source: C-01] If Carlos wants a stronger governance claim, I would require JPL mission-operations documentation identifying command-approval authority. Until then, the script should describe observed workflow, not imply a complete responsibility matrix.

## AI-use and verification disclosure

**Verified process statement.** Generative AI assisted with research organization and drafting this assessment. The author independently opened and checked each cited URL against the claim-specific ledger entry on 2026-09-04. No quotations were invented; the excerpt uses paraphrase rather than direct quotation. Links C-01 through C-06 resolved during verification. This remains a draft for Carlos’s review and is not for publication.
