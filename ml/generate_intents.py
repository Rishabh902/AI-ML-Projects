# import json
# import random
# import os
# # Base intents
# intents_data = {
#     "greeting": [
#         "hello", "hi", "hey", "good morning", "good evening",
#         "good afternoon", "hi there", "hey there"
#     ],
#     "goodbye": [
#         "bye", "goodbye", "see you", "talk later",
#         "see you soon", "catch you later"
#     ],
#     "order_status": [
#         "check my order", "where is my order",
#         "track my order", "order status",
#         "has my order shipped"
#     ],
#     "refund_policy": [
#         "refund policy", "can I get refund",
#         "money back policy", "how to request refund"
#     ],
#     "payment_methods": [
#         "payment options", "how can I pay",
#         "accepted payment methods", "do you accept UPI"
#     ],
#     "reset_password": [
#         "forgot password", "reset my password",
#         "change my password", "password help"
#     ],
#     "contact_number": [
#         "contact number", "phone number",
#         "how can I call you", "support number"
#     ],
#     "email_support": [
#         "support email", "email address",
#         "how to email you", "customer support email"
#     ],
#     "services": [
#         "what services do you offer",
#         "your services",
#         "what do you provide",
#         "service details"
#     ],
#     "pricing": [
#         "pricing details",
#         "what is the cost",
#         "how much do you charge",
#         "price information"
#     ]
# }

# extra_phrases = [
#     "please",
#     "right now",
#     "as soon as possible",
#     "quickly",
#     "today",
#     "for me",
#     "immediately",
#     "can you tell me",
#     "I want to know",
#     "could you please"
# ]

# def generate_variations(base_list, total=200):
#     patterns = []

#     for _ in range(total):
#         base = random.choice(base_list)
#         extra = random.choice(extra_phrases)

#         variations = [
#             base,
#             f"{extra} {base}",
#             f"{base} {extra}",
#             f"{extra} about {base}",
#             f"I need {base}",
#             f"I would like to know {base}",
#             f"Can you help me with {base}",
#             f"Please tell me {base}"
#         ]

#         patterns.append(random.choice(variations))

#     return patterns
# final_intents = []

# for tag, base_patterns in intents_data.items():
#     patterns = generate_variations(base_patterns, total=200)

#     intent = {
#         "tag": tag,
#         "patterns": patterns,
#         "responses": [f"This is response for {tag}."]
#     }

#     final_intents.append(intent)

# data = {"intents": final_intents}
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_DIR = os.path.join(BASE_DIR, "data")

# # ✅ Create data folder if not exists
# os.makedirs(DATA_DIR, exist_ok=True)

# DATA_PATH = os.path.join(DATA_DIR, "intents.json")

# with open(DATA_PATH, "w") as f:
#     json.dump(data, f, indent=4)

# print("✅ 200 patterns per intent generated successfully!")