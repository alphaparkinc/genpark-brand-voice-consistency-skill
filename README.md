# genpark-brand-voice-consistency-skill

> **GenPark AI Agent Skill** — Audit and enforce brand voice consistency across marketing content.

## Features

- Prohibited word detection with severity classification
- Preferred brand word usage scoring
- Passive voice detection
- Filler word density analysis
- Corporate jargon detection
- Sentence length compliance
- Exclamation mark overuse flagging
- Contraction usage enforcement
- Per-piece scores and actionable rewrite suggestions

## Quick Start

```python
from client import BrandVoiceClient

brand_profile = {
    "tone": ["friendly", "professional"],
    "prohibited_words": ["cheap", "fail"],
    "preferred_words": ["premium", "trusted"],
    "use_contractions": True,
    "exclamation_limit": 1,
}

client = BrandVoiceClient(brand_profile=brand_profile)
result = client.audit(["Our products are cheap and basically okay."])
print(f"Score: {result['audit_results'][0]['consistency_score']}/100")
```

## Installation

```bash
python example_usage.py  # No external dependencies
```

---
Built by [GenPark](https://genpark.ai) | [alphaparkinc](https://github.com/alphaparkinc)
