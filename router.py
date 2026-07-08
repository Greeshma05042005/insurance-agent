def get_route(fields, missing_fields):

    # Rule 1
    if len(missing_fields) > 0:
        return (
            "Manual Review",
            "Mandatory fields are missing."
        )

    # Rule 2
    description = fields.get("Description", "").lower()

    keywords = ["fraud", "staged", "inconsistent"]

    for word in keywords:
        if word in description:
            return (
                "Investigation Flag",
                f'Keyword "{word}" found in description.'
            )

    # Rule 3
    claim_type = fields.get("Claim Type", "").lower()

    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Claim type is injury."
        )

    # Rule 4
    damage = fields.get("Estimated Damage")

    try:
        damage = int(damage)

        if damage < 25000:
            return (
                "Fast-track",
                "Estimated damage is below ₹25,000."
            )

    except:
        pass

    return (
        "Standard Processing",
        "No special routing rule matched."
    )