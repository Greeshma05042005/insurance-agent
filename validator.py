mandatory_fields = [
    "Policy Number",
    "Policyholder Name",
    "Date",
    "Time",
    "Location",
    "Description",
    "Claimant",
    "Contact Details",
    "Asset Type",
    "Asset ID",
    "Estimated Damage",
    "Claim Type",
    "Attachments",
    "Initial Estimate"
]


def validate_fields(data):

    missing = []

    for field in mandatory_fields:

        if data.get(field) is None or data.get(field) == "":
            missing.append(field)

    return missing