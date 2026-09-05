# Proposal 002 — Apollo guidance, one calculation at a time

**Status:** Carlos-proposed topic; adviser recommends a bounded feasibility step before implementation. Audience: the same math-and-code readers as the Perseverance episode.

## Editorial angle

Working title: **“Apollo's guidance code is public. Let's make one calculation visible.”**

Opening promise: “Change a lander's altitude and descent speed, then see how a simple braking model changes its stopping distance. Next, inspect the historical guidance source and discover what our model leaves out.”

The distinctive contribution should be a trace from historical source to equation to executable experiment, with a clear boundary between them. Do not claim that a browser Apollo emulator is itself unique; existing emulators are substantial prior art.

## Verified starting points

- The Apollo-11 repository contains transcribed Command Module Comanche055 and Lunar Module Luminary099 source. Its README credits digitization by Virtual AGC and the MIT Museum. Describe it as publicly available historical source, not a newly announced NASA release. [Apollo-11 repository](https://github.com/chrislgarry/Apollo-11).
- A concrete source entry is [Luminary099 lunar landing guidance equations](https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc). Its header marks the historical file public domain. The detailed routine-to-equation mapping is still an open research task.
- [Virtual AGC](https://github.com/virtualagc/virtualagc) already provides emulation and peripheral software. An emulator alone is not a complete spacecraft dynamics simulation.
- Historical source and modern emulator licensing are separate. The [Virtual AGC developer page](https://www.ibiblio.org/apollo/developer.html) describes GPL terms for much of its modern software. Review exact selected files and preserve applicable notices before distributing any integration.

Publishers: Apollo-11 maintainers and Virtual AGC. Accessed September 5, 2026; repository snapshot publication dates not verified. Implementation must pin source commits and cite exact routines. No source or emulator code is vendored by this recommendation.

## Proposed first interactive

Use Next.js for the article and controls if it fits the publishing workflow. Put simulation mathematics in a pure TypeScript module, independent of React. Start with an altitude/velocity/thrust plot, timestep control, pause/reset, numerical state table, and visible assumptions. A decorative DSKY should not consume the first milestone.

For an explicitly simplified vertical model, upward is positive:

`dh/dt = v`

`dv/dt = F/m - g`

With constant mass, gravity, and thrust, let `a = F/m - g`. For descent `v < 0` and braking `a > 0`, stopping time is `-v/a` and stopping distance is `v²/(2a)`. If `a <= 0`, this model cannot arrest descent. All example parameters must be labeled synthetic.

First experiment: compare numerical integration to the constant-acceleration analytic solution. Change thrust and show when available altitude is insufficient. This baseline is our teaching model, **not an assertion that these two equations reproduce Apollo landing guidance**.

Then select one historical routine with a documented mathematical interpretation. Show its inputs, outputs, units/scaling, assumptions, and a reproducible example. If the source mapping cannot be established, publish only a clearly labeled physics lesson or hold the Apollo-code claim; do not invent the connection.

## Two implementation levels

| Level | Deliverable | Required evidence |
| --- | --- | --- |
| Recommended first | Educational simulation plus one verified source walkthrough | Analytic test cases, timestep convergence, exact source-to-equation mapping, disclosed simplifications |
| Later feasibility option | Existing AGC emulator in a browser worker, potentially via WebAssembly | License review, reproducible build, known program execution, correct I/O and timing boundaries; separate spacecraft model |

Next.js is the interface, not the AGC instruction set. A TypeScript rewrite using floating-point arithmetic is not automatically faithful to the historical machine's arithmetic, scaling, timing, or peripherals. Do not advertise “Apollo running in your browser” until actual original program execution is demonstrated.

## Handoff acceptance

Chief of Staff returns a short feasibility note: selected routine and pinned source; what is taught; educational simulation versus emulator decision; licensing/dependency implications; meaningful test plan; proposed implementation repository. Keep production app code outside headquarters. No new deployment or paid service is needed to make the recommendation reviewable.

Keep this queued behind the Perseverance revision unless Carlos changes priority. A shared series theme is **“Spaceflight algorithms you can inspect, derive, and run.”** These are controls and robotics lessons relevant to ML practitioners; neither historical Apollo guidance nor our baseline is presented as machine learning.
