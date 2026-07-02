"""
example_usage.py -- Demonstrates the BrandVoiceClient SDK.
"""
from client import BrandVoiceClient

BRAND_PROFILE = {
    "tone": ["friendly", "empowering", "clear"],
    "values": ["quality", "sustainability", "community"],
    "prohibited_words": ["cheap", "crappy", "worst", "hate", "fail"],
    "preferred_words": ["premium", "sustainable", "community", "crafted", "trusted"],
    "persona": "inspiring guide",
    "use_contractions": True,
    "exclamation_limit": 1,
}

CONTENT_SAMPLES = [
    "Our premium skincare products are crafted with sustainable ingredients. You will love how your skin feels after just one week.",
    "This is basically the cheapest option you can get. We do not really care about quality. It is just okay.",
    "Leverage our synergistic paradigm to disrupt the holistic wellness ecosystem! Our products were designed by experts!! They are absolutely loved by many!!!",
    "Join our trusted community of 50,000 customers who have transformed their routines. We are here to empower your journey.",
    "The formula was tested and verified by dermatologists. It was developed over three years of research.",
]

def main():
    client = BrandVoiceClient(brand_profile=BRAND_PROFILE, strict_mode=False)
    result = client.audit(CONTENT_SAMPLES)

    print(f"Brand Voice Audit Results")
    print(f"Overall Consistency Score: {result['overall_score']}/100")
    print(f"Pieces Audited: {result['pieces_audited']}")
    print(f"Critical Issues: {len(result['critical_issues'])}")

    print("\nPer-Piece Results:")
    for r in result["audit_results"]:
        print(f"\n  Piece {r['index']+1}: Score {r['consistency_score']}/100")
        print(f"  Preview: {r['text_preview'][:70]}...")
        if r["issues"]:
            for issue in r["issues"]:
                sev = issue["severity"].upper()
                print(f"    [{sev}] {issue['detail']}")
        if r["suggestions"]:
            print(f"    Top suggestion: {r['suggestions'][0]}")

    if result["critical_issues"]:
        print("\nCritical Issues to Fix Immediately:")
        for ci in result["critical_issues"]:
            print(f"  Piece {ci['content_index']+1}: {ci['issue']['detail']}")

if __name__ == "__main__":
    main()
