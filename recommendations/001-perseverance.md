# Proposal 001 — Why a Mars rover can stop when the route looks clear

**Status:** adviser proposal for SPA-12 revision 3; implementation pending. Audience: ML engineers and developers curious about robotics. Prerequisites: Python, vectors, basic search. Companion: one small notebook.

## Opening draft

“A route can be geometrically open and still be unusable to a robot that is uncertain where it is. In this notebook, we'll add the robot's size and position-error bound to an obstacle map, run a path planner, and watch a corridor disappear. You'll learn exactly which assumption makes the route fail—and which parts of this experiment resemble Perseverance's documented navigation.”

Show the route and uncertainty slider immediately. Then introduce the mission evidence, the equation, and the experiment. Keep the Claude story as a short distinction, rather than the central technical lesson.

## Verified mission context

| Component | What the evidence supports | Scope |
| --- | --- | --- |
| Stereo vision and visual odometry | Geometry-based ranging and motion estimation are part of the mobility stack. | Onboard; [JPL mobility overview](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/mars-2020-rover/m2020mobility/). |
| ENav / ACE | The 2020 design describes conservative attitude, suspension, and clearance bounds, and a greedy multi-level planner. | Prelaunch design, not an A* implementation claim; [McHenry et al., 2020](https://robotics.jpl.nasa.gov/media/documents/AAS_2020_mobility_mmc_v10.pdf), pp. 11–12. |
| Global position uncertainty | Expanding keep-out regions can eliminate viable routes; the paper describes a sol 385 example. | Historical operations; [Verma et al., 2024](https://robotics.jpl.nasa.gov/media/documents/2024_Global_Localization_IEEE_Aero.pdf), section 2, figures 3–4. Indexed passage inspected; full PDF review remains an implementation research task. |
| Claude waypoint experiment | A ground workflow generated waypoints that engineers checked before uplink. | Separate from onboard control; [JPL, January 30, 2026](https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/). Exact checkpoint, weights, and training details are not established by this release. |

All sources accessed September 5, 2026. JPL mobility page has no verified publication date in this review. This lesson teaches model-based robotics relevant to ML systems; it does not claim to reproduce a flown neural network.

## Analysis: one equation worth understanding

For a circular teaching robot of radius `r` and bounded planar position error `u`, inflate obstacle set `O`:

`O_forbidden = O ⊕ B(r + u)`

Here `⊕` is the Minkowski sum and `B(a)` is a disk of radius `a`. The planner searches for the robot's center outside this set. In an ideal straight corridor of width `w`, passage requires `w > 2(r + u)` when contact counts as collision.

Synthetic example: `w = 3 m`, `r = 0.5 m`. With `u = 0.2 m`, there is 1.6 m of center-position slack; with `u = 1.1 m`, no passage remains. These are teaching parameters, not rover dimensions or flight thresholds. A* is our transparent baseline, not a claim about ENav's search algorithm. Global position error, stereo depth error, and local wheel-placement/slip allowances must not be conflated.

## Weather is a second, narrower lesson

**Verified fact:** the onboard planner's verification paper describes colder-than-predicted thermal conditions extending preheating, delaying an activity, and potentially causing veto/rescheduling. This is concrete event-driven adaptation, not evidence of a general autonomous weather forecaster. [Parjan and Gaines, 2024, p. 4](https://ai.jpl.nasa.gov/public/documents/papers/parjan-ieee2024-m2020.pdf), accessed September 5, 2026.

**Proposal:** later isolate thermal eligibility using `C dT/dt = P_heater - k(T - T_environment)` and an energy budget, with synthetic parameters and explicit simplifications. Perseverance uses an MMRTG and batteries; do not invent solar-panel dust shutdown behavior. [JPL 2020 launch press kit](https://www.jpl.nasa.gov/news/press_kits/mars_2020/launch/mission/spacecraft/power/), accessed September 5, 2026.

First deliver the navigation notebook. Thermal scheduling and stereo depth uncertainty are follow-ups, not additions to its first version.
