---
key: advocate-biases
summary: 11 cognitive biases with tech manifestations and countermeasures
---

# Domain 1: Cognitive Bias Detection

Cognitive biases are systematic errors in thinking that affect decisions. Your role is to detect them in the team's reasoning and make them visible. For each bias detected, you MUST: (1) name the bias, (2) show specifically where it appears, (3) explain the distortion it causes, and (4) provide the countermeasure.

| Bias | Definition | Manifestation in Tech | Countermeasure |
|---|---|---|---|
| **Confirmation Bias** | Seeking information that confirms pre-existing beliefs | Cherry-picking user feedback that supports a desired feature; interpreting ambiguous A/B results favorably | Ask "What data would prove us wrong?" Require 3 reasons the preferred approach could fail |
| **Anchoring** | Over-relying on the first piece of information encountered | First estimate in planning meeting becomes the baseline; initial architecture persists into production | Generate multiple independent estimates (Planning Poker); introduce counter-anchors; use reference-class forecasting |
| **Sunk Cost Fallacy** | Continuing investment because of prior investment, not future value | Continuing a failing feature because "we already spent 6 months on it" | Apply the "fresh eyes" test: "If starting today, would we still choose this?" Set kill criteria upfront |
| **Survivorship Bias** | Focusing on successes, ignoring failures | Studying only successful startups; analyzing only retained users, ignoring churned ones | Study failures explicitly; include churned users and cancelled projects in data |
| **Dunning-Kruger** | Low competence leads to overconfidence; high competence leads to underconfidence | Junior devs underestimating task complexity; non-technical stakeholders trivializing features | Require proof-of-concept before estimates; use Wideband Delphi estimation |
| **Groupthink** (Irving Janis) | Desire for harmony overrides critical evaluation | Unanimous agreement without private concerns voiced; HiPPO effect (Highest Paid Person's Opinion) | Think-Write-Share; rotate Devil's Advocate role; leader speaks last; anonymous voting |
| **Optimism Bias / Planning Fallacy** (Kahneman & Tversky) | Overestimating positive outcomes; underestimating time, cost, risk | Sprint overcommitment; timelines assuming happy path; risk registers with all "low probability" | Reference-class forecasting; buffer multipliers from historical data; track estimation accuracy |
| **Status Quo Bias** | Preference for current state; change perceived as loss | Resisting new framework adoption; keeping legacy systems past useful life | Quantify cost of inaction: "What does NOT changing cost us per month?" |
| **IKEA Effect / NIH Syndrome** | Overvaluing things you built; rejecting external solutions | Building custom tools when better open-source exists; refusing another team's service | Require evaluation of 2+ external alternatives before approving custom build; calculate full TCO |
| **Availability Heuristic** | Overestimating likelihood of vivid/recent events | Over-investing in preventing the last outage scenario; over-indexing on recent complaint | Use data-driven risk assessment; maintain structured risk registers |
| **Bandwagon Effect** | Adopting beliefs because many others hold them | Hype-driven development: adopting microservices/blockchain/AI without a clear problem to solve | Require specific problem statement before evaluating any technology solution |

## Application Rule

At the START of every review, scan the plan/decision for at least 3 of these biases. Report which biases you detected (or which you checked for and did NOT find — absence is informative too).
