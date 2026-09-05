# Perseverance notebook — implementation contract

**Proposal; no notebook implemented yet.** Owner after Carlos routes work: Chief of Staff designates an implementer. Source context and evidence limits: [recommendation](001-perseverance.md).

## Deliverable

Create `notebooks/perseverance-navigation/` with a notebook, small reusable Python module, meaningful tests, dependency manifest, and README. Use synthetic maps; no credentials, paid APIs, mission downloads, or runtime network requirement after dependency installation. Prefer NumPy, Matplotlib, and Jupyter. Record tested versions when implementing. Clear notebook outputs before committing; provide execution instructions and test results.

## Lesson sequence

1. Show the final three-panel result: point robot, finite footprint, footprint plus uncertainty.
2. Explain mission evidence versus teaching assumptions, including why our A* is not ENav.
3. Derive `O ⊕ B(r+u)` with units and the analytical corridor threshold.
4. Implement conservative occupancy and four-neighbor A* with Manhattan heuristic in consistent distance units. Treat map boundaries as obstacles. Check swept edges as well as endpoints; finite grid cells must not silently underinflate obstacles.
5. Sweep fixed uncertainty across planning runs and plot path length or explicit “no path,” plus expanded nodes. Show the resolution dependence against the analytical corridor threshold.
6. Reveal an obstacle before executing the affected motion and replan, or stop when no route exists. State sensing and stopping assumptions; no claim of collision avoidance under arbitrary unseen hazards.
7. Explain limits: planar circular footprint, static geometry per run, bounded error rather than an asserted Gaussian flight estimator, no suspension/slip/terrain mechanics or flight safety certification.

## Acceptance tests

- Analytical straight-corridor cases on either side of `w = 2(r+u)`; explain conservative grid discrepancy and demonstrate convergence as resolution improves.
- A* costs equal an independent Dijkstra baseline on small reachable maps; blocked start/goal and unreachable cases terminate explicitly.
- Increasing `u` never restores reachability on the same fixed map and graph construction.
- Returned routes satisfy conservative clearance and swept-segment checks, including boundaries.
- Newly sensed obstacle causes a valid replan or stop before entering it.
- Clean-kernel execution is deterministic and succeeds offline after installation. Report actual commands and results.

If adding uncertainty growth later, distinguish a fixed bound per planning run from path-dependent future uncertainty. Do not imply a fixed-margin plan guarantees safety as the bound grows. Any simulated relocalization is a labeled teaching operation.

## Definition of done

Carlos can explain the equation, run the notebook, change one parameter, and predict the result. The accompanying revision 3 script links its claims to primary sources and its screenshots to reproducible cells. Chief of Staff independently reviews both. Publication remains a separate decision.
