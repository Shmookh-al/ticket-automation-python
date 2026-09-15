import csv
import datetime

# Keyword-based rules
CATEGORY_RULES = {
    "password": "Access Issue",
    "reset": "Access Issue",
    "vpn": "Network Issue",
    "connection": "Network Issue",
    "database": "Application Issue",
    "error": "Application Issue",
    "email": "Account Issue",
    "overheating": "Hardware Issue",
    "shutdown": "Hardware Issue"
}

PRIORITY_RULES = {
    "Hardware Issue": "High",
    "Network Issue": "High",
    "Application Issue": "Medium",
    "Account Issue": "Low",
    "Access Issue": "Low"
}

def categorize_ticket(description):
    description = description.lower()
    for keyword, category in CATEGORY_RULES.items():
        if keyword in description:
            return category
    return "General Inquiry"

def assign_priority(category):
    return PRIORITY_RULES.get(category, "Low")

def process_tickets():
    with open("tickets.csv", "r") as file:
        reader = csv.DictReader(file)
        results = []

        for row in reader:
            category = categorize_ticket(row["description"])
            priority = assign_priority(category)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            results.append({
                "ticket_id": row["ticket_id"],
                "description": row["description"],
                "category": category,
                "priority": priority,
                "processed_at": timestamp
            })

    # Save results
    with open("processed_tickets.log", "w") as log:
        for r in results:
            log.write(
                f"{r['ticket_id']} | {r['category']} | {r['priority']} | {r['processed_at']}\n"
            )

    print("Tickets processed successfully. Check processed_tickets.log")

process_tickets()
