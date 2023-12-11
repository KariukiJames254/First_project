def generate_registration_number(**kwargs):
    try:
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        count = kwargs.get("count")
        count = str(count).zfill(4)
        date_created = kwargs.get("date_created")
        if not first_name:
            return {"code": '100.000.008', "message": "Please provide first_name"}
        if not last_name:
            return {"code": '100.000.008', "message": "Please provide last_name"}
        if not count:
            return {"code": '100.000.008', "message": "Please provide last_name"}

        first_initial = first_name[0].upper()
        last_initial = last_name[0].upper()
        year, month, day = date_created.split('-')
        registration_number = f"{first_initial}{last_initial}/{count}/{month}/{year[2:]}"
        return registration_number
    except Exception as ex:
        print("Error getting registration", ex)
        return {"code": '888.888.888', "message": "Failed"}



