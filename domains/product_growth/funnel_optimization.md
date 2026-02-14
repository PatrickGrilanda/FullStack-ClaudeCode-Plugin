---
key: growth-funnel
summary: Onboarding optimization, cohort analysis, and churn analysis with benchmarks
---

# Funnel Optimization & Onboarding

The fastest growth lever is usually improving the existing funnel, not adding new channels. Optimizing conversion at each stage compounds — a 10% improvement at each of 4 stages yields 46% more output, not 40%.

## Onboarding Optimization

### Time-to-Value (TTV)
The time from signup to the user experiencing the product's core value.

**Target:** Minimize to < 5 minutes.

Every additional step, field, or screen in the onboarding flow loses 10-20% of users. Ruthlessly cut anything that doesn't directly contribute to the user reaching the "aha moment."

### "Aha Moment" Identification

The specific action after which retention jumps significantly. This is determined by data analysis, not assumption.

**Famous examples:**
- **Facebook:** "7 friends in 10 days" — users who connected with 7 friends within their first 10 days retained at dramatically higher rates
- **Slack:** "2,000 messages sent" — teams that exchanged 2,000 messages became long-term customers
- **Dropbox:** "1 file in 1 folder" — users who saved at least one file to a Dropbox folder activated

**How to identify yours:**
1. Segment retained vs. churned users
2. Compare actions taken in the first session/week
3. Find the action with the highest correlation to long-term retention
4. Validate with controlled experiments

### Activation Checklist Pattern

Break onboarding into 3-5 clear steps:
1. Keep the checklist visible and persistent
2. Show progress (progress bar, completed steps)
3. Celebrate completion of each step (micro-rewards)
4. Guide users to the "aha moment" action as the final step
5. Auto-dismiss when complete, but allow revisiting

**Benchmarks:** Onboarding optimization typically yields 20-40% activation improvement when properly executed.

## Cohort Analysis

### Behavioral Cohorts
Group users by **actions taken**, not just signup date. Behavioral cohorts reveal what users DO that drives retention, while time-based cohorts only show when they signed up.

**Examples of behavioral cohort dimensions:**
- Users who completed onboarding vs. those who didn't
- Users who used feature X in their first week vs. those who didn't
- Users who invited a teammate vs. solo users

### Retention Curves

Plot retention at standard intervals: D1 / D7 / D30 / D60 / D90

**Key concepts:**
- **Flattening point:** The day where the retention curve levels off = the product's natural retention baseline. Users who make it past this point are likely long-term users.
- **Steep early drop:** Normal. Focus on reducing the slope between D1 and D7.
- **Never-flattening curve:** Critical problem — the product lacks a retention mechanism.

### Comparison Dimensions

Analyze cohorts across multiple dimensions to find what drives retention:
- **Acquisition channel:** Which channels bring users that retain best?
- **Signup period:** Is retention improving over time (product improvements)?
- **Plan type:** Do paid users retain better than free? Which tier retains best?
- **Geography:** Are there regional differences in retention?
- **First action taken:** Which initial actions predict long-term retention?

## Churn Analysis

### Voluntary vs. Involuntary Churn

**Voluntary churn (cancellations):**
- User actively decides to leave
- Requires exit surveys to understand reasons
- Address with product improvements, value communication, save offers
- Common reasons: not using enough, found alternative, too expensive, missing features

**Involuntary churn (failed payments):**
- User didn't intend to leave — payment failed
- Requires dunning flows (automated payment retry + notifications)
- Typically 20-40% of total churn in subscription businesses
- Address with: card update reminders, retry logic, grace periods, alternative payment methods

### Leading Indicators of Churn

Identify users at risk BEFORE they churn by monitoring:
- **Reduced usage frequency:** Login/session frequency declining week-over-week
- **Fewer core actions:** Users performing the key value action less often
- **Support escalation:** Increased support tickets or complaint severity
- **Login decline:** Decreasing login frequency or session duration

### Proactive Intervention

**Benchmark:** Proactive churn intervention can reduce churn by 20-30%.

Intervention strategies based on leading indicators:
- **Usage decline:** Trigger re-engagement emails, in-app nudges, feature highlights
- **Feature under-use:** Offer guided tours, webinars, or 1:1 onboarding for underused features
- **Support escalation:** Escalate to customer success for high-value accounts
- **Payment at risk:** Pre-dunning notifications, card expiry reminders

### Win-Back Campaigns

**Timing:** Target churned users within 30-60 days of churn (beyond 60 days, win-back rates drop significantly).

**Typical win-back rate:** 5-15% of churned users.

**Effective tactics:**
- Personalized messaging referencing their past usage and value received
- Limited-time discount or incentive to return
- Highlight new features or improvements since they left
- Make re-activation frictionless (one-click resubscribe)
