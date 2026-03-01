from sms_parser import parse_sms

# Real looking Indian bank SMS examples
sms_examples = [
    "Rs.350 debited from your account via UPI to zomato@okicici on 01-03-2026",
    "INR 1500 credited to your account from refund@ybl on 28-02-2026",
    "Rs.899 paid via UPI to amazon@apl. Your a/c XX1234 debited.",
    "₹250 debited via UPI to swiggy@icici on 01-03-2026",
    "Rs.50 sent to friend@oksbi from your account"
]

print("🧪 Testing SMS Parser...\n")

for sms in sms_examples:
    print(f"📱 SMS: {sms}")
    result = parse_sms(sms)
    print(f"✅ Result: {result}")
    print("-" * 60)


from categorizer import categorize_merchant

print("\n🏷️ Testing Categorizer...\n")

test_merchants = [
    "zomato",
    "amazon",
    "irctc",
    "bigbasket",
    "netflix",
    "airtel",
    "apollo",
    "byju",
    "randomshop",
    "friend"
]

for merchant in test_merchants:
    category = categorize_merchant(merchant)
    print(f"🏪 {merchant} → 🏷️ {category}")
