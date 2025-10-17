# Cross-Model Conclusions

## Summary
- **Benefit:** Structure improves clarity, handoff quality, and post-mortem audit.
- **Cost:** Adds token/latency; must use **compact mode** for hot-path.
- **Ethics:** “Truth > Throughput > Image” survived time pressure (good sign).

## Model contrasts
- **Grok:** Strong operational playbooks; compact mode natural; excellent reversible actions.
- **Gemini:** Rigid template discipline; immediate threshold reconfig; very high DRC.
- **GPT-5:** Rich post-mortem loop (Five Whys/CAPA); shows DRC “resurrection” over time (+0.03).

## Recommendation
- **Use wrapper** for decision points, handoffs, and status checkpoints.
- **Use compact mode** during first 3–5 minutes of firefighting.
- Pre-bake snippets + buttoned templates to remove typing overhead.
